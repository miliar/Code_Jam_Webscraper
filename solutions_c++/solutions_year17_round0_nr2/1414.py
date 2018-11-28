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
ll N,M,a,b,c;
string str;
vector<int> arr, ans;

void pre(){
  return;
}
void init(){
  arr.clear();
  ans.clear();
  N = getint();
}
void sol(){
  while(N){
    arr.PB(N%10);
    N/=10;
  }
  reverse(arr.begin(), arr.end());
  bool flag = 0;
  for(int i=0;i<arr.size();i++){
    if(flag){
      ans.PB(9);
      continue;
    }
    if(i+1<arr.size() and arr[i] > arr[i+1]){
      flag = 1;
      ans.PB(arr[i]-1);
    }
    else
      ans.PB(arr[i]);
  }
  reverse(ans.begin(), ans.end());
  for(int i=0;i+1<ans.size();i++){
    if(ans[i]<ans[i+1]){
      ans[i] = 9;
      ans[i+1] --;
    }
  }
  while(ans.back() == 0) ans.pop_back();
  reverse(ans.begin(), ans.end());
  return ;
}

int main(){
  pre();
  ncase = getint();
  for(int I=1;I<=ncase;I++){
    init();
    sol();
    cout << "Case #" << I << ": ";
    for(auto x : ans)cout << x;
    cout << endl;
  }
}
