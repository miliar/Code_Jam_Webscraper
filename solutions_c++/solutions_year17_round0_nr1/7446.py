#include <cstdio>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <set>
#include <map>
#include <queue>
#define mp make_pair
#define pb push_back
#define fir first
#define sec second
using namespace std;
typedef long long ll;

template <typename T> inline void R(T &x) {
	char ch = getchar(); x = 0;
	for (; ch<'0' || ch>'9'; ch = getchar());
	for (; ch<='9' && ch>='0'; ch=getchar()) x = x*10 + ch-'0';
}
char S[1005];
int n, k;
void run() {
	scanf("%s%d", S, &k);
	n = strlen(S);
	for (int i=0; i<n; ++i) S[i] = (S[i] == '+');
	int ans = 0;
	for (int i=0; i+k<=n; ++i)
		if (S[i] == 0) {
			++ans;
			for (int j=i; j<i+k; ++j)
				S[j] ^= 1;
		}
	for (int i=n-k; i<n; ++i)
		if (!S[i]) {
			puts("IMPOSSIBLE");
			return;
		}
	printf("%d\n", ans);
}
int main(){
	int T; R(T);
	for (int i=1; i<=T; ++i) {
		printf("Case #%d: ", i);
		run();
	}
	return 0;
}