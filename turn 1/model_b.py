import base64
import zerotier_one as zt

# Dummy data for demonstration purposes
dummy_data = b"This is some confidential data to be shared securely!"
dummy_key = b"32_byte_long_random_encryption_key_for_demo_purposes_only_do_not_use_this_in_production"

def encrypt_data(data, key):
    from cryptography.fernet import Fernet
    cipher_suite = Fernet(key)
    encrypted_data = cipher_suite.encrypt(data)
    return encrypted_data

def decrypt_data(encrypted_data, key):
    from cryptography.fernet import Fernet
    cipher_suite = Fernet(key)
    decrypted_data = cipher_suite.decrypt(encrypted_data)
    return decrypted_data

def main():
    # Replace 'YOUR_NETWORK_ID' and 'YOUR_PRIVATE_KEY' with your actual Zerotier network credentials
    network_id = "YOUR_NETWORK_ID"
    private_key = "YOUR_PRIVATE_KEY"

    try:
        # Initialize Zerotier client
        client = zt.Client()
        client.set_auth(network_id, private_key)

        # Connect to the Zerotier network
        network = client.get_network(network_id)
        network.join()

        # Encrypt the data using dummy encryption key
        encrypted_data = encrypt_data(dummy_data, dummy_key)
        print("Encrypted data:", base64.b64encode(encrypted_data).decode())

        # Share the encrypted data securely (in this case, we'll just print it out, but you could use a secure communication channel)
        print("Shared Encrypted Data:", base64.b64encode(encrypted_data).decode())

        # Receiver side (decryption):
        # (In a real-world scenario, the receiver would have the encrypted data and the dummy key)
        received_encrypted_data = base64.b64decode(b"SGVsbG8gV29ybGQh")  # Replace with the actual received encrypted data
        decrypted_data = decrypt_data(received_encrypted_data, dummy_key)
        print("Decrypted Data:", decrypted_data.decode())

    finally:
        # Leave the network
        network.leave()
        client.close()

if __name__ == "__main__":
    main()
