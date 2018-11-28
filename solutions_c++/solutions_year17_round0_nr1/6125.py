#include<stdio.h>
#include<math.h>
#include<iostream>
#include<map>
#include<algorithm>
#include<string.h>

#define in(n) scanf("%d",&n)
#define inl(n) scanf("%ld",&n)
#define inll(n) scanf("%lld",&n)
#define ins(s) scanf("%s",s)
#define out(n) printf("%d",n)
#define outl(n) printf("%ld",n)
#define outll(n) printf("%lld",n)
#define outs(n) printf("%s",s)
#define br printf("\n")

#define max(x, y) x>y?x:y
#define min(x, y) x<y?x:y
typedef long long int lli;
using namespace std;

void solve(int tt) {
	string s; int k;
	cin >> s >> k;
	int count = 0, change = 0, i, j;
	for (i = 0 ; i < s.size() - k ; i++) {
		if (s[i] == '-') {
			change++;
			for (j = i ; j < i + k ; j++) {
				s[j] = s[j] == '-' ? '+' : '-';
			}
		}
	}
	if (s[s.size() - k] == '-') {
		change++;
		for (j = s.size() - k ; j < s.size() ; j++) {
			s[j] = s[j] == '-' ? '+' : '-';
		}
	}
	for (i = 0 ; i < s.size() ; i++) if (s[i] == '+') count++;
	cout << "Case #" << tt << ": ";
	if (count == s.size()) {
		cout << change;
	} else {
		cout << "IMPOSSIBLE";
	}
	cout << endl;
}

int main() {
	int o = 1;
	if (o) {
		freopen("a_large.in", "r", stdin);
		freopen("a_large.txt", "w", stdout);
	}
	int t;
	cin >> t;
	for (int i = 1 ; i <= t ; i++) solve(i);
	return 0;
}


