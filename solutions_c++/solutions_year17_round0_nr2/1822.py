#include<bits/stdc++.h>
using namespace std;
int t,n,i,j,T;
string a;
bool ok;
int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);

    cin>>t;
    while(t--)
    {
        ok=true;

        cin>>a;
        n=a.size();

        for(i=0;i+1<n;i++) if(a[i]>a[i+1]) {ok=false;break;}

        if(!ok)
        {
            for(j=i;j>=0 and a[j]==a[i];j--) ;
            a[++j]--;
            for(i=j+1;i<n;i++) a[i]='9';
        }

        if(a[0]=='0') a=a.substr(1);

        cout<<"Case #"<<++T<<": "<<a<<"\n";
    }
}
