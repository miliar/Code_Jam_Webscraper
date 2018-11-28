#include<bits/stdc++.h>
using namespace std;
#define boost() ios_base::sync_with_stdio(false),cin.tie(0)
#define all(c) c.begin(),c.end()
#define rep(i,c,n) for(i=c;i<n;i++)
#define dw(t) while (t--)
#define PB push_back
#define F first
#define S second
map<int,int> M;
void init(){
  int j,i;
  for(i=1;i<=1000;i++)
  {
    j=i;
    vector<int> v;
    while(j>0)
    {
      v.PB(j%10);
      j/=10;
    }
    for(j=v.size()-1;j>0;j--)
    {
      if(v[j]>v[j-1])
        break;
    }
    if(j==0)
      M[i]=1;
  }
}
int main(){
  boost();
  init();
  int t,n,i;
  cin>>t;
  rep(i,0,t){
    cin>>n;
    while(n){
      if(M[n]==1)
        break;
      n--;
    }
    cout<<"Case #"<<i+1<<": "<<n<<'\n';
  }
  return 0;
}
