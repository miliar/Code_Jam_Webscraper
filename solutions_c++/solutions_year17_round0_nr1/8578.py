#include <bits/stdc++.h>

using namespace std;

int main(void) {

	ios_base::sync_with_stdio(false);

	ifstream fin;
	fin.open("A-large.in");

	ofstream fout;
	fout.open("output.out");

	int t;
	fin>>t;
	for(int tt = 1; tt <= t; ++tt) {
		string s;
		int k;
		fin>>s>>k;
		int ns = s.size();
		int ans = 0;
		for(int i = 0; i <= ns-k; ++i) {
			if(s[i] == '+')	continue;
			ans++;
			for(int j = i; j < i+k; ++j) {
				if(s[j] == '-')	s[j] = '+';
				else			s[j] = '-';
			}
		}
		bool flag = true;
		for(int i = 0; i < ns; ++i) {
			if(s[i] == '-') {
				flag = false;
			}
		}
		if(flag)
			fout<<"Case #"<<tt<<": "<<ans<<"\n";
		else
			fout<<"Case #"<<tt<<": IMPOSSIBLE\n";

	}

	return 0;

}