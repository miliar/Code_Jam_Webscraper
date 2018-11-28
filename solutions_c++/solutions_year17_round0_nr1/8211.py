#include <bits/stdc++.h>
#define INF 1000000007
#define in cin.sync_with_stdio(0);cin.tie(0);
#define PI 3.14159265358979323846
#define clr(v,d) memset(v,d,sizeof(v))
#define all(v) v.begin(),v.end()
#define sz(v) (int)v.size()
#define mp make_pair
#define pb push_back
#define a first
#define b second

using namespace std;

typedef long long ll;
typedef pair<int,int> ii;

int T, k, R;
bool f = 1;
string s;

int main ()
{

  //in;
  freopen("A-large.in", "r", stdin);
  freopen("output.txt", "w", stdout);

  cin >> T;
  for(int i=1; i<=T; i++){
    R = 0;
    f = 1;
    cin >> s >> k;
    for(int i=0; i<sz(s)-k+1; i++){
      if(s[i] == '-'){
        R++;
        for(int j=i; j<i+k; j++) s[j] = (s[j]=='-'? '+': '-');
      }
    }
    for(int i=sz(s)-k+1; i<sz(s); i++){
      if(s[i]=='-') f = 0;
    }
    if(f) printf("Case #%d: %d\n", i, R);
    else printf("Case #%d: IMPOSSIBLE\n", i);
  }

  return 0;
}
