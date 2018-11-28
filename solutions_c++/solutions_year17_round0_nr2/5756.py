
#include <bits/stdc++.h>

using namespace std;

bool ok(long long x) {
	int lst = -1;
	while(x > 0) {
		if(lst == -1) { lst = x % 10; continue; }
		else if((x % 10) > lst) return false;
		lst = x % 10;
		x /= 10;
	}
	return true;
}

long long brute(long long x) {
	while(!ok(x) && x >= 0) x--;
	return x;
}

int main(void) {

	int t;
	int nCase;
	long long n, k, N;
	string s;

	cin >> t;
	//t = 1000;
	nCase = 1;

	while(t--) {
		printf("Case #%d: ", nCase);
		nCase += 1;

		cin >> s;                    
		string S = s;


		k = 0;
		for(int i = 0; i < (int)s.size(); i++)
			k = k * 10 + (s[i] - '0');

		k /= 10;
		int len = 0;
		if(k != 0) {
			while(k > 0) {
				len += 1;
				k /= 10;
			}
			k = 0;
			for(int i = 0; i < len; i++)
				k = k * 10 + 9;
		}

		int flag = 0;
		for(int i = 1; !flag && i < (int)s.size(); i++) {
			if(s[i] < s[i - 1]) {
				flag = 1;
				s[i - 1] -= 1;
				for(int j = i; j < (int)s.size(); j++)
					s[j] = '9';
				for(int j = i - 1; j >= 0; j--) {
					if(j + 1 < (int)s.size() && s[j + 1] < s[j])
						s[j] = s[j + 1];
				} 
			}
		}

		for(int i = 0; i < (int)s.size(); i++) {
			if(s[i] < S[i]) {
				char mx = '0';
				for(int j = i + 1; j < (int)s.size(); j++)
					mx = max(mx, s[j]);
				for(int j = i + 1; j  <(int)s.size(); j++)
				s[j] = mx;
			}
		}


		n = 0;
		for(int i = 0; i < (int)s.size(); i++) {
			n = n * 10 + (s[i] - '0');
		}

		printf("%lld\n", max(k, n));
	}


	return 0;
}