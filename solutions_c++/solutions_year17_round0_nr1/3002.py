
#include <bits/stdc++.h>
#define fr freopen("input.in","r",stdin);
#define fw freopen("output.txt","w",stdout);
using namespace std;

int main() {
    fr;fw;
	int t,k;
	string s ;

	cin>>t;//to be replaced by file input
	for(int u=1;u<=t;u++)
	{
	    cin>>s>>k;
	    int ans=0,prev=0,flag=0,temp=0;//to be replaced by file input
	    for(int i=0;i<s.size();i++)
        {
            if(s[i]=='-')
            {
                ans++;
                if(i+k>s.size())
                {
                    flag=1;
                    break;
                }
                for(int j=i;j<i+k;j++)
                {
                    if(s[j-1]=='-'&&s[j]=='+')
                        {
                            prev=j-1;
                            break;
                        }
                }
                for(int j=i;j<i+k;j++)
                {
                    if(s[j]=='+')
                        s[j]='-';
                    else
                        s[j]='+';
                }
                i=prev;
            }
            if(flag==1)
                break;
        }

	    if(flag==0)
	    cout<<"Case #"<<u<<": "<<ans<<"\n";
	    else
        cout<<"Case #"<<u<<": IMPOSSIBLE\n";
	}
	return 0;
}
