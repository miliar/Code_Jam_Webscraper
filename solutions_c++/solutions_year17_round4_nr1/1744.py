#include <bits/stdc++.h>
using namespace std;
#define sc(a) scanf("%d", &a)
#define sc2(a, b) scanf("%d%d", &a, &b)
#define sc3(a, b, c) scanf("%d%d%d", &a, &b, &c)
#define scs(a) scanf("%s", a)
#define pri(x) printf("%d\n", x)
#define prie(x) printf("%d ", x)
#define mp make_pair
#define pb push_back
#define BUFF ios::sync_with_stdio(false);
#define db(x) cerr << #x << " == " << x << endl
typedef long long int ll;
typedef long double ld;
typedef pair<int, int> ii;
typedef vector<int> vi;
typedef vector<vector<int> > vvi;
typedef vector<ii> vii;
typedef vector< vii> vvii;
const int INF = 0x3f3f3f3f;
const ll LINF = 0x3f3f3f3f3f3f3f3fll;
const ld pi = acos(-1);
int n,p;
int mapa[5];
int simula(vi &v){
  int r=0;
  int ret=0;
  for(int x: v){
    if(r==0) ret++;
    r+=x;
    r%=p;
  }
  return ret;
}
int solve2()
{
  vi v;
  for(int i=0;i<n;i++) {
    int x;
    cin>>x;
    mapa[x%2]++;
  }
  while(mapa[0]>0) {v.pb(0); mapa[0]--;}
  while(mapa[1]>0) {v.pb(1); mapa[1]--;}
  cout<<simula(v)<<endl;
}
int solve3()
{
  vi v;
  for(int i=0;i<n;i++){
    int x;
    cin>>x;
    mapa[x%3]++;
  }
  while(mapa[0]>0) {v.pb(0); mapa[0]--;}
  int x=min(mapa[1],mapa[2]);
  while(x>0){
    v.pb(1);
    v.pb(2);
    x--;
    mapa[1]--;
    mapa[2]--;
  }
  while(mapa[2]>0) {v.pb(2); mapa[2]--;}
  while(mapa[1]>0) {v.pb(1); mapa[1]--;}
  cout<<simula(v)<<endl;
}
void solve()
{
  cin>>n>>p;
  memset(mapa,0,sizeof(mapa));
  if(p==2) solve2();
  if(p==3) solve3();
  //if(p==4) solve4();
}
int main()
{
  int t;
  cin>>t;
  for(int i=1;i<=t;i++){
    cout<<"Case #"<<i<<": ";
    solve();
  }
  return 0;
}
