#include <bits/stdc++.h>

using namespace std;

#define sd(x) scanf("%d", &x)
#define boost ios_base::sync_with_stdio(false);
#define mp make_pair
#define pb push_back
#define all(a) a.begin(), a.end()
#define f first
#define s second
#define TRACE
#ifdef TRACE
#define trace(...) __f(#__VA_ARGS__, __VA_ARGS__)
template <typename Arg1>
void __f(const char* name, Arg1&& arg1) {
  cerr << name << " : " << arg1 << endl;
}
template <typename Arg1, typename... Args>
void __f(const char* names, Arg1&& arg1, Args&&... args) {
  const char* comma = strchr(names + 1, ',');
  cerr.write(names, comma - names) << " : " << arg1<<" | ";
  __f(comma+1, args...);
}
#else
#define trace(...)
#endif

typedef pair <int, int> pii;
typedef long long ll;
typedef vector <vector <ll>> matrix;

const int mod = 1000000007;
const int inf = 50000000;
const int maxn = 1005;

int n, k;
char str[maxn];

void flip(int s) {
	for (int i = s; i < s + k; i++) {
		if (str[i] == '+') {
			str[i] = '-';
		}
		else {
			str[i] = '+';
		}
	}
}

int check() {
	for (int i = 1; i <= n; i++) {
		if (str[i] == '-') {
			return 0;
		}
	}
	return 1;
}

int main() {
	// freopen("A.in", "r", stdin);
	// freopen("o.txt", "w", stdout);
	int t, cn = 1;
	scanf("%d", &t);
	while (t--) {
		scanf("%s %d", str + 1, &k);
		n = strlen(str + 1);
		int ans = 0;
		for (int i = 1; i <= n - k + 1; i++) {
			if (str[i] == '-') {
				flip(i);
				ans += 1;
			}
		}
		if (check()) {
			printf("Case #%d: %d\n", cn++, ans);
		}
		else {
			printf("Case #%d: IMPOSSIBLE\n", cn++);
		}
	}
	return 0;
}