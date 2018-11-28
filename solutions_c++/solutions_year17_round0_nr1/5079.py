#include <stdio.h>
#include <iostream>
#include <fstream>
#include <algorithm>
#include <vector>
#include <string>
#include <queue>
#include <map>
#include <set>
#include <cmath>
#include <sstream>
#include <stack>
#include <string.h>
#include <list>
#include <time.h>

#define pb push_back
#define mp make_pair
#define X first
#define Y second
#define PI 3.14159265358979
#define forn(i, n) for(int i = 0; i < n; ++i)
#define ALL(x) x.begin(), x.end()
#define L(s) (int)((s).size())
#define sz(s) (int)((s).size())
#define ms(x) memset(x,0,sizeof(x))
#define ms1(x) memset(x,-1,sizeof(x))
#define del(y,x) erase(y.begin()+x)

typedef long long ll;
using namespace std;
typedef pair<int,int> pii;
const int INF = 2147483647;
const ll LLINF = 9223372036854775807LL;
const int ST = 100010;
const int ST1 = 1000010;
const ll MOD = 1000000007;

ll ABS(ll a) {
    if(a<0)
        return a*(-1);
    else
        return a;
}

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
	int T;
	cin >> T;
	int test = 0;
	while(test++<T){
		string a;
		cin >> a;
		int k;
		cin >> k;
		int ans = 0;
		for(int i = 0;i <= L(a)-k;i++){
			if(a[i] == '-'){
				ans++;
				for(int j = i;j < i+k;j++){
					if(a[j] == '-')
						a[j] = '+';
					else
						a[j] = '-';
				}
			}
		}
		for(int i = 0;i < L(a);i++)
			if(a[i] == '-')
				ans = -1;
		printf("Case #%d: ",test);
		if(ans == -1){
			cout << "IMPOSSIBLE" << endl;
		}else
			cout << ans << endl;
	}

    return 0;
}