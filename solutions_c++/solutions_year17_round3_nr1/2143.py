// t1

#include <iostream>
#include <vector>
#include <algorithm>
#include <fstream>
#include <memory.h>

using namespace std;

const double pi = 3.14159265359;

vector <pair <double, double> > pan;
double dpTable[1004][1004];

// 최대값 리턴
double bigPi(int, int);

int main()
{

	ofstream fout;
	fout.open("output.txt");
	cout << fixed;
	cout.precision(9);

	fout << fixed;
	fout.precision(9);

	// testCase
	int testCase;	cin >> testCase;
	for (int t = 1; t <= testCase; t++) {
		
		// input & init
		int n, k;	cin >> n >> k;
		double panR, panH;
		pan.clear();
		for (int i = 0; i < n; i++) {
			cin >> panR >> panH;
			pan.push_back({panR * panR * pi, 2 * pi * panR * panH});
		}
		memset(dpTable, 0, sizeof(dpTable));

		// n개 중에 k개를 골라 겉넓이가 최대값 가지도록 설계
		// 1. sort
		sort(pan.begin(), pan.end());
		
		// 2. solve
		double ans = 0.0;
		for (int i = n - 1; i > -1; i--) {;
			ans = max(ans, pan[i].first + pan[i].second + bigPi(i, k - 1));
		}
		cout << "Case #" << t << ": " << ans << endl;
		fout << "Case #" << t << ": " << ans << endl;
	}
}

// 남은 n개 중에 k개를 골라 최대 값을 리턴
double bigPi(int n, int k) {
	if (k <= 0 || n < k)
		return 0;

	double &ret = dpTable[n][k];

	if (ret > 0)
		return ret;
	if (n == k) {
		ret = 0;
		for (int i = n - 1; i > -1; i--)
			ret += pan[i].second;
		return ret;
	}

	for (int i = n - 1; i > -1; i--)
		ret = max(ret, bigPi(i, k - 1) + pan[i].second);
	return ret;
}