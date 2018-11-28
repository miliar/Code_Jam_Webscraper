#include<iostream>
#include <string.h>
using namespace std;
int main()
{
	int t,i;
	cin>>t;
	for(i=1;i<=t;i++)
	{
		int j,k,l,n,start=0,end,flag=1,cnt=0;
		char S[1001];
		cin>>S;
		cin>>k;
		n = strlen(S);
		j=0;
		while(S[j]=='+')
		{
			j++;
		}
		while(j<n && flag==1)
		{
			start = j;
			end = k-1 + j;
			if(end > n-1)
			{
				flag = 0;	
			}
			else
			{
				l=start;
				while(l<=end)
				{
					if(S[l]=='-')
					{
						S[l]='+';
					}
					else
					{
						S[l]='-';
					}
					l++;
				}
				cnt++;
				j=start;
				while(S[j]!='-')
				{
					j++;
				}
			}
		}
		if(flag==0)
		{	
			cout<<"Case #"<<i<<": IMPOSSIBLE"<<endl;
		}
		else
		{
			cout<<"Case #"<<i<<": "<<cnt<<endl;
		}
	}
	return 0;
}
