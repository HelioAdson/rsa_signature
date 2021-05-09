from rsa_signature import Rsa_signature
import os

if __name__ == "__main__":
	rs = Rsa_signature()
	while True:
		os.system('cls' if os.name == 'nt' else 'clear')
		dig = int(input("-------------- Options --------------\n1 - Generate RSA Keys \n2 - Show Public Key \n3 - Show Private Key \n4 - Signature Verifier \n5 - Sign File\n6 - Show Signature\n0 - Exit\n-- > "))
		print('\n')
		if dig == 1:
			rs.generate_rsa_key()
		elif dig == 2:
			print(rs.public_key())
		elif dig == 3:
			print(rs.private_key())
		elif dig == 4:
			doc_path = input("Enter the name of the file to be scanned: ")
			rs.verify_rsa_signature(doc_path)
		elif dig == 5:
			doc_path = input("Enter the file name: ")
			rs.sign(doc_path)
		elif dig == 6:
			print(rs.signature().hex())
		else:
			break

		input("\nPress enter to continue...")