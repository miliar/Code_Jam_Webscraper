#include<bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef pair<int,int> pii;
typedef vector<int> vi;
typedef map<int,int> mii;


int t,n,m,x,y;
string s;

int main()
{
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout); 

	scanf("%d",&t);
	for(int tc=1;tc<=t;tc++)
	{
		cin>>s;
		printf("Case #%d: ",tc);

		for(int i=0;i<s.size()-1;i++)
		{
			if(s[i]>s[i+1])
			{
				int j=i;
				while(j>=0&&s[j]==s[i])
				{
					j--;
				}
				s[j+1]=s[j+1]-1;
				for(int k=j+2;k<s.size();k++)
				{
					s[k]='9';
				}
				break;
			}
		}
		int i=0;
		while(s[i]=='0')
		{
			i++;
		}
		for(;i<s.size();i++)
		{
			printf("%c",s[i]);
		}
		printf("\n");
		
	}
	return 0;	
}