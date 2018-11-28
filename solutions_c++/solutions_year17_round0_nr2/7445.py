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
ll ten[20], one[20];
void run() {
	ll res, a;
	scanf("%lld", &a);
	res = a;
	for (int i=18; i; --i) {
		ll cur = a / ten[i];
		int c = cur % 10;
		if (!cur) continue;
		if (a % ten[i] < c * one[i - 1]) {
			res = (cur - 1) * ten[i] + one[i - 1] * 9;
			break;
		}
	}
	printf("%lld\n", res);
}
int main(){
	int T; R(T);
	ten[0] = one[0] = 1;
	for (int i=1; i<=18; ++i)
		ten[i] = ten[i-1] * 10,
		one[i] = one[i-1] * 10 + 1;
	for (int i=1; i<=T; ++i) {
		printf("Case #%d: ", i);
		run();
	}
	return 0;
}