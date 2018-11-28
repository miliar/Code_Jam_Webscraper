#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <vector>
#include <cmath>
#include <queue>
#include <stack>
#include <map>
#include <string>

using namespace std;

# define pb push_back
# define mp make_pair


typedef long long ll;
typedef pair<int,int> PII;

const int maxn =  1010;
const double pi = atan(1)*4;

int n,k;
struct one{
	double h,r;
	double area;
};
one a[maxn];

bool cmp(const one & s1 , const one & s2) {
	return s1.r > s2.r;
}
bool cmp2(const one & s1, const one & s2) {
	return s1.area > s2.area;
}
 
int main()
{
	// freopen("input.txt","r",stdin);
	freopen("A-large.in", "r", stdin);
	freopen("output.txt","w", stdout);
	int ncase, T , D, n, k, s;
	double ans;
	ncase = 0;
	cin >> T;
	while(T --) {
		ncase++;
		cin >> n >> k;
		for(int i = 1; i <= n; i++) {
			cin >> a[i].r >> a[i].h;
			a[i].area = 2*pi*1.0*a[i].r * a[i].h;
		}
		sort(a+1,a+n+1, cmp);
		double ans = 0;
		for(int i = 1; i <= n; i++) {
			// cout << "a[" << i << "] r = " << a[i].r << endl;
			double base = 2*pi*a[i].r * a[i].h + pi*(a[i].r*a[i].r);
			vector<one> v;
			if((n-i) < k-1) continue;
			for(int j = i+1; j <= n; j++) {
				v.push_back(a[j]);
			}
			sort(v.begin(), v.end(), cmp2);
			double tmp_ans = base;
			for(int j = 0; j < k-1; j++) {
				tmp_ans += (v[j].area);
				// cout << " j = " << j << " r = " << v[j].r << endl;
			}
			// cout << "i = " << i << " tmp_ans = " << tmp_ans << endl;
			ans = max(ans, tmp_ans);
		}
		printf("Case #%d: %.10lf\n",ncase,ans);
	}
	return 0;
}