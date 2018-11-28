#include <bits/stdc++.h>
using namespace std;

int main()
{
	int T;
	cin >> T;
	cout.precision(15);
	for(int testCase = 1; testCase <= T; testCase++){
		cout << "Case #" << testCase << ": ";
		int N, K;
		cin >> N; cin >> K;
		vector <pair <long long, long long> > RH(N);
		for(int i = 0; i < N; i++){
			cin >> RH[i].first; cin >> RH[i].second; 
		}
		sort(RH.begin(), RH.end(), [&](pair <long long, long long> aa, pair <long long, long long> bb){return aa.first * aa.second > bb.first * bb.second;});
		long long A = 0;
		long long R0 = 0;
		for(int i = 0; i < K - 1; i++){
			A += 2 * RH[i].first * RH[i].second;
			R0 = max(R0, RH[i].first);
		}
		long long Emax = 0;
		for(int i = K - 1; i < N; i++){
			Emax = max(Emax, A + max(R0, RH[i].first) * max(R0, RH[i].first) + 2 * RH[i].first * RH[i].second);
		}
		cout << 3.1415926535897932 * Emax << endl;
	}
  return 0;
}
