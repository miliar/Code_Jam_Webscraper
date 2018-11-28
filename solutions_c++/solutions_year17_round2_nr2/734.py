#include <set>
#include <map>
#include <queue>
#include <stack>
#include <cmath>
#include <bitset>
#include <string>
#include <cctype>
#include <cstdio>
#include <vector>
#include <cstdlib>
#include <cstring>
#include <iomanip>
#include <sstream>
#include <iostream>
#include <algorithm>
using namespace std;
#define ls id<<1,l,mid
#define rs id<<1|1,mid+1,r
#define OFF(x) memset(x,-1,sizeof x)
#define CLR(x) memset(x,0,sizeof x)
#define MEM(x) memset(x,0x3f,sizeof x)
typedef long long ll ;
typedef pair<ll,ll> pii ;
const int maxn = 150 ;
const int maxm = 1e6 + 50;
const double eps = 1e-10;
const int max_Index = 62;
const int inf = 0x3f3f3f3f ;
const int MOD = 1e9+7 ;

int num[6];
void add(string &x, int id) {
	if (id == 0) x += 'R';
	else if (id == 1) x += 'Y';
	else x += 'B';
}

int main() {
#ifdef zzblack
	freopen("C:\\Users\\zzblack\\Desktop\\case.in","r",stdin);
    freopen("C:\\Users\\zzblack\\Desktop\\case.out","w",stdout);
#endif
    int T, cas = 1; cin >> T;
    while (T--) {
    	printf("Case #%d: ", cas++);
    	int n; cin >> n;
    	bool ok = 1;
    	for (int i = 0; i < 6; i++) cin >> num[i];
    	for (int i = 0; i < 6; i++) {
    		int x = num[(i+2)%6] + num[(i+3)%6] + num[(i+4)%6];
    		if (num[i] > x) ok = 0;
    	}
    	if (!ok) puts("IMPOSSIBLE");
    	else {
    		string ans;
    		num[1] = num[2]; num[2] = num[4];
    		int id = 0;
    		if (num[1] > num[0]) id = 1;
    		if (num[2] > num[id]) id = 2;
    		int x = num[id];
    		int y = n - 2 * x;
    		int idx = 0, idy = 1;
    		if (id == 0) idx = 1, idy = 2;
    		else if (id == 1) idy = 2;
    		int lx = num[idx] - (y/2);
    		int ly = num[idy] - (y/2);
    		int begin = idx;
    		if (n % 2 && lx) lx--;
    		else if (n % 2 && ly) begin = idy, ly--;
    		int limit = begin == idx ? lx : ly;
    		for (int i = 1; i <= x; i++) {
    			add(ans, id);
    			if (i <= limit) {
    				add(ans, begin);
    			} else add(ans, idx+idy-begin);
    		}
    		for (int i = 0; i < y / 2; i++) {
    			add(ans, begin);
    			add(ans, idx+idy-begin);
    		}
    		if (ans.size() < n) add(ans, begin);
    		// else if (ans.size() > n) ans.pop_back();
    		// bool ok = 1;
    		// for (int i = 0; ans[i]; i++) 
    		// 	if (ans[i] == ans[i-1]) ok = 0;
    		// if (ans.back() == ans[0]) ok = 0;
    		// if (ans.size() != n) ok = 0;
    		// int a = 0, b = 0, c = 0;
    		// for (int i = 0; ans[i]; i++)
    		// 	if (ans[i] == 'R') a++;
    		// 	else if (ans[i] == 'Y') b++;
    		// 	else c++;
    		// if (a != num[0] || b != num[1] || c != num[2]) ok = 0;
    		cout << ans << endl;
    	}
    }

    return 0;
}

    
