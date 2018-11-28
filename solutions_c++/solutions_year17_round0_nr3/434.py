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

		//初期化
		S.insert(N); MAP[N]++;

		while (K > 0) { // K人を配置しながら減らしていく
			auto itr = S.end();
			--itr;
			long long int H = *itr; // 最大の連結成分
			long long int num = MAP[H]; // その個数

			
			if (num < K) {  // num<Kであれば, num個のH連結成分をすべて消去
			S.erase(itr--); //最大の連結成分を消去
			K -= num;
			S.insert(H / 2); MAP[H / 2] += num;   //新たに二つの連結成分が生じる　個数も記録
			S.insert(H - H / 2 - 1); MAP[H - H / 2 - 1] += num;
			}
			else {     // 最後の人のH連結成分は今のもの
				break;
			}
		}

		auto itr = S.end();
		--itr;
		long long int H = *itr; // 残っている最大の連結成分

		long long int MAX = H / 2;
		long long int MIN = H - H / 2 - 1;

		cout << "Case #" << t + 1 << ": " <<MAX<<" " <<MIN << endl;
		ofs << "Case #" <<t+1<<": "<<MAX<<" " <<MIN << endl;

	} // end of test cases


	system("pause");
	return 0;
}