#include<bits/stdc++.h>
using namespace std;
#define ll                  long long
#define rep(i,n)            for(ll i=0;i<n;i++)
#define hell                1000000007LL
#define vi                  vector<ll>
#define vii                 vector< vi >
#define pb                  push_back
#define mp                  make_pair
#define fi                  first
#define se                  second
#define pii                 pair<int,int>
#define all(c)              c.begin(),c.end()
#define mini(c)             min_element(all(c))
#define maxi(c)             max_element(all(c))
int main()
{
   int t;
   cin>>t;
   rep(j,t)
    {
        string s;
        int k,c=0,l;
        cin>>s>>k;
        l=s.length();
        rep(i,l-k+1)
        {
            if(s[i]!='+'){
                c++;
                rep(z,k){
                    s[i+z]=(s[i+z]=='+')? '-':'+';
                }
            }
        }
        int f=1;
        for(int i=l-k+1;i<l;i++){
            if(s[i]=='-')
              {f=0;  break;}
        }
            if(f==0)cout<<"Case #"<<j+1<<": IMPOSSIBLE\n";
            else cout<<"Case #"<<j+1<<": "<<c<<"\n";
   }



    return 0;
}
