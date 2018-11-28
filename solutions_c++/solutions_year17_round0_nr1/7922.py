#include<bits/stdc++.h>
using namespace std;
typedef long long int ll;
int main()
{
	cin.tie(NULL);
	freopen("A-large (2).in","r",stdin);
	freopen("out.txt","w",stdout);
	ll t,n;
	string s;
	cin>>t;
	for(int test=1;test<=t;test++)
    {
        cin>>s>>n;
        ll re=0;
        for(int i=0;i<=s.size()-n;i++)
        {
            if(s[i]=='-')
            {
                for(int j=i;j<i+n;j++)
                {
                    if(s[j]=='-')
                        s[j]='+';
                    else
                        s[j]='-';
                }
                re++;
            }
        }
        //cout<<s<<" ";
        int flag=1;
        for(int i=0;i<s.size();i++)
        {
            if(s[i]=='-')
            {
                flag=0;
            }
        }
        if(flag==1)
            cout<<"Case #"<<test<<": "<<re<<"\n";
        else
            cout<<"Case #"<<test<<": IMPOSSIBLE"<<"\n";
    }
	return 0;
}
