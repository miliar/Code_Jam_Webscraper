#include <algorithm>
#include <bitset>
#include <cassert>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <deque>
#include <fstream>
#include <iostream>
#include <list>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <vector>


using namespace std;

#define pi acos(-1)
#define gcd(a,b) __gcd(a,b)
#define PB push_back
#define SIZE(x) (int)x.size()
#define clr(x,y) memset(x,y,sizeof(x))
#define MP(x,y) make_pair(x,y)
#define ALL(t) (t).begin(),(t).end()
#define FOR(i,n,m) for (int i = n; i <= m; i ++)
#define ROF(i,n,m) for (int i = n; i >= m; i --)
#define RI(x) scanf ("%d", &(x))
#define RII(x,y) RI(x),RI(y)
#define RIII(x,y,z) RI(x),RI(y),RI(z)


typedef long long ll;
typedef unsigned int uint;
typedef unsigned long long ull;

const ll mod = 1e9+7;
const int INF = 1e9;
const double EPS = 1e-8;

/**************************************END************************************/
int N;
priority_queue<int> q;

int main()
{
    freopen("/Users/apple/Desktop/C-small-2-attempt0.in","r",stdin);
    freopen("/Users/apple/Desktop/C-small-2-attempt0.out","w",stdout);
    for(int i=0;i<100;i++);
    
    int T, kase = 1; cin>>T;
    while (T --) {
        int N, k;
        scanf("%d%d", &N, &k);
        while (!q.empty()) q.pop();
        q.push(N);
        for (int i = 0; i < k - 1; i ++) {
            int x = q.top(); q.pop();
            x --;
            if (x & 1) {
                int tmp = x / 2;
                q.push(tmp);
                q.push(x - tmp);
            }
            else {
                q.push(x / 2);
                q.push(x / 2);
            }
        }
        int x = q.top(); q.pop();
        x --;
        int a = x / 2, b = x - a;
        if (a < b) swap(a, b);
        printf("Case #%d: %d %d\n", kase ++, a, b);
    }
    return 0;
}