#include <fstream>
#include <sstream>
#include <iostream>
#include <string>
#include <vector>
#include <utility>
#include <algorithm>
#include <iomanip>
#include <map>
#include <set>
#include <queue>
#include <cmath>

using namespace std;

long long int N;
long long int K;

int main()
{
	ifstream ifs("C-large.in");
	ofstream ofs("answer_C_large");
	int T;
	ifs >> T; cout << "T= " << T << endl;

	for (int t = 0; t<T; t++) {  // test cases
		
		ifs >> N; cout << "N= " << N << endl;
		ifs >> K; cout << "K= " << K << endl;

		set<long long int> S;
		map<long long int, long long int> MAP;

		//������
		S.insert(N); MAP[N]++;

		while (K > 0) { // K�l��z�u���Ȃ��猸�炵�Ă���
			auto itr = S.end();
			--itr;
			long long int H = *itr; // �ő�̘A������
			long long int num = MAP[H]; // ���̌�

			
			if (num < K) {  // num<K�ł����, num��H�A�����������ׂď���
			S.erase(itr--); //�ő�̘A������������
			K -= num;
			S.insert(H / 2); MAP[H / 2] += num;   //�V���ɓ�̘A��������������@�����L�^
			S.insert(H - H / 2 - 1); MAP[H - H / 2 - 1] += num;
			}
			else {     // �Ō�̐l��H�A�������͍��̂���
				break;
			}
		}

		auto itr = S.end();
		--itr;
		long long int H = *itr; // �c���Ă���ő�̘A������

		long long int MAX = H / 2;
		long long int MIN = H - H / 2 - 1;

		cout << "Case #" << t + 1 << ": " <<MAX<<" " <<MIN << endl;
		ofs << "Case #" <<t+1<<": "<<MAX<<" " <<MIN << endl;

	} // end of test cases


	system("pause");
	return 0;
}