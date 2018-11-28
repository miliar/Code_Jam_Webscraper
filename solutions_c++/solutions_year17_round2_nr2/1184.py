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

const int maxn =  (1e5)+10;


struct one {
	char c;
	int num;
	/* data */
};

bool cmp(const one & s1, const one & s2) {
	return s1.num > s2.num;
}

int main()
{
	// freopen("input.txt","r",stdin);
	freopen("B-small-attempt3.in", "r", stdin);
	freopen("output.txt","w", stdout);
	int ncase, T;
	int n,r,o,y,g,b,v;
	ncase = 0;
	cin >> T;
	while(T --) {
		ncase++;
		cin >> n >> r >> o >> y >> g >> b >> v;
		string ans = "";
		if(o != 0 || g != 0 || v != 0 )
			ans = "hehe";
		else {
			one a[4];
			a[0].c = 'R';
			a[0].num = r;
			a[1].c = 'Y';
			a[1].num = y;
			a[2].c = 'B';
			a[2].num = b;
			sort(a,a+3,cmp);
			if(a[0].num < a[1].num || a[1].num < a[2].num) {
				while(1);
			}
			if(a[0].num > a[1].num + a[2].num ) {
				ans = "IMPOSSIBLE";
			}
			else {
				int cnt1 = a[1].num + a[2].num - a[0].num;
				int cnt2 = a[0].num - a[2].num;
				int cnt3 = a[0].num - a[1].num;
				// cout << "cnt1 = " << cnt1 << " cnt2 = " << cnt2 << " cnt3 = " << cnt3 << endl;
				for(int i = 0 ; i < cnt1; i++) {
					ans += a[0].c;
					ans += a[1].c;
					ans += a[2].c;
				}
				for(int i = 0; i < cnt2; i++) {
					ans += a[0].c;
					ans += a[1].c;
				}
				for(int i = 0; i < cnt3; i++) {
					ans += a[0].c;
					ans += a[2].c;
				}
			}

		}
		printf("Case #%d: ",ncase);
		cout << ans << endl;
	}
	return 0;
}