import re
import sys

from datetime import datetime

pattern = re.compile(r'how long has it been since (?P<date>\d{4}\-\d{2}\-\d{2})\?')

def main():
	match = pattern.fullmatch(' '.join(sys.argv[1:]))
	
	if match is None:
		print('invalid call')
	
	try:
		start_date = datetime.strptime(match.group('date'), '%Y-%m-%d')
		print('{} days'.format((datetime.today() - start_date).days))
	except ValueError:
		print('invalid start date')


if __name__ == '__main__':
	main() 
