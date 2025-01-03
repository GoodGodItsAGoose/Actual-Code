import base64
import pyperclip

def encode_to_base64(input_string, security_level, other_encoding):
    #Convert the input string to bytes
    if other_encoding == None:
        input_bytes = bytes(input_string, "cp1252")
    else:
        input_bytes = bytes(input_string, other_encoding)

    #Encode the bytes to Base64 using the security level to encode
    if security_level == "1": # note: maybe make 2-3?
        for i in range(int(security_level)+2):
            encoded_bytes=base64.b32encode(input_bytes)
            encoded_bytes=base64.b85encode(encoded_bytes)
    elif security_level == "2": # note: maybe make 2-4?
        for i in range(int(security_level)+3):
            encoded_bytes=base64.a85encode(input_bytes)
            encoded_bytes=base64.b64encode(encoded_bytes)
            encoded_bytes=base64.b16encode(encoded_bytes)
            encoded_bytes=base64.a85encode(encoded_bytes)
    elif security_level == "3": # note: maybe make 3-6?
        for i in range(int(security_level)*4):
            encoded_bytes=base64.b16encode(input_bytes)
            encoded_bytes=base64.b64encode(encoded_bytes)
            encoded_bytes=base64.a85encode(encoded_bytes)
            encoded_bytes=base64.b85encode(encoded_bytes)
            encoded_bytes=base64.b32encode(encoded_bytes)
            encoded_bytes=base64.b16encode(encoded_bytes)
    elif security_level == "4": # note: maybe make 5-8?
        for i in range(int(security_level)*7):
            encoded_bytes=base64.b85encode(input_bytes)
            encoded_bytes=base64.b64encode(encoded_bytes)
            encoded_bytes=base64.b16encode(encoded_bytes)
            encoded_bytes=base64.b32encode(encoded_bytes)
            encoded_bytes=base64.a85encode(encoded_bytes)
            encoded_bytes=base64.b64encode(encoded_bytes)
    elif security_level == "5": # note: maybe make 7-11?
        for i in range(int(security_level)*10):
            encoded_bytes=base64.b32encode(input_bytes)
            encoded_bytes=base64.b64encode(encoded_bytes)
            encoded_bytes=base64.b16encode(encoded_bytes)
            encoded_bytes=base64.b85encode(encoded_bytes)
            encoded_bytes=base64.a85encode(encoded_bytes)
            encoded_bytes=base64.b16encode(encoded_bytes)
            encoded_bytes=base64.a85encode(encoded_bytes)

    # Convert the Base64 bytes back to a string
    if other_encoding == None:
        base64_string = encoded_bytes.decode("cp1252")
    else:
        base64_string = encoded_bytes.decode(other_encoding)

    return base64_string

def decode(base64_string, security_level, other_encoding):
    #Convert the Base64 string to bytes
    if other_encoding == None:
        base64_bytes = bytes(base64_string, "cp1252")
    else:
        base64_bytes = bytes(base64_string, other_encoding)
    
    #Decode the Base64 bytes back to the original bytes using the security level to decode
    if security_level == "1":
        for i in range(int(security_level)+2):
            decoded_bytes=base64.b85decode(base64_bytes)
            decoded_bytes=base64.b32decode(decoded_bytes)
    elif security_level == "2":
        for i in range(int(security_level)+3):
            decoded_bytes=base64.a85decode(base64_bytes)
            decoded_bytes=base64.b16decode(decoded_bytes)
            decoded_bytes=base64.b64decode(decoded_bytes)
            decoded_bytes=base64.a85decode(decoded_bytes)
    elif security_level == "3":
        for i in range(int(security_level)*4):
            decoded_bytes=base64.b16decode(base64_bytes)
            decoded_bytes=base64.b32decode(decoded_bytes)
            decoded_bytes=base64.b85decode(decoded_bytes)
            decoded_bytes=base64.a85decode(decoded_bytes)
            decoded_bytes=base64.b64decode(decoded_bytes)
            decoded_bytes=base64.b16decode(decoded_bytes)
    elif security_level == "4":
        for i in range(int(security_level)*7):
            decoded_bytes=base64.b64decode(base64_bytes)
            decoded_bytes=base64.a85decode(decoded_bytes)
            decoded_bytes=base64.b32decode(decoded_bytes)
            decoded_bytes=base64.b16decode(decoded_bytes)
            decoded_bytes=base64.b64decode(decoded_bytes)
            decoded_bytes=base64.b85decode(decoded_bytes)
    elif security_level == "5":
        for i in range(int(security_level)*10):
            decoded_bytes=base64.a85decode(base64_bytes)
            decoded_bytes=base64.b16decode(decoded_bytes)
            decoded_bytes=base64.a85decode(decoded_bytes)
            decoded_bytes=base64.b85decode(decoded_bytes)
            decoded_bytes=base64.b16decode(decoded_bytes)
            decoded_bytes=base64.b64decode(decoded_bytes)
            decoded_bytes=base64.b32decode(decoded_bytes)
            
    # Convert the original bytes back to a string
    if other_encoding == None:
        decoded_string = decoded_bytes.decode("cp1252")
    else:
        decoded_string = decoded_bytes.decode(other_encoding)

    return decoded_string

