#include<bits/stdc++.h>
using namespace std;

int main() {
freopen("X.txt","r",stdin);
freopen("out.txt","w",stdout);

	int T,k;
	cin>>T;
	int u=1;
	//cout<<T<<endl;
	while(T--)
	{
			string s;
			cin>>s>>k;
			cout<<"Case #"<<u<<": ";
			u+=1;
			int i,j,ans=0;
			for(i=0;i<s.size();i++)
			{
				if(i+k>s.size())
					break;
				if(s[i]=='-')
				{ ans++;
						for(j=0;j<k;j++)
						{
							if(s[i+j]=='-')
								s[i+j]='+';
							else
								s[i+j]='-';
						}
				}

			}
			for(i=0;i<s.size();i++)
			{
				if(s[i]=='-')
			{
					ans=-1;
					break;
			}
			}
			if(ans==-1)
			{
				cout<<"IMPOSSIBLE"<<endl;
			}
			else
			{
				cout<<ans<<endl;
			}
	}

return 0;
}
