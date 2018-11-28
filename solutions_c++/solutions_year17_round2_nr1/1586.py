#include<iostream>
#include<fstream>
#include<stdio.h>
#include<string>
#include<vector>
#include<map>
#include<math.h>
#include<algorithm>
#include<iomanip>

using namespace std;

int main() {
	ifstream ifs("in.txt");
	ofstream ofs("out.txt");
	int t;
	ifs >> t;
	for (int loop = 1; loop <= t; loop++) {
		int n;
		long long d;
		double ans;
		vector<long long> k, s;
		ifs >> d >> n;
		k.resize(n);
		s.resize(n);
		for (int i = 0; i < n; i++) {
			ifs >> k[i] >> s[i];
		}
		vector<double> time;
		time.resize(n);
		for (int i = 0; i < n; i++) {
			time[i] = (double)(d - k[i]) / (double)(s[i]);
		}
		sort(time.begin(), time.end());
		ans = (double)d / time[time.size() - 1];
		ofs << "Case #" << loop << ": "<< fixed << setprecision(6)  << ans << endl;
	}
	return 0;
}