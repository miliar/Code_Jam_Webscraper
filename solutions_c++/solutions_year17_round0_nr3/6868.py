#include <iostream>
#include <fstream>
#include <vector>
using namespace std;

//ũ�� n�� �迭���� �߰��ε���(Ȧ���̸� Ls=Rs, ¦���̸� Ls�� Rs���� �������� �ε���)
//�� �������� ������ Max�� Min���� ���� Rs,Ls�̰�
//������ Ls, Rs�̴�.
//�� �ε����� Ls/Rs�� �츮�� �ͺ��� Max,Min������ LS Rs�� �˼��ֵ�.



//Stall ����ü
typedef struct _stall {
	int Ls;
	bool check;
	int Rs;
}Stall;


//Basic Data
int testcase(0);
Stall arr[1000];
int minArray[1000] = { 0, };
int maxArray[1000] = { 0, };
vector<int> MinMaxVec; // 1�ܰ迡�� MinMax�� ���� �ε����� ����
int n(0), k(0); // n : ���� ��, k : ����� ��
int MinMax(0); //1�ܰ迡���� �ּҰ��� �߿� �ִ밪�� ����ϸ鼭 ���ؼ� ������ �ְ� ���� ���� �ε����� ã�Ƴ�
int ansIdx(0); //���� ����� �� �ε��� ���� ���� ����



//���� �����
ifstream fin;
ofstream ofn;


//Stall �迭�� Ls/Rs�� ���
void PrintStallArray() {
	for (int i = 0; i < n; i++) {
		cout << i << " stall : Ls = ";

		if (arr[i].check == true) {
			cout << "���õ�" << endl;
		}
		else {
			cout<< arr[i].Ls << ", Rs = " << arr[i].Rs << endl;
		}
			
	}
}

void FindMaxMin(int idx) {
	if (arr[idx].Ls >= arr[idx].Rs) {
		minArray[idx] = arr[idx].Rs;
		maxArray[idx] = arr[idx].Ls;
	}
	else {
		minArray[idx] = arr[idx].Ls;
		maxArray[idx] = arr[idx].Rs;
	}

	if (minArray[idx] > MinMax)
		MinMax = minArray[idx];
}


//sidx : �����ε���
void Solution() {

	for (int m = 0; m < k; m++) {
		//cout << "MinMax(1�ܰ��� �ִ밪) = " << MinMax << endl;

		//cout << "1�ܰ迡�� ä�õ� �ε����� -----" << endl;
		//1�ܰ�
		for (int i = 0; i < n; i++) {
			if (minArray[i] == MinMax && arr[i].check==false) {
				//cout << i << "�ε���" << endl;
				MinMaxVec.push_back(i);
			}
		}
		MinMax = 0;

		//2�ܰ�
		int maxIdx(0), maxValue(0);
		//cout <<"1�ܰ� ���õ� �ε��� �� ="<< MinMaxVec.size() << endl;
		for (int i = 0; i < MinMaxVec.size(); i++) {
			int idx = MinMaxVec[i];
			if (maxArray[idx] > maxValue) {
				maxValue = maxArray[idx];
				maxIdx = idx;
			}
		}

		if (maxValue == 0) {
			for (int i = 0; i < MinMaxVec.size(); i++) {
				int idx = MinMaxVec[i];
				if (arr[idx].check == false)
					maxIdx = idx;
			}
		}
		
		//cout<< "MaxValue(2�ܰ��� �ִ밪) = " << maxValue << endl;
		//cout << "maxIdx(����� ���� ������ ��ġ) = " << maxIdx << endl;
		arr[maxIdx].check = true;
		if (m == k - 1) {
			ansIdx = maxIdx;
		}

		//maxIdx�� �������� �������� ������Ʈ
		int Lc = arr[maxIdx].Ls - 1;
		int Rc = arr[maxIdx].Rs - 1;

		int Lidx = maxIdx - 1;
		int Ridx = maxIdx + 1;

		int tempL = 0;
		while (Lc >= 0) {
			arr[Lidx].Ls = Lc;
			arr[Lidx].Rs = tempL;
			Lidx--;
			Lc--;
			tempL++;
		}

		int tempR = 0;
		while (Rc >= 0) {
			arr[Ridx].Rs = Rc;
			arr[Ridx].Ls = tempR;
			Ridx++;
			Rc--;
			tempR++;
		}
		//PrintStallArray();
		//cout << "\n\n\n" << endl;

		for (int i = 0; i < n; i++) {
			if (arr[i].check == false) {
				FindMaxMin(i);
				if (MinMax < minArray[i]) {
					MinMax = minArray[i];
				}
			}
		}

		MinMaxVec.clear();
	}
}






//Stall �迭 �ʱ�ȭ
void InitStallArray() {
	arr[0].Ls = 0;
	arr[0].Rs = n - 1;
	arr[0].check = false;
	FindMaxMin(0);

	for (int i = 1; i < n; i++) {
		arr[i].Ls = arr[i - 1].Ls + 1;
		arr[i].check = false;
		arr[i].Rs = arr[i - 1].Rs - 1;
		FindMaxMin(i);
	}
	//PrintStallArray();
}





void Init() {
	fin.open("C-small-1-attempt5.in");
	ofn.open("ans.txt");
	fin >> testcase;

	for (int i = 1; i <= testcase; i++) {
		fin >> n;
		fin >> k;
		cout << "�׽�Ʈ ������ : n = " << n << ", k = " << k << endl;

		
		int MaxAns, MinAns;

		if (n == k) {
			MaxAns = 0;
			MinAns = 0;
		}
		else
		{
			InitStallArray();
			Solution();

			int leftAns = arr[ansIdx].Ls;
			int rightAns = arr[ansIdx].Rs;

			if (leftAns > rightAns) {
				MaxAns = leftAns;
				MinAns = rightAns;
			}
			else {
				MaxAns = rightAns;
				MinAns = leftAns;
			}
		}
		

		cout << "���� " << MaxAns << " , " << MinAns << "\n\n"<<endl;
		ofn << "Case #" << i << ": " << MaxAns << " " << MinAns << endl;
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