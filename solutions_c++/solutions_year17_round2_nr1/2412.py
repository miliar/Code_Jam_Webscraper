#include <stdio.h>
#include <vector>  
#include <cstdio>
#include <iostream>
#include <algorithm>
#include <cstdlib>
#include <map>
#include <cstring> 
#include <queue>   
#include <list>
#include <climits>


#define pb push_back
#define pp pop_back
#define sz(a) (int)(a.size())
#define mp make_pair
#define F first
#define S second
#define next _next
#define prev _prev
#define left _left
#define right _right
#define y1 _y1
#define all(x) x.begin(), x.end()
#define tr(c,i) for(typeof((c).begin()) i = (c).begin();i!=(c).end();i++)

using namespace std;

typedef long long ll;
typedef unsigned long long ull;
typedef long double ld;
typedef pair<int, int> pii;
typedef pair<ll, ll> pll;

const int N = (int)1e5 + 123;
const ll INF = (ll)1e18 + 123;
const int inf = (int)1e9 + 123;
const int MOD = (int)1e9 + 7;

int main() {
  int d,n,t,c=1;
  scanf("%d",&t);
  while(t--) {
    scanf("%d%d",&d,&n);
    double maxTime  = 0.0;
    while(n--) {
      double dd,ss;
      scanf("%lf%lf",&dd,&ss);
      if(((d-dd)/ss)>maxTime) maxTime=(d-dd)/ss;
    }
    double ans = (double)d/maxTime;
    printf("Case #%d: %lf\n",c++,ans);
  }
  return 0;
}