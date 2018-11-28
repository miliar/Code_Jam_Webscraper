//phi

#include <bits/stdc++.h>

#define iOS ios::sync_with_stdio(false)

#define M 1000000007

#define tp4 10000
#define tp5 100000
#define tp6 1000000
#define tp7 10000000
#define tp8 100000000
#define tp9 1000000000

#define ll long long
#define pb push_back
#define mp make_pair
#define ff first
#define ss second
#define sd(x) scanf("%d",&x)
#define sc(x) scanf("%c",&x)

using namespace std;

int main()
{
	int t,test;

	cin>>test;

	int k;
	string s;

	for(t=1;t<=test;t++)
	{
		cin>>s;
		cin>>k;

		int l=s.length();
		int imp=0;
		int ans=0;
		for(int i=0;i<l;i++)
		{
			if(s[i]=='-')
			{
				if((i+k)>l)
				{
					//cout<<i<<" "<<s<<endl;
					imp=1;
					break;
				}

				ans++;
				for(int j=i;j<i+k;j++)
				{
					if(s[j]=='-') s[j]='+';
					else s[j]='-';
				}

				//cout<<s<<endl;
			}

		}

		if(imp)
			cout<<"Case #"<<t<<": "<<"IMPOSSIBLE"<<endl;
		else
			cout<<"Case #"<<t<<": "<<ans<<endl;

	}

	return 0;
}
/*
3
---+-++- 3
+++++ 4
-+-+- 4
*/
