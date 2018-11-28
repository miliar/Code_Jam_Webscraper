#include <bits/stdc++.h>

using namespace std;

int main()
{
    freopen("input.in","r",stdin);
	freopen("op.txt","w",stdout);
	int t;cin>>t;
	int x=1;
	while(t--)
	{
	    cout<<"Case #"<<x<<": ";
	    x++;
		string s;cin>>s;
        int k,c=0;cin>>k;
        for(int i=0;i<=s.length()-k;i++)
        {
            if(s[i]=='-')
            {
                c++;
                for(int j=i;j<i+k;j++)
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
            {
                f=1;
                break;
            }
        }
        if(f==0)
            cout<<c<<"\n";
        else
            cout<<"IMPOSSIBLE\n";
    }
    return 0;
}