#find a specific file
def find_File(fileName, fileEncoding):
    try:
        with open(fileName, "r", encoding=fileEncoding) as f:
            fileContents = f.read()
            return fileContents
    except FileNotFoundError:
        print()
        print("Please enter file name properly.")
        main_Menu()
    except LookupError:
        print()
        print("Please enter file encoding properly.")
        main_Menu()

# checking level of security then encoding or decoding
def security_check(input_text, security, encodeOrDecode, writeToFile, fileName, fileEncoding):
    num = 1
    # Check to see what security level is
    for _ in range(5):

        if security != str(num):
            num += 1

            if num == 6:
                print("Please re-enter choice with a valid choice.")
                print()
                main_Menu()

        else:
            if encodeOrDecode == "encode":
                # Encode
                encoded_text = encode_to_base64(input_text, security, fileEncoding)
                print(f"Encoded message: {encoded_text}")

                if writeToFile == "y":
                    with open(fileName, "w", encoding=fileEncoding) as f:
                        f.write(encoded_text)
                        f.close()
                        print("Written to file.")

                else:
                    pyperclip.copy(encoded_text)
                    print("Message has been copied to your clipboard.")

                print()
                main_Menu()

            elif encodeOrDecode == "decode":
                # Decode
                    decoded_text = decode(input_text, security, fileEncoding)
                    print(f"Decoded message: {decoded_text}")

                    if writeToFile == "y":
                        with open(fileName, "w", encoding=fileEncoding) as f:
                            f.write(decoded_text)
                            f.close()
                            print("Written to file.")

                    print()
                    main_Menu()

# For invalid input     
def notAnAnswer():
    print("Please re-enter choice with a valid choice.")
    print()
    main_Menu()

# Added function to be able to write the encoded or decoded text into the file supplied (this is optimizing for less code)
def writeToFileYN(input_text, security, fileName, encodeOrDecode, fileEncoding):
    # input_text is the text of the file that has been read using find_File()
    write_to_file = input("Would you like to write the text to the file? NOTE: This will replace all text in the file. (y/n): ")

    if write_to_file.lower() == "y":
        security_check(input_text, security, encodeOrDecode, "y", fileName, fileEncoding)

    elif write_to_file.lower() == "n":
        write_to_new_file = input("Would you like to write the text to a different file? NOTE: This will replace the file's previous content. (y/n): ")
        if write_to_new_file.lower() == "y":
            file_name = input("Enter file name (please include any parent folders (aka, texts/boogerman.txt) ): ")
            file_encoding = input("Enter file encoding (leave blank if none): ")
            if file_encoding == "":
                file_encoding = None
            print()
            security_check(input_text, security, encodeOrDecode, "y",  file_name, fileEncoding)
        print()
        security_check(input_text, security, encodeOrDecode, "n", "", fileEncoding)

    else:
        notAnAnswer()

# Example usage
if __name__ == "__main__":
    def main_Menu():
        decode_or_encode = input("Input 1 for encoding a message, 2 for decoding a message, 3 to upload a text file to encode or decode, or 4 to exit: ")
        
        if decode_or_encode == "1":
            input_text = input("Input string to encode: ")
            security = input("Input level of security, 1 is minimal, 5 is maximal: ")
            print()
            security_check(input_text, security, "encode")

        elif decode_or_encode == "2":
            encoded_text = input("Input encoded message: ")
            security = input("Input level of security used: ")
            print()
            security_check(encoded_text, security, "decode")

        elif decode_or_encode == "3":
            choice = input("Input 1 to encode the file, 2 or decode the file or 3 to go back: ")

            if choice == "1":
                input_file = input("Enter file name (please include any parent folders (aka, texts/boogerman.txt) ): ")
                file_encoding = input("Enter file encoding (leave blank if none): ")
                if file_encoding == "":
                    file_encoding = None
                input_text = find_File(input_file, file_encoding)
                security = input("Input level of security, 1 is minimal, 5 is maximal: ")
                print()
                writeToFileYN(input_text, security, input_file, "encode", file_encoding)

            elif choice == "2":
                input_file = input("Enter file name (please include any parent folders (aka, texts/boogerman.txt) ): ")
                file_encoding = input("Enter file encoding (leave blank if none): ")
                if file_encoding == "":
                    file_encoding = None
                encoded_text = find_File(input_file, file_encoding)
                security = input("Input level of security used: ")
                print()
                writeToFileYN(encoded_text, security, input_file, "decode", file_encoding)

            elif choice == "3":
                main_Menu()

            else:
                notAnAnswer()

        elif decode_or_encode == "4":
            exit()

        else:
            notAnAnswer()
        
    main_Menu()
