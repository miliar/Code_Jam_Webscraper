#include "bits/stdc++.h"

using namespace std;

#define ll long long int
#define FOR(i,a,b) for(ll i=a;i<b;i++)
#define NFOR(i,a,b) for(ll i=a;i>b;i--)
#define sz(a) int((a).size())
#define all(c) c.begin(),c.end()
#define find(c, x) (c.find(x)!=c.end())
#define tr(c,i) for(typeof((c).begin() i=(c).begin();i!=(c).end();i++)
#define pb push_back
#define mp make_pair
#define boost ios_base::sync_with_stdio(false); cin.tie(0); cout.tie(0);
#define Mod 1000000007

int main()
    {
        freopen("B-large.in","r", stdin);
        freopen("B-output2.txt","w",stdout);
        ll t;
        cin>>t;
        ll ptr=1;
        while(ptr<=t)
            {
                cout<<"Case #"<<ptr<<": ";
                string s;
                cin>>s;
                ll sz=s.size();
                bool f=0;
                ll index=0;
                FOR(i,1,sz)
                    if(s[i]<s[i-1])
                        { f=1; index=i-1; break;}

                while(s[index]==s[index-1]&&index>-1)
                    index--;

                if(!f) cout<<s;
                else
                    {
                     s[index]--;
                     FOR(i,index+1,sz)
                        s[i]=9+'0';
                     if((s[0]-'0')!=0) cout<<s[0];
                     FOR(i,1,sz)
                        cout<<s[i];
                    }
                ptr++;
                cout<<endl;

            }
        return 0;
    }
