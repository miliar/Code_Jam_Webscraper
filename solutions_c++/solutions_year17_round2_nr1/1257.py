#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <queue>
#include <stdio.h>
#include <iomanip>
//#include <utility>
using namespace std;
typedef long long ll;

int T;

int main()
{
	cin >> T;
	for (int testcase = 0; testcase < T; testcase++) {
		int D, N;
		cin >> D >> N;
		vector < pair<int, int> > H;
		for (int i = 0; i < N; i++) {
			int tmps, tmpk;
			cin >> tmpk >> tmps;
			pair<int,int> tmp = pair<int,int>(tmpk, tmps);
			H.push_back(tmp);
		}

		double maxtime = 0;
		for (int i = 0; i < N; i++) {
			double time = (D - H[i].first);
			time = time / H[i].second;
			//cout << setprecision(10) << D - H[i].first << " / " << H[i].second << " = " << time << endl;
			if (time > maxtime) {
				maxtime = time;
			}
		}
		//cout << maxtime << endl;
		double res = D / maxtime;
		cout << fixed << setprecision(6) << "Case #" << testcase + 1 << ": " << res << endl;
	}
	return 0;
}