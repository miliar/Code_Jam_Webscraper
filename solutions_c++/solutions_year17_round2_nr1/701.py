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
const int N = 1005;
int n, d;
pair<int, int> a[N];
void run() {
	R(d); R(n);
	double t, mt = 0;
	for (int i=1; i<=n; ++i) { 
		R(a[i].fir), R(a[i].sec);
		if (a[i].fir < d) {
			t = (double)(d - a[i].fir) / a[i].sec;
			mt = max(t, mt);
		}
	}
	printf("%.9lf\n", d / mt);
}
int main( ){
	int T; R(T);
	for (int i=1; i<=T; ++i) {
		printf("Case #%d: ", i);
		run();
	}
	return 0;
}