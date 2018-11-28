#include <iostream>
#include <string>
#include <cstring>
using namespace std;
int main()
{
	ios_base::sync_with_stdio(false);
	bool flag;
	long long x,T,K,ans,i,j;
	string S;
	cin>>T;
	for(x=1;x<=T;x++)
	{
		cin>>S>>K;
		flag=true;
		ans=0;
		for(i=0;i<S.length();i++)
		{
			if(S[i]=='-')
			{
				if(S.length()-i<K)
				{
					flag=false;
					break;
				}
				else
				{
					for(j=i;j<=i+K-1;j++)
						S[j]=(S[j]=='+'?'-':'+');
					ans++;
				}
			}
		}
		if(flag)
		{
			cout<<"Case #"<<x<<": "<<ans<<"\n";
		}
		else
		{
			cout<<"Case #"<<x<<": IMPOSSIBLE\n";
		}
	}
	return 0;
}
