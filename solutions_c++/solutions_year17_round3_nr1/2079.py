#define _USE_MATH_DEFINES
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

vector<int> R, H;
vector<pair<long long int, long long int> > cake;
long long int N,K;

long long int C[1010][1010];

int main()
{
	ifstream ifs("A-small-attempt1.in");
	ofstream ofs("answer_A_small");
	long long int  T;
	ifs >> T; cout << "T= " << T << endl;

	for (int t = 0; t<T; t++) {  // test cases

		ifs >> N >> K;
		cout << "N= " << N << "  K= " << K << endl;
		R.clear(); H.clear();
		R.push_back(-1); H.push_back(-1);

		cake.clear();

		long long int temp1, temp2;
		pair<long long int, long long int> temp_p;

		temp1 = -1; temp2 = -1; temp_p.first = -1; temp_p.second = -1;
		cake.push_back(temp_p);

		for (int i = 0; i < N; i++) {
			ifs >> temp1; 
			ifs >> temp2; 
			temp_p.first = temp1; temp_p.second = temp2;
			cake.push_back(temp_p);
		}

		sort(cake.begin(),cake.end());

		/*for (int i = 0; i<int(cake.size()); i++) {
			cout << cake[i].first << " " << cake[i].second << endl;
		}*/

		for (int k = 1; k <= K; k++) {
			for (int i = 1; i <= N; i++) {
				C[k][i] = 0;
			}
		}

		for (int i = 1; i <= N; i++) {
			C[1][i] = cake[i].first*cake[i].first + 2*cake[i].first * cake[i].second;
		}

		long long int  MAX_V = 0;
		for (int k = 2; k <= K; k++) {
			for (int i = 1; i <= N; i++) {
				MAX_V = 0;
				for (int j = 1; j < i; j++) {
					MAX_V = max(MAX_V, C[k - 1][j] + cake[i].first*cake[i].first - cake[j].first*cake[j].first + 2*cake[i].first*cake[i].second);
				}
				C[k][i] = MAX_V;
			}
		}

		MAX_V = 0.0;

		for (int i = 1; i <= N; i++) {
			MAX_V = max(MAX_V,C[K][i]);
		}

		
		cout << "Case #" << t + 1 << ": " <<fixed << setprecision(9)<<MAX_V*M_PI<<endl;
		ofs << "Case #" << t + 1 << ": " << fixed << setprecision(9) << MAX_V*M_PI << endl;

	} // end of test cases

	system("pause");

	return 0;
}