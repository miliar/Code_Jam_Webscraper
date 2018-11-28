#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <unordered_map>
#include <cstring>
#include <queue>
#include <map>
using namespace std;
typedef long long ll;
const int maxn = 30;

int n,m;
string s[maxn];

int main() {
  freopen("A-large.in","r",stdin);
  freopen("A-large.out","w",stdout);
  int T,ncase=0;
  cin>>T;
  while(T--) {
    cin>>n>>m;
    for(int i=0; i<n; i++)cin>>s[i];
    for(int i=0; i<n; i++)
      for(int j=0; j<m; j++) {
        if(s[i][j]=='?')continue;
        for(int k=i+1; k<n; k++) {
          if(s[k][j]!=s[i][j]&&s[k][j]!='?')break;
          s[k][j]=s[i][j];
        }
      }
    for(int i=n-1; i>=0; i--)
      for(int j=0; j<m; j++) {
        if(s[i][j]=='?')continue;
        for(int k=i-1; k>=0; k--) {
          if(s[k][j]!=s[i][j]&&s[k][j]!='?')break;
          s[k][j]=s[i][j];
        }
      }
    for(int i=0; i<n; i++)
      for(int j=0; j<m; j++) {
        if(s[i][j]=='?')continue;
        for(int k=j+1; k<m; k++) {
          if(s[i][k]!='?'&&s[i][k]!=s[i][j])break;
          s[i][k]=s[i][j];
        }
      }
    for(int i=0; i<n; i++)
      for(int j=m-1; j>=0; j--) {
        if(s[i][j]=='?')continue;
        for(int k=j-1; k>=0; k--) {
          if(s[i][k]!='?'&&s[i][k]!=s[i][j])break;
          s[i][k]=s[i][j];
        }
      }
    cout<<"Case #"<<++ncase<<":"<<endl;
    for(int i=0; i<n; i++)cout<<s[i]<<endl;
  }
  return 0;
}
