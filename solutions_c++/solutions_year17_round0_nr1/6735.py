/*
 *
 * */

#include <iostream>
#include <string>
#include <cstring>
#include <sstream>
#include <fstream>
#include <cstdio>
using namespace std;

int str_to_int(string );
string int_to_str(int );
void flip(char *);
string findNeg(char [], int );


//int t = 1;	//test case number, need to read from file later.
//int k = 3;	//test value, need to read from file later.

void parseFile() {

}

int str_to_int(string str) {
	int rst;
	istringstream convert(str);
	if(!(convert >> rst)) {
		rst = 0;
	}
	return rst;
}

string int_to_str(int a) {
	ostringstream convert;
	convert << a;

	return convert.str();
}

void flip(char *ch) {
	if((*ch) == '+') {
		(*ch) = '-';
	}
	else if((*ch) == '-') {
		(*ch) = '+';
	}	
}

string findNeg(char str[], int k) {
	int attempt = 0;
	int pos = 0;
	char *pch = strchr(str, '-');	//find the first '-'
	
	if(pch == NULL) {	//all '+', do not need to flip.
	//	cout << "'-' not found at the first time" << endl;
		return "0";
	}
	else {
		while(pch != NULL) {	//can find a '-' in char array.
			pos = pch - str;	//set position  
	//		cout << "found at: " << pos << endl;
			if (pos < (strlen(str) - k + 1)) {
				attempt += 1;
	//			cout << attempt << endl;
				for(int i = 0; i < k; i++) {
					flip(&str[pos + i]);	//flip consecutive K pancakes
				}
	//			cout << str << endl;
				pch = strchr(pch + 1, '-');
			}
			else {
				return "IMPOSSIBLE";
			}
		}
	//	cout << "attempt: " << attempt << endl;
		return int_to_str(attempt);
	}
}

int main(int argc, char *argv[]) {
	
	string line;
	int testcase_num;
	char s[1024];
	int pan_size;
	
	int count = 0;

//	char str[] = "---+-++-";
	
	ifstream myfile("A-large.in");
	if (myfile.is_open()) {
		getline(myfile, line);	//get the testcase_num in the first line
		testcase_num = str_to_int(line);
		while ((!myfile.eof()) && (getline (myfile, line))) {	//get the rest
		//	cout << line << endl;
			count += 1;
			istringstream instr(line);
			instr >> s >> pan_size;
			cout << "Case #" << count << ": " << findNeg(s, pan_size) << endl;
		}
	}
	
	return 0;
}
