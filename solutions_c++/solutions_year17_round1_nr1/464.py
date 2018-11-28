#include<bits/stdc++.h>
#define pb push_back
#define mp make_pair
#define fs first
#define sc second
using namespace std;
int N,T,R,C;
string s[100];
int ok[100];
int l[100][100];

int main() {
  cin.sync_with_stdio(false);
  cin>>T;
  for(int t=1;t<=T;++t) {
    cout<<"Case #"<<t<<":\n";
    cin>>R>>C;
    for(int i=0;i<R;++i) {
      cin>>s[i];
      ok[i] = 0;
      for(int j=0;j<C;++j) {
        if(s[i][j] != '?') {
          ok[i] = 1;
        }
      }
    }
    int lastLine = -1;
    int curr = 0;
    while(!ok[curr]) {
      ++curr;
    }
    
    for(int j=0;j<C;++j) {
      if(s[curr][j] != '?') {
        for(int k=j-1;k>=0;--k) {
          if(s[curr][k] == '?') {
            s[curr][k] = s[curr][j];
          } else break;
        }
        for(int k=j+1;k<C;++k) {
          if(s[curr][k] == '?') {
            s[curr][k] = s[curr][j];
          } else break;
        }
      }
    }
    for(int i=0;i<curr;++i) {
      s[i] = s[curr];
    }
    
    for(int i=curr;i<R;++i) {
      if(!ok[i]) continue; 
      for(int j=0;j<C;++j) {
        if(s[i][j] != '?') {
          for(int k=j-1;k>=0;--k) {
            if(s[i][k] == '?') {
              s[i][k] = s[i][j];
            } else break;
          }
          for(int k=j+1;k<C;++k) {
            if(s[i][k] == '?') {
              s[i][k] = s[i][j];
            } else break;
          }
        }
      }
      
      for(int j=i+1;j<R;++j) {
        if(!ok[j]) {
          s[j] = s[i];
        } else break;
      }
    }
    
    for(int i=0;i<R;++i) {
      cout<<s[i]<<"\n";
    }
  }
  return 0;
}
