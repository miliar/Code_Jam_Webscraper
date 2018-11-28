#include <iostream>
#include <fstream>
#include <vector>
using namespace std;

//Basic Data
int testcase;
char num[20]; //테스트 데이터
int sizeOfNum;


//파일 입출력
ifstream fin;
ofstream ofn;


bool CheckTidy(){
	int a, b; // a는 앞에수, b는 뒤의수

	//cout << "sizeOfNum = " << sizeOfNum << endl;

	for (int i = sizeOfNum - 1; i > 0; i--) {
		a = num[i - 1] - '0';
		b = num[i] - '0';

		//cout << "a = " << a << ", b = " << b << endl;

		if (a > b) {
			a -= 1;
			num[i - 1] = a + '0';

			//cout << "num[" << i - 1 << "] = " << num[i-1] << endl;

			for (int j = i; j < sizeOfNum; j++) {
				num[j] = '9';
			}
			//cout << "\n";

			return false;
		}
	}
	return true;
}

//sidx : 기준인덱스
void Solution(int caseNum) {
	sizeOfNum = strlen(num); //문자열 길이 받음
	while (true) {
		if (CheckTidy()) {
			ofn << "Case #" << caseNum << ": ";
			int stridx = 0;

			while (stridx < sizeOfNum) {
				if (num[stridx] != '0') {
					ofn << num[stridx];
				}
				stridx++;
			}
			ofn << "\n";

			break;
		}
	}
}



void Init() {
	fin.open("B-large.in");
	ofn.open("ans.txt");
	fin >> testcase;

	for (int i = 1; i <= testcase; i++) {
		fin >> num;
		cout << "테스트 데이터 : " << num << endl;

		Solution(i);
		cout << "답 : " << num << endl;
	}

	if (fin.is_open()) {
		fin.close();
	}
	if (ofn.is_open()) {
		ofn.close();
	}
}

int main() {
	Init();

	return 0;
}