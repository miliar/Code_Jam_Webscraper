
#include <bits/stdc++.h>
using namespace std;
#define MOD 1000000007
#define pii pair<int, int>
#define pll pair<long long, long long>
#define V  vector
#define pb  push_back
#define mp  make_pair
#define pq priority_queue
#define FIN(x) freopen(x,"r",stdin)
#define FOUT(x) freopen(x,"w",stdout)
#define ALL(x) x.begin(),x.end()
#define M(a,x) memset(a,x,sizeof(a))
#define S(x) scanf("%d",&x)
#define Sl(x) scanf("%lld",&x)
#define scs(x) scanf("%s",x);
#define SZ(x) (int)x.size()
#define print(x) printf("%d",x);
#define nl printf("\n")
#define fr first
#define se second
#define printl(x) printf("%lld",x)
#define F(i,a,n) for(int i=a;i<n;i++)
#define INF 4000000000000000000LL
#define LL long long

const int N = 1e5+5;
string s;
int k;
void flip(int idx) {
  for(int i = 0 ; i < k ; i++) {
    if(s[idx+i] == '+') {
      s[idx+i] = '-';
    }
    else {
      s[idx+i] = '+';
    }
  }
}
bool valid() {
  for(int i = 0 ; i < s.size() ; i++) {
    if(s[i] != '+') return false;
  }
  return true;
}
int cs = 0;
int main() {
  FIN("lg.in");
  FOUT("lg.out");
  int t;
  S(t);
  while(t--) {
    cin >> s;
    cin >> k;
    int ans = 0;
    int i = 0 , j = s.size()-1;
    while(j-i+1 >= k) {
      if(s[i] == '-') {
	ans++;
	flip(i);
      }
      if(s[j] == '-') {
	ans++;
	flip(j-k+1);
      }
      i++;
      j--;
    }
    if(!valid()) {
      printf("Case #%d: IMPOSSIBLE\n",++cs);
    }
    else {
      printf("Case #%d: %d\n",++cs,ans);
    }
  }
}
