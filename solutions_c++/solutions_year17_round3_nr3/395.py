#include <bits/stdc++.h>
using namespace std;

#define EPS      1e-9
#define F        first
#define S        second
#define pi       acos(-1)
#define ll       long long
#define inf      0x3f3f3f3f
#define sz(x)    (int)x.size()
#define sc(x)    scanf("%d",&x)
#define all(x)   x.begin(),x.end()
#define rall(x)  x.rbegin(),x.rend()

int T;
int n,k,u;
int arr[55];
string tmp;

int conv(){
  cin>>tmp;
  int res=tmp[0]-'0';
  if(tmp[1]!='.')res=res*10+tmp[1]-'0';
  for(int i=2+(tmp[2]=='.');i<sz(tmp);++i)
    res=res*10+tmp[i]-'0';
  return res;
}

int main() {
#ifndef ONLINE_JUDGE
  //freopen("C-small-1-attempt0.in", "r", stdin);
  freopen("C-small-1-attempt2.in", "r", stdin);
  freopen("out.txt", "w", stdout);
#endif
  sc(T);
  for(int C=1;C<=T;++C){
    sc(n),sc(k);
    u=conv();
    for(int i=0;i<n;++i)
      arr[i]=conv();
    sort(arr,arr+n);
    priority_queue<int> pq;
    for(int i=0;i<n;++i)
      pq.push(-1*arr[i]);
    int cur;
    while(u--){
      cur=pq.top();
      pq.pop();
      pq.push(--cur);
    }
    double out=1;
    while(!pq.empty()){
      out*=(-1*pq.top()/10000.0);
      pq.pop();
    }
    printf("Case #%d: %.9f\n",C,out);
  }
}
