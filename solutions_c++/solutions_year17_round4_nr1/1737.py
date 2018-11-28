//g++ -std=c++14 -g -O2 -o ./a ./A.cpp
#include <bits/stdc++.h>
using namespace std;
#define ff first
#define ss second
#define nl '\n'
typedef long long ll;
//////////////////////////////////////////////////////////////////////



int main(){
  ios::sync_with_stdio(0);cin.tie(0);cout.tie(0);
  int __tc;cin>>__tc;
  for(int __t = 1; __t <= __tc ; __t++){
    cout<<"Case #"<<__t<<": ";

    int n,p;
    cin>>n>>p;
    int x[n+1];
    for(int i=1;i<=n;i++)cin>>x[i];

    if(p==2){
      int odd=0,even=0;
      for(int i=1;i<=n;i++)
	if(x[i]%2)odd++;else even++;
      cout << (even+(odd+1)/2) << nl;
    }else if(p==3){
      int a=0,b=0,c=0;
      for(int i=1;i<=n;i++)
	if(x[i]%3==0)a++;
	else if(x[i]%3==1)b++;
	else c++;
      cout << (a + min(b,c) + (2+abs(c-b))/3) << nl;
    }
    
  }
  return 0;
}
