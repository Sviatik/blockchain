import json
import os
import hashlib as hl

bc_dir = os.curdir + "/bc/"

def get_hash(filename):
	file = open(bc_dir + filename, "rb").read()
	return hl.md5(file).hexdigest()


def get_files():
	files = os.listdir(bc_dir)
	return sorted([int(i) for i in files])



def check_integrity():
	results = []
	files = get_files()
	for i in files[1:]:
		f = open(bc_dir + str(i), "r")
		h = json.load(f)['hash']

		prev_file = str(i - 1)

		actual_hash = get_hash(prev_file)

		if h == actual_hash:
			res = "Ok"
		else:
			res = "Coruppted"

		results.append({"block": i, "result": res})
	return results

def write_block(name, amount, to_whome, prev_hash=''):
	files = get_files()

	prev_file = files[-1]
	filename = str(prev_file + 1)


	prev_hash = get_hash(str(prev_file))


	data = {"name": name,
			"amount": amount,
			"to_whome": to_whome,
			"hash": prev_hash}

	with open(bc_dir + filename, mode="w") as file:
		json.dump(data, file, ensure_ascii=False, indent=4)







def main():
#	write_block(name="Ivan", amount=32, to_whome="Igor")
	print(check_integrity())
	print("INFO: Seccessfully")



if __name__ == '__main__':
	main()