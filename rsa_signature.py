import rsa

class Rsa_signature:
	def __read_file(self, file):
		f = open(file, 'rb')
		opened_file = f.read()
		f.close()
		return opened_file

	def public_key(self):
		return self.__read_file('public_key.txt')

	def private_key(self):
		return self.__read_file('private_key.txt')

	def signature(self):
		return self.__read_file('signature.txt')

	def generate_rsa_key(self):
		(public_key, private_key) =  rsa.newkeys(2048)
		print("Criando chaves rsa...")
		try:
			with open("public_key.txt", "wb") as outfile:
				outfile.write(public_key.save_pkcs1('PEM'))
		except IOError:
			print('Erro! Tente Novamente')

		try:
			with open("private_key.txt", "wb") as outfile2:
				outfile2.write(private_key.save_pkcs1('PEM'))
			print("Chaves Rsa Criadas!!")
		except IOError:
			print('Erro! Tente Novamente')

	def sign(self, file):
		private_key_load = rsa.PrivateKey.load_pkcs1(self.__read_file('private_key.txt'))

		file = self.__read_file(file)

		sign_hash = rsa.compute_hash(file, 'SHA3-256')

		signature = rsa.sign(file, private_key_load, 'SHA3-256')

		try:
			with open("signature.txt", "wb") as outfile2:
				outfile2.write(signature)
		except IOError:
			print('Erro! Tente Novamente')

	def verify_signature(self, file):
		public_key_load = rsa.PublicKey.load_pkcs1(self.__read_file('public_key.txt'))

		file = self.__read_file(file)

		signature = self.__read_file('signature.txt')

		try:
			rsa.verify(file, signature, public_key_load)
			print('\n Assinatura válida! Documento não foi modificado.\n')
		except:
			print('\n Documento foi modificado ou não possui assinatura digital.\n')