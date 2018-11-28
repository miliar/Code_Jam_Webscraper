#include<bits/stdc++.h>
using namespace std;

int main()
{
	int T,K,cnt,flips,c=1;
	vector<bool> v;
	string cur;
	char S[1005];
	scanf("%d",&T);
	while(T--)
	{
		scanf("%s",&S[0],sizeof S);
		scanf("%d",&K);
	
		cur=S;
		cnt=0;
		flips=0;
		v.clear();
		for(int i=0;i<cur.length();i++)
		{
			if(cur.at(i)=='+')
			{
				cnt++;
				v.push_back(true);
			}
			else 
			v.push_back(false);
		}
		if(cnt!=cur.length())		
		for(int i=0;i<=cur.length()-K;i++)
		{
			if(!v[i])
			{
				flips++;
				for(int j=i;j<i+K;j++)
				{
					if(v[j])cnt--;
					else cnt++;
					
					v[j]=!v[j];
				}
			}
			
		}
		printf("Case #%d: ",c);
		if(cnt!=cur.length())printf("IMPOSSIBLE\n");
		else printf("%d\n",flips);
		c++;
	}
	return 0;
}