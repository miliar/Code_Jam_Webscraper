#include<bits/stdc++.h>
typedef long long ll;
#define f first
#define s second
#define pb push_back
#define mp make_pair
using namespace std;
int main()
{
	int t;
	scanf("%d",&t);
	int nn=1;
	while(t--)
	{
		string s;
		cin>>s;
		int i=0,n=s.size(),j;
		printf("Case #%d: ",nn);
		nn++;
		if(n==1)cout<<s[0];
		else
		{
			while(s[i+1]>=s[i]&&i<n-1)
			{
				i++;
			}
			if(i==n-1&&s[n-1]>=s[n-2])
			{
				cout<<s;
			}
			else
			{
				j=i;
				while(s[j]==s[i]&&j>=0)j--;
				j++;
				s[j]=s[j]-1;
				i=j;
				for(j=i+1;j<n;j++)s[j]='9';
				if(s[0]!='0')cout<<s[0];
				for(j=1;j<n;j++)cout<<s[j];
			}
		}
		printf("\n");
	}
	return 0;
}