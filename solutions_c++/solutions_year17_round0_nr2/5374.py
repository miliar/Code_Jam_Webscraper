#include "stdafx.h"
#include <iostream>
#include <string>
#include <sstream>
#include <vector>
using namespace std;
int halt = 0;
void getTestCases(int& inT, vector<string> & inS) {
	int tc = 0;
	string input = "";
	getline(cin, input);
	stringstream myStream(input);
	myStream >> inT;
	inS.resize(inT);

	int tempNum = 0;
	while (tc < inT) {
		getline(cin, input);
		inS[tc] = input;
		tc++;
	}
}
bool isSmaller(char fst, char scnd) {
	if (fst <= scnd)
		return true;
	return false;
}
int getIntValue(char a) {
	return a - '0';
}
char getSmallerEle(char a) {
	int ip = getIntValue(a);
	if (ip >= 2) {
		ip--;
		return ip + '0';
	}
	return 9 + '0';
}
int ChangeforLeftSide(string &input,int temp,char  tempChar,char newTempChar ) {
	while (temp >= 0) {
		if (input[temp] == tempChar) {
			//input[temp] = newTempChar;
			temp--;
		}
		else
			break;
		
	}
	return temp+1;
}
string getNumberForTidy(string input)
{
	string str;
	int counter = 0,size = input.size();
	
	str.resize(input.size());
	str[0] = input[0];
	int temp = 0;

	while (temp+1 < size) {
		if (isSmaller(input[temp],input[temp+1])) {
			str[temp] = input[temp];
			if (temp + 1 == size-1)
				str[temp+1] = input[temp+1];
		}else {
			char tempChar = input[temp];
			int lessDigit = 0;
			if (tempChar == '1')
				lessDigit = 1;
			char newTempChar = getSmallerEle(tempChar);
			int loc = ChangeforLeftSide(str,temp-1,tempChar,newTempChar);
			str[loc] = newTempChar;
			temp = loc +1;
			if (lessDigit)
				size--;
			while (temp < size) {
				str[temp] = '9';
				temp++;
			}
			break;
		}
		temp++;
	}
	return str;
}
int main() {
	// your code goes here
	int tc = 0;
	vector<string> S;
	vector<string> op;
	getTestCases(tc, S);
	int temp = 0;
	op.resize(tc);
	while (temp < tc) {
		op[temp] = getNumberForTidy(S[temp]);
		temp++;
	}
	temp = 0;
	while (temp < tc) {
		cout << "Case #" << temp+1 << ": "  << op[temp] << endl;
		//cout << "string :" << S[temp] << " flip:" << K[temp] << endl;
		temp++;
	}
	getchar();
	return 0;

}