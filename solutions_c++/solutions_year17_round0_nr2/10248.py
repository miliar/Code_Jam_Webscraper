#include <bits/stdc++.h>
using namespace std;
typedef long long int ll;
int main()
{
    freopen("input.in","r",stdin);
    freopen("output.txt","w",stdout);
   int tt,j=1;
   cin>>tt;
   while(tt--)
   {
       ll n;
       cin>>n;
       for(ll i=n; ; i--)
       {
           string s;
           ll nn=i;
            while(nn)
            {
                s+=(nn%10)+'0';
                nn=nn/10;
            }
            reverse(s.begin(),s.end());
            string rv=s;
            sort(rv.begin(),rv.end());

            if(rv==s)
            {
                 cout<<"Case #"<<j++<<": ";
                cout<<s<<endl;
                break;
            }
       }
   }
}
