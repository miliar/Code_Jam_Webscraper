#include <bits/stdc++.h>
using namespace std;
#define LL long long
vector<LL>w;
LL a3(LL i){
  LL q=i;
  while(w[q]>=w[q+1] && q>=0){
    if(0==q)return -1;
    q-=1;
  }
  return q+1;
}
int main() {
  LL a5;cin>>a5>>ws;
  string a4;
  for (LL i=1;i<=a5;i+=1) {
    bool a1=false;
    cin>>a4>>ws;
    w.clear();
    for(auto x:a4)w.push_back(x-'0');
    if(1<w.size()){
      for (LL j=w.size()-2;j>=0;j-=1){
        if(w[j+1]<w[j]){
          LL a2=a3(j);
          if(-1==a2){
            a2=0;
            if(1==w[a2])
              a1=true;
          }
          w[a2]--;
          for (LL c=a2+1;c<w.size();c++)w[c]=9;
          if (a1) break;
        }
      }
    }
    cout<<"Case #"<<i<<": ";
    for(LL j=(a1?1:0);j<a4.size();j++)cout<<w[j];
    cout<<endl;
  }
  return 0;
}
