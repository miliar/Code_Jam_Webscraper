#include<iostream>
using std::cin;
using std::cout;
static const int size_buf = 16;
long long kukan[size_buf];
long long kasu[size_buf];
int main() {
	int T;
	cin >> T;
	cin.get();
	for (int caseN = 1; caseN <= T; caseN++) {
		long long N, K;
		cin >> N >> K;
		cout << "Case #" << caseN << ": ";
		//구간 스플릿
		for (int i = 0; i < size_buf; i++){
			kukan[i] = 0;
			kasu[i] = 0;
		}
		//start
		kukan[0] = N;
		kasu[0] = 1;
		long long p = 0;
		int nK = 1;
		//enter person
		while (p < N){
			//구간분할
			long long sn = (kukan[0] - 1) / 2;
			long long ln = kukan[0] / 2;
			if (p + kasu[0] >= K){
				cout << ln << " " << sn;
				break;
			}
			//insert
			bool pass = false;
			for (int i = 1; i < nK; i++){
				if (kukan[i] == ln){
					kasu[i] += kasu[0];
					pass = true;
				}
			}
			if (pass == false){
				kukan[nK] = ln;
				kasu[nK] = kasu[0];
				nK++;
			}
			//insert small
			pass = false;
			for (int i = 1; i < nK; i++){
				if (kukan[i] == sn){
					kasu[i] += kasu[0];
					pass = true;
				}
			}
			if (pass == false){
				kukan[nK] = sn;
				kasu[nK] = kasu[0];
				nK++;
			}
			p += kasu[0];
			//move forward
			for (int i = 1; i < nK; i++){
				kukan[i - 1] = kukan[i];
				kasu[i - 1] = kasu[i];
			}
			nK--;

		}
		

	
		
		
		cout << std::endl;

	}
	//system("PAUSE");
	return 0;
}


/*
3번
작은사이즈의 경우 시뮬레이션 돌림(계산10만,메모리 1000)
중간사이즈 역시 시뮬돌림(계산1억,메모리100만)

데이터구조:
구간 큐 사용할 것
처음: N개 전구간
분할: 왼-오른 순으로 넣을 것

구간 분할방법: 짝수구간은 0.5n-1이 왼쪽, 0.5n이 오른쪽((n/2)-1,n/2)
홀수구간은 0.5n-0.5가 왼쪽+오른쪽(n/2,n/2)
n/2, (n-1)/2

라지도전:
이때는 구간 대신 구간개수를 사용
처음:N개구간 1
A B

A B C D

A를 다쓰면 B C D
B도 다쓰면 C D
C D E F 로 리셋
마지막: 2를 쪼개면 1,0
1을 쪼개면 0,0

*/