#include <bits/stdc++.h>

#define N 1000007
#define it(i, n) for(i = 0; i < n; ++i)
#define pb push_back
#define eps 1e-9
#define all(x) x.begin(), x.end() 

using namespace std;
typedef long long ll;

void decchar(string& s, int p) {
	if(s[p] == '0') s[p] = '9';
	else s[p]--;
}

int main(int argc, char * argv[]) {
	int i, j, k, m, n, p, q, r, t;
	string s;
	scanf("%d", &t);

	it(j, t) {
		cin >> s;
		printf("Case #%d: ", j+1);
		for(i = s.size()-1; i >= 1; --i) {
			if(s[i-1] > s[i]) {
				decchar(s, i-1);
				for(k = i; k < s.size(); ++k) s[k] = '9';
			}
		}
		for(i = 0; i < s.size() and s[i] == '0'; ++i);
		for(; i < s.size(); ++i) printf("%c", s[i]);
		printf("\n");
	}

	//1110


	return 0;
}