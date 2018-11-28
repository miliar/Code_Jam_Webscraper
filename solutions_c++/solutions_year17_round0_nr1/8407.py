#include <bits/stdc++.h>

using namespace std;

void updatefen(int *a,int i)
{
	while(i<1000)
	{
		a[i]++;
		i = i + (i&(-i));
	}
}

int queryfen(int* a,int i)
{
	int sum = 0;
	if(i==0)
		return 0;
	while(i>0)
	{
		sum += a[i];
		i = i - (i&(-i));
	}
	return sum;
}


int main()
{
	int a[2001],T,i,j,count,flag,newflag,k;
	string s;
	cin>>T;
	for(i=0;i<T;i++)
	{
		cin>>s;
		cin>>k;
		memset(a,0,sizeof a);
		count = 0;
		newflag = 1;
		for(j=0;j<s.size();j++)
		{
			flag = (queryfen(a,j+1) - queryfen(a,max(0,j-k+1)))&1;
			if((s[j] == '+' && flag) || (s[j] == '-' && flag == 0) )
			{
				if(j>=(s.size()-k+1))
				{
					newflag = 0;
					break;
				}
				count++;
				updatefen(a,j+1);	
			}
		}	
		cout<<"Case #"<<i+1<<": ";
		if(newflag)
		cout<<count<<"\n";
		else
		cout<<"IMPOSSIBLE\n";	
	}
	return 0;
}