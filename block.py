import json





def write_block(name, amount, to_whome, prev_hash=''):
	data = {"name": name,
			"amount": amount,
			"to_whome": to_whome,
			"prev_hash": prev_hash}

	with open("test", mode="w") as file:
		json.dump(data, file, ensure_ascii=False, indent=4)







def main():
	write_block(name="Ivan", amount=32, to_whome="Igor")



if __name__ == '__main__':
	main()