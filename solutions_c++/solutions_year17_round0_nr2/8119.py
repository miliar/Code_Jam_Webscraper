#include <iostream>
#include <fstream>
using namespace std;

int testCases;

/*
string toString(int num) {
	string res = "";
	while(num > 0) {
		char number = ((int)'0' + num%10);
		//cout<<number;
		res = res + number;
		num/=10;
	}
	//cout<<res<<endl;
	string temp = "";
	for(int i = res.length() - 1; i >=0 ; i--) {
		temp = temp + res[i];
	}
	res = temp;
	return res;
}
*/

void make9(string& num, int pos) {
	for(int i = pos; i < num.length(); i++) {
		num[i] = '9';
	}
}

string trail0(string num) {
	int i;
	for(i = 0; i < num.length(); i++) {
		if(num[i] != '0') {
			break;
		}
	}
	string ret = "";
	for(int j = i; j < num.length(); j++)
		ret = ret + num[j];
	return ret;
}

string lastTidyNumber(string num) {
	for(int i = num.length() - 1; i >= 1; i--) {
		if(num[i-1] > num[i]) {
			char digit = (int)num[i-1] - 1;
			num[i-1] = digit;
			make9(num, i);
		}
	}
	return trail0(num);
}

int main() {
	ifstream in ("b.in");
	ofstream out ("b.out");	
	
	/*
	string num = "41568431";
	make9(num, 2);
	cout<<num;
	*/
	
	in>>testCases;
	
	int testNumber = 0;
	
	while(testNumber++ < testCases) {
		string number;
		in>>number;
		string answer = lastTidyNumber(number);
		out<<"Case #"<<testNumber<<": "<<answer<<endl;
	}
	
	
	
	
	//cout<</*((int)('0')+1) - '0';//*/toString(5431);
}
