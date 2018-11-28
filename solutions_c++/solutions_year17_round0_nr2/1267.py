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
const int maxn = 105;

int main() {
  //freopen("in.cpp","r",stdin);
  freopen("B-large.in","r",stdin);
  freopen("B.l.out","w",stdout);
  int T,ncase=0;
  cin>>T;
  while(T--) {
    ll n;
    cin>>n;
    vector<int>v;
    while(n) {
      v.push_back(n%10);
      n/=10;
    }
    ll ret=0;
    for(int i=v.size()-1; i>=0; i--) {
      bool sign=0;
      for(int j=i-1; j>=0; j--) {
        if(v[j]>v[i])break;
        if(v[j]<v[i]) {
          sign=1;
          break;
        }
      }
      if(sign) {
        ret=ret*10+v[i]-1;
        for(int j=i-1; j>=0; j--)ret=ret*10+9;
        break;
      } else {
        ret=ret*10+v[i];
      }
    }
    cout<<"Case #"<<++ncase<<": "<<ret<<endl;
  }
  return 0;
}
