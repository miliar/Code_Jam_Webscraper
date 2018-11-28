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
ll ncase = 1;
ll N,K,cnt;
map<ll,ll, greater<ll> > arr;
pll ans;

void pre(){
  return;
}

void init(){
  N = getint();
  K = getint();
}
void sol(){
  arr.clear();
  arr[N] = 1;
  for(auto i : arr){
    K -= i.Y;
    if(K <= 0){
      ans = MP((i.X -1)>>1, (i.X)>>1);
      return ;
    }
    arr[((i.X)-1)>>1] += i.Y;
    arr[(i.X)>>1] += i.Y;
  }
}

int main(){
  pre();
  ncase = getint();
  for(int I=1;I<=ncase;I++){
    init();
    sol();
    cout << "Case #" << I << ": " << ans.Y << " " << ans.X << endl;
  }
}
