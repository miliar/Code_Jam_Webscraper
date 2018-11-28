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
		//���� ���ø�
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
			//��������
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
3��
������������ ��� �ùķ��̼� ����(���10��,�޸� 1000)
�߰������� ���� �ùĵ���(���1��,�޸�100��)

�����ͱ���:
���� ť ����� ��
ó��: N�� ������
����: ��-���� ������ ���� ��

���� ���ҹ��: ¦�������� 0.5n-1�� ����, 0.5n�� ������((n/2)-1,n/2)
Ȧ�������� 0.5n-0.5�� ����+������(n/2,n/2)
n/2, (n-1)/2

��������:
�̶��� ���� ��� ���������� ���
ó��:N������ 1
A B

A B C D

A�� �پ��� B C D
B�� �پ��� C D
C D E F �� ����
������: 2�� �ɰ��� 1,0
1�� �ɰ��� 0,0

*/