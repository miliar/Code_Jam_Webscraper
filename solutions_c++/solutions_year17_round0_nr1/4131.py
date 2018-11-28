#include <iostream>
#include <cstring>
using namespace std;
int A[1010];
int S[1010];
string s;
int main()
{
	int T,k,sum;
	int i,j;
	cin>>T;
	for(i=1;i<=T;i++)
	{
		cin>>s;
		cin>>k;
		memset(A,0,sizeof(A));
		sum=0;
		for(j=0;j<s.size();j++)
		{
			if(j-k>=0)
			{
				sum-=A[j-k];
			}
			if(j-1>=0)
			{
				sum+=A[j-1];
			}
			if(sum%2==1)
			{
				if(s[j]=='+')
				{
					s[j]='-';
				}
				else
				{
					s[j]='+';
				}
			}
			if(j+k-1<s.size()&&s[j]=='-')
			{
				A[j]++;
				s[j]='+';
			}
		}
		sum=0;
		for(j=0;j<s.size();j++)
		{
			if(s[j]=='-')
			{
				break;
			}
			sum+=A[j];
		}
		cout<<"Case #"<<i<<": ";
		if(j<s.size())
		{
			cout<<"IMPOSSIBLE"<<endl;
		}
		else
		{
			cout<<sum<<endl;
		}
	}
	return 0;
}
