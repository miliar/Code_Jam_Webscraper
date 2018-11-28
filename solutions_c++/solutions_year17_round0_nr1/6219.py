#include <bits/stdc++.h>
using namespace std;
#define ll long long
#define sc(a) scanf("%d",&a)
#define scl(a) scanf("%lld",&a)
#define pb(a) push_back(a)
typedef vector<int> vi;
int main()
{
	int t;
	sc(t);
	int tc=1;
	while(tc <= t)
	{
		int n,k;
		string s;
		cin>>s;	sc(k);
		
		int len=s.length();
		
		int count=0;
		for(int i=0;i<=len-k;i++)
		{
			if(s[i]=='-')
			{
				count++;
				int j=0;
				while(i+j<len && j<k)
				{
					if(s[i+j]=='-')
						s[i+j]='+';
					else
						s[i+j]='-';
					j++;
				}
			}

		}
		bool flag=true;
		for(int i=0;i<len;i++)
			if(s[i]=='-'){
				flag=false;
				break;
			}

		cout<<"Case #"<<tc++<<": ";
		if(!flag)
			cout<<"IMPOSSIBLE";
		else
			cout<<count;
		cout<<endl;
	}
	return 0;
}