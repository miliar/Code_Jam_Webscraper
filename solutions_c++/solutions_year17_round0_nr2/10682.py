// ConsoleApplication1.cpp : 콘솔 응용 프로그램에 대한 진입점을 정의합니다.
//



#include "stdafx.h"
#include "ConsoleApplication1.h"

using namespace std;

int getTidyNumber(int);
bool isTidy(int);

int main()
{
	int inputNumber;
	int cases;
	int idx = 1;
	int result = 0;
	cin >> cases;
	while (cases-- > 0) {
		cin >> inputNumber;
		result = getTidyNumber(inputNumber);
		cout << "case #" << idx << ": " << result << endl;
		idx++;
	}


	
    return 0;
}

int getTidyNumber(int inputNumber) {
	int result = 0;

	for (int i = inputNumber;i >= 1;i--) {
		if (isTidy(i) == true) {
			result = i;
			break;
		}
	}
	return result;
}

bool isTidy(int i) {
	//separate number array
	char testNumber[10];
	memset(testNumber, 0, 10);
	itoa(i, testNumber, 10);
	//check non decresaing rule

	if (strlen(testNumber) == 1)
		return true;

	if (strlen(testNumber) == 2) {
		if (testNumber[0] > testNumber[1])
			return false;
	}

	if (strlen(testNumber) == 3) {
		if (testNumber[0] > testNumber[1])
			return false;
		if (testNumber[1] > testNumber[2])
			return false;
	}

	if (strlen(testNumber) == 4) {
		if (testNumber[0] > testNumber[1])
			return false;
		if (testNumber[1] > testNumber[2])
			return false;
		if (testNumber[2] > testNumber[3])
			return false;
	}
	return true;
}

