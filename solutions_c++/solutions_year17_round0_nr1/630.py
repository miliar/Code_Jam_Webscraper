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

int n, k;
string str;
void solve(){
	cin >> str >> k;
	int cnt = 0;
	for (int i = 0; i + k <= str.size(); ++i){
		if (str[i] == '-'){
			REP(j, i, i + k - 1) str[j] = str[j] == '+' ? '-' : '+';
			++cnt;
		}
	}
	int fl = 1;
	RVC(i, str) if (str[i] == '-') fl = 0;
	if (fl) cout << cnt << endl;
	else cout << "IMPOSSIBLE\n";
}

int main(){
	int T = read();
	REP(kas, 1, T){
		printf("Case #%d: ", kas);
		solve();
	}
	return 0;
}