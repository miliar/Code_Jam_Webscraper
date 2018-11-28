#include <iostream>
#include <fstream>
#include <vector>
using namespace std;

//Basic Data
int testcase;
char num[20]; //�׽�Ʈ ������
int sizeOfNum;


//���� �����
ifstream fin;
ofstream ofn;


bool CheckTidy(){
	int a, b; // a�� �տ���, b�� ���Ǽ�

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

//sidx : �����ε���
void Solution(int caseNum) {
	sizeOfNum = strlen(num); //���ڿ� ���� ����
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
		cout << "�׽�Ʈ ������ : " << num << endl;

		Solution(i);
		cout << "�� : " << num << endl;
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