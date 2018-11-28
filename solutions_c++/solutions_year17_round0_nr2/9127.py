#include <fstream>
#include <iostream>
#include <string>
#include <stdlib.h>
using namespace std;

int main()
{
	
	ifstream infile("input.txt");

	if(!infile) {
		cout << "Couldn't open input file.\n";
		return 1;
	}

	ofstream outfile;
	outfile.open("output.txt");

	string str;
	getline(infile, str);
	cout << str << " test cases detected" << endl;
	int count = 1;

	while(getline(infile, str)) {


		cout << "processing test case #" << count << ": " << str << endl;

		int index = 0;
		int strlen = str.length();
		//find first instance where digit is greater than the next digit
		while(index < strlen-1 && (int)str[index]-48 <= (int)str[index+1]-48 ) {
			index += 1;
		}
		//all nondescending, return input
		if(index == str.length()-1) {
			outfile << "Case #" << count << ": " << str << endl;
		}
		else { //reduce current digit by 1
			int digit_val = (int)str[index]-48;
			digit_val -= 1;
			char new_digit = '0' + digit_val;
			str[index] = new_digit;

			for(int i = index+1; i < strlen; i++) {
				str[i] = '9';
			}

			while(index != 0 && (int)str[index-1]-48 > (int)str[index]-48) {

				str[index] = '9';
				index -= 1;
				digit_val = (int)str[index]-48;
				digit_val -= 1;
				new_digit = '0' + digit_val;
				str[index] = new_digit;

			}

			str.erase(0, min(str.find_first_not_of('0'), str.size()-1));
			outfile << "Case #" << count << ": " << str << endl;

		}

		count++;
	}

}