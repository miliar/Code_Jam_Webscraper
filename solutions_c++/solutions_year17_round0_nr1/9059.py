#include <bits/stdc++.h>
#define rep(i,n) for(int i=0;i<n;++i)
#define repp(i,a,b) for(int i=a;i<b;++i)
using namespace std;
typedef long long int ll;

int main() 
{

freopen("input","r",stdin);
freopen("o","w",stdout);

int x;
cin>>x;

for(int no=1;no<=x;no++)
{
cout<<"Case #"<<no<<": ";
    
    int k;
    string s;
    cin>>s;
    cin>>k;
    
    int c=0;
    rep(i,s.length())
    {
        if(s[i]=='-' && i+k<s.length()+1)
        {
            c++;            
            repp(j,i,i+k)
            {
                if(s[j]=='-')
                    s[j]='+';
                else
                    s[j]='-';
            }
        }
    }
    
    int flag=0;
    rep(i,s.length())
        if(s[i]=='-')
            flag=1;

    if(flag)
        cout<<"IMPOSSIBLE"<<endl;
    else
        cout<<c<<endl;
}    
return 0;
}