#include <bits/stdc++.h>
#define rep(i,n) for(int i=0;i<(n);++i)
#define ALL(A) A.begin(), A.end()

using namespace std;

typedef long long ll;
typedef pair<int, int> P;

int solve(string s, int k){
	int res = 0;
	int n = s.length();
	for (int i = 0; i < n; ++i){
		if (s[i] == '-'){
			++res;
			for (int j = i; j < k + i; ++j){
				if (j == n) return -1;
				if (s[j] == '-'){
					s[j] = '+';
				}else{
					s[j] = '-';
				} // end if
			} // end for
		} // end if
	} // end for

	int cnt = 0;
	rep (i, n) cnt += (int)(s[i] == '+');
	
	return (cnt == n ? res : -1);
}

int main()
{
	ios_base::sync_with_stdio(0);
	cin.tie(0);
	int T; cin >> T;
	for (int t = 1; t <= T; ++t){
		string s; int k; cin >> s >> k;
		int res = solve(s,k);
		cout << "Case #" << t << ": ";
		if (res < 0){
			cout << "IMPOSSIBLE";
		}else{
			cout << res;
		} // end if
		cout << endl;
	} // end for

	return 0;
}
