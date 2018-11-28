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

priority_queue<pii> q;
int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
	int T;
	cin >> T;
	int test = 0;
	while(test++<T){
		
		int n,k;
		cin >> n >> k;
		int l,r;
		q = priority_queue<pii> ();
		q.push(mp(n,-0));
		for(int i = 0;i < k;i++){
			pii t = q.top();
			q.pop();
			int x = t.X - 1;
			int y = -t.Y;
			int x1 = x/2;
			int x2 = x - x1;
			int y1 = y;
			int y2 = y + x1 + 1;
			q.push(mp(x1,-y1));
			q.push(mp(x2,-y2));
			l = max(x1,x2);
			r = min(x1,x2);
		}

		printf("Case #%d: ",test);
		cout << l << " " << r << endl;
	}

    return 0;
}