#include <bits/stdc++.h>

using namespace std;

bool test (string s) {
	int n = s.size();
	for (int i = 0; i < n; i++)
		if (s[i])
			return false;
			
	return true;
}

int main() {
	int tst;
	cin>>tst;
		
	for (int t = 0; t < tst; t++) {
		string s;
		int k;
		cin>>s>>k;
		int n = s.size();
		for (int i = 0; i < n; i++) {
			if (s[i] == '+')
				s[i] = 0;
			else
				s[i] = 1;
		}
		int res = 1000;
		
		int nn = 1<<(n-k + 1);
		for (int i = 0; i < nn; i++) {
			int x = i, start = 0, moves = 0;
			string sol = s;
			while (x) {
				if (x & 1) {
					for (int j = start; j < start + k; j++)
						sol[j] = 1-sol[j];
						moves++;
				}
				start++;
				x >>= 1;
			}
			
			if (test(sol))
				res = min(res, moves);
		}
	
		if (res < 1000)	
			cout<<"Case #"<<t+1<<": "<<res<<endl;
		else
			cout<<"Case #"<<t+1<<": "<<"IMPOSSIBLE"<<endl;
				
	}

	return 0;

}



