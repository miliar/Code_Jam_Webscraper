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

char flip(char x) {return x == '+' ? '-' : '+';}

int main() {
#ifdef zzblack
	freopen("C:\\Users\\zzblack\\Desktop\\case.in","r",stdin);
    freopen("C:\\Users\\zzblack\\Desktop\\case.out","w",stdout);
#endif
    int T, cas = 1; cin >> T;
    while (T--) {
    	printf("Case #%d: ", cas++);
    	string s; cin >> s;
    	while (1) {
	    	bool ok = 1;
	    	for (int i = 1; s[i]; i++) {
	    		if (ok == 0) s[i] = '9';
	    		if (s[i] >= s[i-1]) continue;
	    		ok = 0;
	    		s[i] = '9';
	    		int id = i-1;
	    		while (s[id] == '0') s[id] = '9';
	    		s[id]--;
	    	}
	    	if (ok) break;
    	}
    	bool lead = 1;
    	for (int i = 0; s[i]; i++)
    		if(s[i] == '0' && lead == 1) continue;
    		else {
    			lead = 0;
    			printf("%c", s[i]);
    		}
    	puts("");

    }


    return 0;
}

    
