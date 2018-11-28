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

long long int D;
int N;

vector<long long int> K;
vector<int> S;

int main()
{
	ifstream ifs("A-large.in");
	ofstream ofs("answer_A_large");
	int T;
	ifs >> T; cout << "T= " << T << endl;

	for (int t = 0; t<T; t++) {  // test cases

		ifs >> D; cout << "D= " << D << endl;
		ifs >> N; cout << "N= " << N << endl;

		long long int temp;
		int dummy;

		K.clear(); S.clear();
		for (int i = 0; i < N; i++) {
			ifs >> temp;  K.push_back(temp);
			ifs >> dummy; S.push_back(dummy);
		}

		long double ans = 9.9e120;

		for (int i = 0; i < N; i++) {
			ans = min(ans,(long double) 1.0*D*S[i] / (D - K[i]));

			//cout << 1.0*D*S[i] / (D - K[i]) << endl;
		}

		cout << "Case #" << t + 1 << ": " <<ans<< endl;
		ofs << "Case #" <<t+1<<": "<<fixed<<setprecision(8)<<ans <<endl;

	} // end of test cases

	system("pause");

	return 0;
}