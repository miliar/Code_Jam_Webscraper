#include <iostream>
#include <fstream>
#include <sstream>
using namespace std;


bool isTidy(int num) {
	ostringstream convertedNum;
	convertedNum<<num;
	int convertedNumLength = convertedNum.str().length();
	if (convertedNumLength == 1) {
		return true;
	}
	int firstDigit = num%10;
	int nextNum = (num - firstDigit)/10;
	int secondDigit = nextNum%10;
	if (firstDigit < secondDigit) {
		return false;
	}
	else return isTidy(nextNum);
}

int main () {

	ifstream inputFile;
	ofstream outputFile;

	inputFile.open("B-small-attempt0.in");
	outputFile.open("B-out.txt");

	int N;
	inputFile>> N;
	int caseNum;

	for (int i=1; i<=N; i++) {
		inputFile>>caseNum;
		for (int j=caseNum; j>=0; j--) {
			if (isTidy(j)) {
				outputFile<<"Case #"<<i<<": "<<j<<endl;
				break;
			}
		}
	}
	inputFile.close();
	outputFile.close();

}

