#include<bits/stdc++.h>
using namespace std;

#define fi first
#define se second
#define mp make_pair
#define pb push_back

typedef long long ll;
typedef pair<int,int> ii;
typedef vector<int> vi;
typedef long double ld;
typedef set<int>::iterator sit;
typedef map<int,int>::iterator mit;
typedef vector<int>::iterator vit;

int main()
{
   int t;
   cin>>t;
    for(int u=1;u<=t;u++)
   {
       string s;
       int k;
       cin>>s>>k;
       int ans=0;
       for(int i=0;i<=s.length()-k;i++)
        {
            if(s[i]=='-')
            {
               ans++;
               for(int j=i;j<=i+k-1;j++)
               {
                   if(s[j]=='+')
                    s[j]='-';
                   else
                    s[j]='+';
               }
            }
        }
        int f=0;
        for(int i=0;i<s.length();i++)
        {
            if(s[i]=='-')
                f=1;
        }
        cout<<"Case #"<<u<<": ";
        if(f==1)
            cout<<"IMPOSSIBLE"<<endl;
        else
            cout<<ans<<endl;
   }
    return 0;
}
