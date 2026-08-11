How to use it on Linux
Save the code above into a file named keeloq_gen.py.

Ensure you have a directory named KEELOQ in the same location as your Python script, and that your key.txt file is inside it.

Open your terminal and make the script executable by running:
chmod +x keeloq_gen.py

Execute the script:
./keeloq_gen.py

-----------------------------------------------------------

Python
#!/usr/bin/env python3
import os

def generate_keeloq_files():
    print("Keeloq Flipper Zero Generator")
    print("---")

    input_dir = "KEELOQ"
    input_file = os.path.join(input_dir, "key.txt")

    # Check if the input file exists
    if not os.path.exists(input_file):
        print(f"{input_file} not found")
        return

    # Read all lines from the key.txt file
    with open(input_file, 'r') as f:
        # Strip whitespace/newlines to ensure accurate length checks
        lines = [line.strip() for line in f if line.strip()]

    total_keys = len(lines)
    print(f"total keys: {total_keys}")

    write_count = 1
    read_count = 1

    for key in lines:
        # Skip keys that aren't exactly 8 characters long
        if len(key) != 8:
            print("bad key - skipping")
            read_count += 1
            continue

        # Split the 8-character key into four 2-character chunks
        k1, k2, k3, k4 = key[0:2], key[2:4], key[4:6], key[6:8]

        # Format write_count to be 5 digits (e.g., 00001)
        file_name = f"Key{write_count:05}.sub"
        file_path = os.path.join(input_dir, file_name)
        
        key_string = f"{k1} {k2} {k3} {k4} C2 44 00 05"

        # Write the .sub file
        with open(file_path, 'w') as out_f:
            out_f.write("Filetype: Flipper SubGhz Key File\n")
            out_f.write("Version: 1\n")
            out_f.write("Frequency: 433920000\n")
            out_f.write("Preset: FuriHalSubGhzPresetOok270Async\n")
            out_f.write("Latitute: nan\n")
            out_f.write("Longitude: nan\n")
            out_f.write("Protocol: KeeLoq\n")
            out_f.write("Bit: 64\n")
            out_f.write(f"Key: {key_string}\n")
            out_f.write("Manufacture: Unknown\n")

        # Echo the progress to the console
        print(f"KEY {read_count} - {file_path} Key: {key_string}")

        write_count += 1
        read_count += 1

    print("finished")

if __name__ == "__main__":
    generate_keeloq_files()

