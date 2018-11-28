#include <bits/stdc++.h>
#define REP(i, a, b) for (int i = a; i <= b; ++i)
#define PER(i, a, b) for (int i = a; i >= b; --i)
#define RVC(i, S) for (int i = 0; i < S.size(); ++i)
#define fi first
#define se second
#define mp make_pair
#define pb push_back
#define debug(...) fprintf(stderr, __VA_ARGS__)
using namespace std;
 
typedef long long LL;
typedef pair<int, int> pii;
typedef vector<int> VI;
typedef unsigned long long ULL;
 
inline int read(){
    int x = 0, ch = getchar(), f = 1;
    while (!isdigit(ch)){if (ch == '-') f = -1; ch = getchar();}
    while (isdigit(ch)) x = x * 10 + ch - '0', ch = getchar();
    return x * f;
}

LL p10[19];

int valid(LL x){
	int stk[20], tp = 0;
	while (x){
		stk[++tp] = x % 10;
		x /= 10;
	}
	REP(i, 1, tp - 1) if (stk[i] < stk[i + 1]) return 0;
	return 1;
}

void solve(){
	LL n;
	cin >> n;
	if (valid(n)){
		cout << n << endl;
		return;
	}
	for (int i = 1; i <= 18 && p10[i] <= n; ++i){
		if (valid(n / p10[i] - 1)){
			cout << (n / p10[i] - 1) * p10[i] + p10[i] - 1 << endl;
			return;
		}
	}
}

int main(){
	int T = read();
	p10[0] = 1;
	REP(i, 1, 18) p10[i] = p10[i - 1] * 10ll;

	REP(kas, 1, T){
		printf("Case #%d: ", kas);
		solve();
	}
	return 0;
}