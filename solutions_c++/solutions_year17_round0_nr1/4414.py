#include<iostream>
#include<fstream>
#include<string>
using namespace std;
char rese(char x) {
	if (x == '-') return '+';
	if (x == '+') return '-';
}
int main() {
	int num,count,sum=0,no=string::npos;
	string x;
	ifstream inFile;
	ofstream outFile;
	inFile.open("A-large.in");
	outFile.open("a.out");
	inFile >> num;
	for (int j = 1;j<= num;++j) {
		inFile >> x>>count;
		int si = x.size();sum = 0;
		outFile << "Case #" << j<< ": ";
		for (int i = 0;i <=si - count;++i) {
			if (x[i] == '-')
			{for (int j = 0;j <= count-1;++j) { x[i+j]=rese(x[i + j]); }
			sum += 1;}
		}
			if (x.find('-')!=no) outFile << "IMPOSSIBLE"<<endl;
			else outFile << sum << endl;
		}
	}