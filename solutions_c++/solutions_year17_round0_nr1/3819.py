#include <bits/stdc++.h>

#define REP(i, n) for(int i = 0; i < n; i++)

using namespace std;




void testcase(int tcn){
	string ss;
	int k;
	cin >> ss >> k;
	int n = ss.size();

	vector<int> s;
	s.resize(n);
	REP(i, n)s[i] = (ss[i] == '+' ? 1 : 0);

	int res = 0;
	REP(i, n){
		if(s[i] == 0){
//			cerr << i << endl;
			if(i+k > n){
				res = -1;
				break;
			}
			++res;
			for(int j = i; j < i+k; j++){
				s[j] = 1-s[j];
			}
		}
	}

	cout << "Case #"<<tcn<<": ";
	if(res == -1) cout << "IMPOSSIBLE"<<endl;
	else cout << res << endl;

}

int main(){
	int T;
	cin >> T;
	REP(i, T){
		testcase(i+1);
	}
	return 0;

}