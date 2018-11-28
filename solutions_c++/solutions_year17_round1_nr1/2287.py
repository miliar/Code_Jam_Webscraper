#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <string>
#include <vector>
#include <iostream>
#include <map>
#include <set>
#include <algorithm>
#include <queue>
#include <sstream>
using namespace std;
typedef long long ll;
typedef pair<int,int> pii;
#define SZ(x) (int)(x.size())
#define F0(i,n) for(int i=0;i<n;i++)
#define F1(i,n) for(int i=1;i<=n;i++)
ll gcd(ll x, ll y) { return y ? gcd(y, x%y) : x; }

int i, j, k, m, n, l,r,c;

int main() {
  freopen("A-large.in", "r", stdin);
  freopen("A-large.out", "w", stdout);
  
  //freopen("C-large-practice.in", "r", stdin);
  //freopen("C-large-practice.out", "w", stdout);
  vector<char> rows(26);
  vector<char> cols(26);
  int tt, tn;
  cin >> tn;
  F1(tt,tn) {
    cin>>r>>c;
    vector<vector<char> > myM(26,vector<char>(26));
    rows.clear();
    cols.clear();
    F1(i,r){
      F1(j,c){
        cin>>myM[i][j];
      }
    }
    F1(i,r){
      F1(j,c){
        if(myM[i][j] !='?'){
          k=1;
          while(((j+k)<=c) && (myM[i][j+k]=='?')){
            myM[i][j+k]=myM[i][j];k++;
          }
          k=1;
          while(((j-k)>=0) && (myM[i][j-k]=='?')){
            myM[i][j-k]=myM[i][j];k++;
          }
        }
      }
    }
    F1(j,c){
      F1(i,r){
        if(myM[i][j] !='?'){
           k=1;
          while(((i+k)<=r) && (myM[i+k][j]=='?')){
            myM[i+k][j]=myM[i][j];k++;
          }
          k=1;
          while(((i-k)>=0) && (myM[i-k][j]=='?')){
            myM[i-k][j]=myM[i][j];k++;
          }
        }
      }
    }
    
    printf("Case #%d:\n",tt);
    F1(i,r){
      F1(j,c){
        cout<<myM[i][j];
      }
      cout<<endl;
    }
 }
 return 0;
}
