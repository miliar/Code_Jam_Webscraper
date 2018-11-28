#include <bits/stdc++.h>
using namespace std;

int main(){
    freopen("input2.in","r",stdin);
    freopen("output2.out","w",stdout);
    int t;
    cin>>t;
    int cas=1;
    while(t--){
    long long d,n;
    cin>>d>>n;
    double a[n];
    for(int i = 0;i<n;i++){
      long long s,w;
      cin>>w;
      cin>>s;
      a[i] = (d - w)/s;
    }
    double max_s = 0;
    for(int i = 0;i<n;i++){
      if(max_s<a[i])
      {
          max_s = a[i];
      }
    }
    double ans = d/max_s;
    std::cout << std::fixed;
    std::cout << std::setprecision(6);
    cout<<"Case #"<<cas<<": "<<ans<<endl;
    cas++;
    }
}

