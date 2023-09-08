#CREATED BY CYCO EXPLOIT

import argparse

def shift_cipher(text, shift):
    N = 0x10FFFF
    return ''.join(chr((ord(ch) + shift) % N) for ch in text)

def decrypt_shift_cipher(text, shift):
    N = 0x10FFFF
    return ''.join(chr((ord(ch) - shift) % N) for ch in text)

def main():
    parser = argparse.ArgumentParser(description="Contoh penggunaan argumen baris perintah")

    parser.add_argument("-t", "--text", type=str, required=True, help="Teks yang akan diolah")

    parser.add_argument("-b", "--brute", action="store_true", help="Brute force dekripsi")

    parser.add_argument("-r", "--range", type=int, help="Pergeseran untuk enkripsi/dekripsi")

    parser.add_argument("-r1", "--range1", type=int, help="range 1")

    parser.add_argument("-r2", "--range2", type=int, help="range 2")

    parser.add_argument("-f", "--final", type=str, default="", help="text yang dicari")

    parser.add_argument("-e", "--encode", action="store_true", help="Enkripsi teks")

    parser.add_argument("-d", "--decode", action="store_true", help="Dekripsi teks")

    args = parser.parse_args()

    if args.brute:
        if args.encode:
            print("Argumen --encode tidak dapat digunakan bersama dengan --brute.")
            return

        if args.range1 is None or args.range2 is None:
            print("Argumen --brute memerlukan argumen --range1 dan --range2.")
            return
        
        search = args.final[:3]
        for i in range(args.range1, args.range2 + 1):
            value = decrypt_shift_cipher(args.text, i)
            tmp = value[:3]
            if search == tmp:
                print(f"\x1b[6;30;42m{i}: {value}\x1b[0m")
            else:
                print(f"{i}: {value}")
                
    else:        
        if args.encode:
            if args.range is None:
                print("Argumen --encode memerlukan argumen --range.")
                return
            value = shift_cipher(args.text, args.range)
        else:
            if args.range is None:
                print("Argumen --decode memerlukan argumen --range.")
                return
            value = decrypt_shift_cipher(args.text, args.range)
        print(value)

if __name__ == "__main__":
    main()
