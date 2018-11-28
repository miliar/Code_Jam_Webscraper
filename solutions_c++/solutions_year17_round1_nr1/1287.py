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
  
  int tc;cin>>tc;
  for(int tt=1;tt<=tc;tt++){
    int r,c;
    cin>>r>>c;
    char a[r+1][c+2];
    for(int i=1;i<=r;i++)cin>>1+a[i];

    for(int i=1;i<=r;i++)
      for(int j=1;j<=c;j++)
	if(a[i][j]!='?'){
	  for(int k=i+1;k<=r and a[k][j]=='?';k++)a[k][j]=a[i][j];
	  for(int k=i-1;k>=1 and a[k][j]=='?';k--)a[k][j]=a[i][j];
	}
    
    for(int j=1;j<=c;j++)
      if(a[1][j]!='?'){
	for(int k=j-1;k>=1 and a[1][k]=='?';k--)
	  for(int i=1;i<=r;i++)a[i][k]=a[i][j];
	for(int k=j+1;k<=c and a[1][k]=='?';k++)
	  for(int i=1;i<=r;i++)a[i][k]=a[i][j];
      }

    cout<<"Case #"<<tt<<": \n";
    for(int i=1;i<=r;i++){
      for(int j=1;j<=c;j++)cout<<a[i][j];
      cout<<nl;
    }
  }
  
  return 0;
}
