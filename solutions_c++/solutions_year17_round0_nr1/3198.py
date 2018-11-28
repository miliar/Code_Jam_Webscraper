#include<bits/stdc++.h>
#include<climits>
using namespace std;

bool check;
int n,k;

int func(string s)
{
		int i=0,j,count=0,marker;
		while(i<n)
		{
			marker=k;
			while(i<n && s[i]=='+')
			i++;
			if(i+k-1>=n)
			break;
			count++;
			s[i]='+';
			for(j=1;j<k;j++)
			if(i+j<n)
			{
				if(s[i+j]=='+')
				{
				if(marker==k)
				marker=j;
				s[i+j]='-';
				}
				else
				s[i+j]='+';
			}
			i+=marker;
		}
		i=n-k;
		while(i<n-1)
		if(s[i]!=s[i+1])
		{
			break;
		}
		else
		i++;
		if(i==n-1)
		{
			check=true;
			if(s[n-1]=='-')
			count++;
			return count;
		}
		return INT_MAX;
}

int main()
{
	int t,ans1,ans2;
	string s;
	freopen("A-large.in","r",stdin);
	freopen("output2.out","w",stdout);
	scanf("%d",&t);
	for(int testcase=1; testcase<=t; testcase++)
	{
		printf("Case #%d: ",testcase);
		check=false;
		cin>>s;
		n=s.length();
		scanf("%d",&k);
		ans1=func(s);
		reverse(s.begin(),s.end());
		ans2=func(s);
		if(!check)
		printf("IMPOSSIBLE\n");
		else
		printf("%d\n",min(ans1,ans2));
	}
	return 0;
}
