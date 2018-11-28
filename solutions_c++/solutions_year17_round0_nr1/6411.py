#include<bits/stdc++.h>
using namespace std;

int makeHappySUp(char cake[],int k)
{
	int ans = 0;
	for(int i =0;i<strlen(cake);i++)
	{
		if(cake[i]=='-')
		{
			if(i<(strlen(cake)-k+1))
			{
				ans++;
				for(int j =i;j<i+k;j++)
				{
					if(cake[j]=='+')
					cake[j]='-';
					else
					cake[j] = '+';		
				}
				//printf("cur cake: %s\n",cake);	
			}
			else
			{
				return -1;
			}
		}
	}
	return ans;
}
int main()
{
	int t,c(1);
	cin>>t;
	while(c<=t)
	{
		string cake;
		int k;
		cin>>cake>>k;
		//cout<<cake<<" "<<k<<endl;
		int ans = makeHappySUp((char *)cake.data(),k);
		if(ans == -1)
		{
			printf("Case #%d: IMPOSSIBLE\n",c);
		}
		else
		{
			printf("Case #%d: %d\n",c,ans);
		}
		c++;
	}
}
