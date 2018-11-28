#include <bits/stdc++.h>

using namespace std;

int main()
{
      freopen("br.in","r",stdin);
    freopen("low.txt","w",stdout);
    int t;
    int ca=0;
    unsigned long long n,k,l,a,b;
        vector<unsigned long long> v;
    cin>>t;
    while(t--){
            ca++;
       v.clear();
        cin>>n>>k;
        v.push_back(n);
        for(int i=0;i<k;i++){
            sort(v.begin(),v.end());
             l= v[v.size()-1];
            if(i==k-1){
               if(l%2){
                a=l/2;
                b=l/2;
               }
               else{
                a=l/2-1;
                b=l/2;
               }
               break;
            }
           if(l%2){
            v[v.size()-1]=l/2;
            v.push_back(l/2);
           }
           else{
            v[v.size()-1]=l/2;
            v.push_back(l/2-1);
           }
        }
       cout<<"Case #"<<ca<<": ";
        cout<<b<<" "<<a<<endl;

    }
    return 0;
}
