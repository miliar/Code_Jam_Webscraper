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

int T, n, k, cnt, p1, p2;
ii test;
multiset<ii> bath;

int main ()
{

//  in;
  freopen("C-small-2-attempt0.in", "r", stdin);
  freopen("output.txt", "w", stdout);

  cin >> T;
  for(int i=1; i<=T; i++){
    cnt = 0;
    bath.clear();
    cin >> n >> k;
    if(n&1)
      p1 = p2 = n/2;
    else{
      p1 = n/2;
      p2 = (n/2)-(p1>0);
    }
    bath.insert({-max(p1, p2), -min(p1, p2)});
    cnt++;
    while(cnt<k){
      test = *bath.begin();
//      cout << -test.a << " " << -test.b << endl;
      bath.erase(bath.begin());
      if(-test.a&1)
        p1 = p2 = -test.a/2;
      else{
        p1 = -test.a/2;
        p2 = (-test.a/2)-(p1>0);
      }
      bath.insert({-max(p1, p2), -min(p1, p2)});
      if(-test.b&1)
        p1 = p2 = -test.b/2;
      else{
        p1 = -test.b/2;
        p2 = (-test.b/2)-(p1>0);
      }
      bath.insert({-max(p1, p2), -min(p1, p2)});
      cnt++;
    }
    test = *bath.begin();
//    for(auto A: bath)
//      cout << -A.a << " " << -A.b << endl;
    printf("Case #%d: %d %d\n", i, -test.a, -test.b);
  }

  return 0;
}
