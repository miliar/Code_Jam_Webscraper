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
   rep(k,t)
    {
        string s;
        int l;
        cin>>s;
        l=s.length();
        for(int i=l-2;i>=0;i--)
        {
            if(s[i]>s[i+1]){
                s[i]=(char)((int)s[i]-1);
                for(int j=i+1;j<l;j++){
                    s[j]='9';
                }
            }
        }
        int f=0;
        string p;
        for(int i=0;i<l;i++){
            if(s[i]=='0')
              f++;
            else break;
        }
        p=s.substr(f,l-f);
        cout<<"Case #"<<k+1<<": "<<p<<"\n";
   }



    return 0;
}
