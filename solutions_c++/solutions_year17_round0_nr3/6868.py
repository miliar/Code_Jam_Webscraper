#include <iostream>
#include <fstream>
#include <vector>
using namespace std;

//크기 n인 배열에서 중간인덱스(홀수이면 Ls=Rs, 짝수이면 Ls가 Rs보다 많아지는 인덱스)
//를 기준으로 좌측의 Max와 Min값은 각각 Rs,Ls이고
//우측은 Ls, Rs이다.
//각 인덱스의 Ls/Rs를 살리는 것보다 Max,Min값으로 LS Rs도 알수있따.



//Stall 구조체
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
vector<int> MinMaxVec; // 1단계에서 MinMax랑 같은 인덱스를 삽입
int n(0), k(0); // n : 탕의 수, k : 사람의 수
int MinMax(0); //1단계에서의 최소값들 중에 최대값을 계산하면서 구해서 변수에 넣고 같은 것의 인덱스만 찾아냄
int ansIdx(0); //최종 사람이 들어갈 인덱스 값을 가질 변수



//파일 입출력
ifstream fin;
ofstream ofn;


//Stall 배열의 Ls/Rs값 출력
void PrintStallArray() {
	for (int i = 0; i < n; i++) {
		cout << i << " stall : Ls = ";

		if (arr[i].check == true) {
			cout << "선택됨" << endl;
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


//sidx : 기준인덱스
void Solution() {

	for (int m = 0; m < k; m++) {
		//cout << "MinMax(1단계의 최대값) = " << MinMax << endl;

		//cout << "1단계에서 채택된 인덱스들 -----" << endl;
		//1단계
		for (int i = 0; i < n; i++) {
			if (minArray[i] == MinMax && arr[i].check==false) {
				//cout << i << "인덱스" << endl;
				MinMaxVec.push_back(i);
			}
		}
		MinMax = 0;

		//2단계
		int maxIdx(0), maxValue(0);
		//cout <<"1단계 선택된 인덱스 수 ="<< MinMaxVec.size() << endl;
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
		
		//cout<< "MaxValue(2단계의 최대값) = " << maxValue << endl;
		//cout << "maxIdx(사람이 최종 선택한 위치) = " << maxIdx << endl;
		arr[maxIdx].check = true;
		if (m == k - 1) {
			ansIdx = maxIdx;
		}

		//maxIdx를 기준으로 좌측으로 업데이트
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






//Stall 배열 초기화
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
		cout << "테스트 데이터 : n = " << n << ", k = " << k << endl;

		
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
		

		cout << "답은 " << MaxAns << " , " << MinAns << "\n\n"<<endl;
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