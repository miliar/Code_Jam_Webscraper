#include <cstdio>
#include <iostream>
#include <vector>
#include <string>
using namespace std;

int dp[101][2];

int main() {
	ios::sync_with_stdio(false);
	cin.tie(nullptr);
	cout.precision(10);
	cout << fixed;

	int T;
	cin >> T;
	for(int to=1;to<=(int)T;++to){
		cout << "Case #"<< to <<": ";
		int K;
		string s;
		cin >> s;
		cin >> K;
		int n = s.size();
		int flg = 0;
		int cnt =0;
		for(int i=0;i<n;i++){
			if(s[i] == '-' && i+K <= n ){
				for(int j = i ;j<i+K;j++){
					s.replace(j, 1, s[j]=='-'?"+":"-");
				}
				cnt+=1;
			 }
		}
		string ret = s.find("-")!=string::npos?"IMPOSSIBLE":to_string(cnt); 
		cout << ret << "\n";
	}
#ifdef LOCAL_DEFINE
	cerr << "Time elapsed: " << 1.0 * clock() / CLOCKS_PER_SEC << " s.\n";
#endif
	return 0;
}

