#include <bits/stdc++.h>
#define pb push_back
using namespace std;
vector<int> v,k;
vector<int> misa(int u){
    for(int i=u;i>=0;--i){
        int mi=i;
        while(mi>0){
           v.pb(mi%10);
           mi=mi/10;
         }
           k=v;
           sort(k.begin(),k.end());
           reverse(k.begin(),k.end());
           if(v==k){
             return v;
           }
           v.clear(); k.clear();
    }
}
int main()
{
    freopen("B-small-attempt1.in","r",stdin);
    freopen("misael.txt","w",stdout);
    int a,b,c;
    cin>> a;
    for(int i=0;i<a;++i){
      cin>> b;
      vector<int>w = misa(b);
      cout<<"Case #"<<i+1<<": ";
      for(int s=w.size()-1;s>=0;--s){
          cout<<v[s];
       }
       cout<<endl;
       v.clear(); k.clear();
    }

}
