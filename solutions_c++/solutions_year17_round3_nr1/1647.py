//hi~ :)
#include <bits/stdc++.h>
#define X first
#define Y second
#define PB push_back
#define MP make_pair
#define fastio ios::sync_with_stdio(false);cin.tie(0)
using namespace std;
typedef long long ll;
typedef pair<int,int> pii;
typedef pair<ll,ll> pll;
typedef vector<int> vi;
typedef vector<ll> vl;
typedef vector<pii> vii;
typedef vector<pll> vll;

inline ll getint(){
  ll _x=0,_tmp=1; char _tc=getchar();    
  while( (_tc<'0'||_tc>'9')&&_tc!='-' ) _tc=getchar();
  if( _tc == '-' ) _tc=getchar() , _tmp = -1;
  while(_tc>='0'&&_tc<='9') _x*=10,_x+=(_tc-'0'),_tc=getchar();
  return _x*_tmp;
}
bool _cmp(const pair<int,int>&i, const pair<int,int>&j){
  return ((i.first == j.first) ? (i.second>j.second) : (i.first<j.first));
} //x increase, y decrease
struct Node{
  int x, y;
  Node(int a=0, int b=0):
    x(a), y(b){}
  bool operator < (const Node& a)const{
    return ((x==a.x) ? (y>a.y) : (x<a.x));
  }//x increase, y decrease
};

const int mxn = 1e0 + 1;
double eps = 1e-9;
typedef long double lb;
ll ncase = 1;
ll N,M,a,b,c,K;
string str;

vll in;
ll dp[1005][1005];

void pre(){
  return;
}
void init(){
  in.clear();
  memset(dp, 0, sizeof(dp));
  cin >> N >> K;
  for(int i=0;i<N;i++){
    cin >> a >> b;
    in.PB(MP(a,b));
  }
}
void sol(){
  sort(in.begin(), in.end(), greater<pll>());
  a = dp[0][0] = in[0].X * in[0].X+((in[0].X*in[0].Y)<<1);
  for(int i=1;i<N;i++){
    dp[i][0] = max(dp[i-1][0], in[i].X * in[i].X+((in[i].X*in[i].Y)<<1));
    a = max(a, dp[i][0]);
  }
  for(int i=1;i<N;i++){
    for(int j=1;j<K;j++){
      if(j>i) break;
      dp[i][j] = max(dp[i-1][j], dp[i-1][j-1] + ((in[i].X*in[i].Y)<<1));
      a = max(a, dp[i][j]);
    }
  }
  return ;
}

int main(){
  pre();
  cin >> ncase;
  //long double x = acos(-1);
  //cout << fixed << setprecision(9) << x << endl;
  for(int I=1;I<=ncase;I++){
    cout << "Case #" << I << ": " ;
    init();
    sol();
    lb ans = acos(-1);
    ans *= a;
    cout << fixed << setprecision(9) << ans << endl;
  }
}
