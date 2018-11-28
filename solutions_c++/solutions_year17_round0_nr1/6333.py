#include <string>
#include <vector>
#include <algorithm>
#include <iostream>
#include <fstream>
using namespace std;


void removeHeadTailPlus(string& str) 
{
	int i = 0;
	while (str[i] == '+') {
		str.erase(0, 1);
	}
	int j = str.size() - 1;
	while (str[j] == '+'){
		str.erase(j, 1);
		j = str.size() - 1;
	}
}

void change(string& str, int K) 
{
	for (int i = 0; i < K; i++) {
		if (str[i] == '-') {
			str[i] = '+';
		}
		else {
			str[i] = '-';
		}
	}
}

bool checkString(string& str) {
	for (int i = 0; i < str.size(); ++i) {
		if (str[i] == '-')
			return false;
	}
	return true;
}

int main()
{
	fstream inStream, outStream;
	inStream.open("input.txt", ios::in);
	outStream.open("output.txt", ios::out);
	int T;
//	inStream >> T;
//	inStream >> T;
//	inStream >> T;
	inStream >> T;
	int dem = 1;
	while (T)
	{
		string str;
		inStream >> str;
		int K; 
		inStream >> K;
		int count = 0;
		bool flag = true;
		while (str.size() >= K) {
			if (checkString(str))
				break;
			removeHeadTailPlus(str);
			if (str.size() < K && !checkString(str)) {
				flag = false;
				outStream << "Case #"<<dem << ": "  << "IMPOSSIBLE" << endl;
				break;
			}
			change(str, K);
			++count;
		}
		if (flag) outStream << "Case #" << dem << ": " << count << endl;
		--T;
		++dem;
	}
	inStream.close();
	outStream.close();	
}