#include <bits/stdc++.h>
using namespace std;
#define F first
#define S second
#define mp make_pair
#define pb push_back
#define mse(x , y) memset(x , y , sizeof(x))
#define IOS do{ ios :: sync_with_stdio(0); cin.tie(NULL); }while(0) 

typedef long long ll;
typedef pair<int , int> pii;

const int maxn = 1005;
const int INF = 0x3f3f3f3f;
const int mod = 1000000007;
const double eps = 1e-9;

int __ = 1 , kase = 0;

/************default************/

int n , m;
struct node {
	int d , s;
}a[maxn];

void init() {}

void read() {
	cin >> n >> m;
	for(int i = 0; i < m; i++) {
		cin >> a[i].d >> a[i].s;
	}
}

void solve() {
	double maxt = 0;
	for(int i = 0; i < m; i++) {
		maxt = max(maxt , (double)(n - a[i].d) / a[i].s);
	}
	printf("Case #%d: %.6lf\n" , ++kase , n / maxt);
}

int main() {
	scanf("%d" , &__);
	while(__--) {
		init();
		read();
		solve();
	}
	return 0;
}