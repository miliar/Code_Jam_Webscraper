#include <iostream>
#include <vector>
#include <cmath>

using namespace std;

int main() {
  int t;
  long long n,p;
  cin >> t;
  for (int i = 1; i <= t; ++i) {
        cin>>n;
        p=n;
    vector<int> v;
    int l=0,m=0;
  long long k=1,lastk;
 // if(n>=10){
    while(k<=n){
        int r=p%10;
        v.push_back(r);
        p=(p-r)/10;
        k=k*10;
        ++l;
        lastk=k;

    }
    while(m<l){
        k=k/10;

        if(v[l-m-1]==v[l-m-2]){
                if((v[l-m-2]>v[l-m-3])&&((l-m)>2)){
                        n=n-(n%(lastk/10))-1;
                        break;
                }
        }
        if((v[l-m-1]>v[l-m-2])&&((l-m)>1)){n=n-(n%k)-1;break;}
        m++;
    }
    //}
    cout << "Case #" << i << ": " <<n<< endl;
    v.clear();
    }
  return 0;
}
