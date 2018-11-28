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

int check(string s) {
	for (int i = 0 ; i < s.size() - 1 ; i++) {
		if (s[i] > s[i + 1]) {
			return 0;
		}
	}
	return 1;
}

string remove_leading_zeros(string s) {
	s.erase(0, min(s.find_first_not_of('0'), s.size() - 1));
	return s;
}

void solve(int tt) {
	string s;
	cin >> s;
	int p, i, j;
	while (!check(s)) {
		p = s.size() - 2;
		for (i = p ; i >= 0 ; i--) {
			if(s[i] > s[i + 1]) {
				for (j = i + 1 ; j <= p + 1 ; j++) s[j] = '9';
				s[i]--;
			}
		}
		s = remove_leading_zeros(s);
	}
	cout << "Case #" << tt << ": " << s << endl;
}

int main() {
	int o = 1;
	if (o) {
		freopen("b_large.in", "r", stdin);
		freopen("b_large.txt", "w", stdout);
	}
	int t;
	cin >> t;
	for (int i = 1 ; i <= t ; i++) solve(i);
	return 0;
}


