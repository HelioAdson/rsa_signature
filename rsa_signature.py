import rsa
# import pyasn1.codec.der.encoder
# import pyasn1.type.univ

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
		print("Generating RSA Keys...")
		(public_key, private_key) =  rsa.newkeys(2048)

		# e = 0x010001
		# p = 0xCAA8F25E146F81FB0C31FB9FC98C5A4EDB25829EAA97B1B07C0761FE4E185D9EB886A8EC478A4BCCBF43A2AB3300A972074B1BACF1BEB731C1C096F9573A02D9
		# q = 0xB0A1DD2EAB28ED07BE20658BF6D0FAA0CF395352746AB256A251F95AAA558E0C575866719821815A64F4DE0BE62E89D2F5E99805AFB1596C2755CCB96C4D9C63

		# pub, prv = keygen(p, q, e)
		# e, n = pub
		# d, _ = prv
		# dP = rsa.modinv(e, p -1)
		# dQ = rsa.mdinv(e, q -1)

		# qInv = rsa.modinv(q, p)

		# template = '-----BEGIN RSA PRIVATE KEY-----\n{}-----END RSA PRIVATE KEY-----\n'

		# seq = pyans1.type,univ.Sequence()

    # for x in [0, n, e, d, p, q, dP, dQ, qInv]:
		# 	seq.setComponentByPosition(len(seq), pyasn1.type.univ.Integer(x))
    # der = pyasn1.codec.der.encoder.encode(seq)
    # prv_pem =  template.format(base64.encodestring(der).decode('ascii'))

		try:
			with open("public_key.txt", "wb") as outfile:
				outfile.write(pub_pem.save_pkcs1('PEM'))
		except IOError:
			print('Error! Try again')

		try:
			with open("private_key.txt", "wb") as outfile2:
				outfile2.write(prv_pem.save_pkcs1('PEM'))
			print("Created Rsa Keys!")
		except IOError:
			print('Error! Try again')

	def sign(self, file):
		private_key_load = rsa.PrivateKey.load_pkcs1(self.__read_file('private_key.txt'))

		file = self.__read_file(file)

		sign_hash = rsa.compute_hash(file, 'SHA3-256')

		signature = rsa.sign(file, private_key_load, 'SHA3-256')

		try:
			with open("signature.txt", "wb") as outfile2:
				outfile2.write(signature)
			print("File has been signed!")
		except IOError:
			print('Error! Try again')

	def verify_rsa_signature(self, file):
		public_key_load = rsa.PublicKey.load_pkcs1(self.__read_file('public_key.txt'))

		file = self.__read_file(file)

		signature = self.__read_file('signature.txt')

		try:
			rsa.verify(file, signature, public_key_load)
			print('\n Valid signature! Document has not been modified.\n')
		except:
			print('\n Document has been modified or does not have a signature.\n')


	# def keygen(p: int, q: int, e: int = None) -> Tuple[Key, Key]:
  #   '''Create public key (exponenet e, modulus n) and private key
  #   (exponent d, modulus n)'''
  #   assert is_prime(p) and is_prime(q)
  #   assert p != q
  #   n = p * q
  #   phi = (p - 1) * (q - 1)
  #   if e != None:
  #       assert euclid(phi, e) == 1
  #   else:
  #       while True:
  #           e = random.randrange(1, phi)
  #           if euclid(e, phi) == 1:
  #               break
  #   d = modinv(e, phi)
  #   return ((e, n), (d, n))