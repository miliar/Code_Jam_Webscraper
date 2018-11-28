#include <bits/stdc++.h>
#define rep(i,n) for(int i=0;i<(n);++i)
#define ALL(A) A.begin(), A.end()

using namespace std;

typedef long long ll;
typedef pair<int, int> P;

string i2s(int n){
	stringstream ss;
	ss << n;
	return ss.str();
}

bool is_tidy(int n){
	string s = i2s(n);
	int len = s.length();
	for (int i = 1; i < len; ++i){
		if (s[i-1] <= s[i]){
			continue;
		} // end if
		return false;
	} // end for
	return true;
}	

int main()
{
	ios_base::sync_with_stdio(0);
	cin.tie(0);
	int T; cin >> T;
	for (int t = 1; t <= T; ++t){
		int n; cin >> n;
		int res = -1;
		for (int i = n; i >= 0; --i){
			if (is_tidy(i)){
				res = i;
				break;
			} // end if
		} // end for
		cout << "Case #" << t << ": " << res << endl;
	} // end for
	
	return 0;
}
