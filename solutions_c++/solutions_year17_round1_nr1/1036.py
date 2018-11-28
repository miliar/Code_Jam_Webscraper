#include <bits/stdc++.h>

using namespace std;
char a[30][30];
int main() {
  freopen("inal.in","r",stdin);
  freopen("outal.txt","w",stdout);
  int t,r,c;
  cin>>t;
  for(int test=1;test<=t;test++) {
    cin>>r>>c;
    for(int i=0;i<r;i++){
      for(int j=0;j<c;j++) {
        cin>>a[i][j];
      }
    }

    for(int i=0;i<r;i++){
      for(int j=0;j<c;j++) {
        if(a[i][j]=='?'){
          int k=i-1;
          while(k>=0) {
            if(a[k][j]!='?'){
              a[i][j]=a[k][j];
              break;
            } else {
              k--;
            }
          }
          if(a[i][j]!='?')
            continue;
          k=i+1;
          while(k<r) {
            if(a[k][j]!='?'){
              a[i][j]=a[k][j];
              break;
            } else {
              k++;
            }
          }
        }
      }
    }



    for(int i=0;i<r;i++){
      for(int j=0;j<c;j++) {
        if(a[i][j]=='?'){
          int k=j-1;
          while(k>=0) {
            if(a[i][k]!='?'){
              a[i][j]=a[i][k];
              break;
            } else {
              k--;
            }
          }
          if(a[i][j]!='?')
            continue;
          k=j+1;
          while(k<c) {
            if(a[i][k]!='?'){
              a[i][j]=a[i][k];
              break;
            } else {
              k++;
            }
          }
        }
      }
    }

    cout<<"Case #"<<test<<":"<<endl;
    for(int i=0;i<r;i++){
      for(int j=0;j<c;j++) {
        cout<<a[i][j];
      }
      cout<<endl;
    }

  }
}
