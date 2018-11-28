#include <iostream>
#include <fstream>
#include <algorithm>
#include <math.h>
#include <string>
#include <iomanip>
#include <cstdlib>
#include <vector>

using namespace std;

struct greater
{
	template<class T>
	bool operator()(T const &a, T const &b) const { return a > b; }
};


const long double PI = 3.1415926535897932384626433832795028841971693993751058209749445923078164L;

int main() {
	ofstream fout("cakelarge.out");
	ifstream fin("cakelarge.in");
	int T;
	fin >> T;
	for (int t = 0; t < T; t++) {
		int N, K;
		fin >> N >> K;
		vector< pair<long long, long long>> pancakes;
		for (int n = 0; n < N; n++) {
			long r, h;
			fin >> r >> h;
			pancakes.push_back(make_pair(r, h));
		}
		//cout << N << " " << K << endl;
		sort(pancakes.begin(), pancakes.end());
		vector<long long> side;
		for (int n = 0; n < N; n++) {
			side.push_back(2 * pancakes[n].first*pancakes[n].second);
		}
		long long answer = 0;
		for (int i = 0; i < N + 1 - K; i++) {
			long long surface = pancakes[N - 1-i].first*pancakes[N - 1-i].first;
			surface += side[N - 1 - i];
			vector<long long> copy;
			int j=0;
			while (j < N) {
				if (j != N - 1 - i&& !(pancakes[j].first > pancakes[N - 1 - i].first)) {
					copy.push_back(side[j]);
				}
				j++;
			}
			sort(copy.begin(), copy.end(), greater());
			for (int k = 0; k < K - 1; k++)
			{
				surface += copy[k];
			}
			if (answer < surface) {
				answer = surface;
			}
		}
		long double ans = PI*answer;
		cout << "Case #" << t + 1 << ": " << setprecision(10) << fixed << ans << endl;
		fout << "Case #" << t + 1 << ": " << setprecision(10) << fixed << ans << endl;
	}
	system("pause");
}