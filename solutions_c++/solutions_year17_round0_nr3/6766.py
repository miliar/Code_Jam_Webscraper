#include<iostream>
using namespace std;
int main()
{
	int t,n,k;
	cin>>t;
	for(int i=1;i<=t;i++)
	{
		cin>>n>>k;
		bool str[n+2]={0};
		str[0]=1;
		str[n+1]=1;
		int ls=0,rs=0,temp;
		cout<<"Case #"<<i<<": ";
		while(k--)
			{
			int m=0,templ=0,tempr=0,count=0;
			int j=0;
			while(j<n+2)
				{
				if(str[j]==1)
					{
					tempr=j;
					if(m<j-templ)
						{
						ls=templ;
						rs=tempr;
						m=j-templ;
						}
					templ=j;
					}
				++j;
				}
			str[(ls+rs)/2]=1;
			temp=(ls+rs)/2;
			}
	int j=temp-1;
	while(str[j]!=1)
		{
		j--;
		}
	ls=temp-j-1;
	j=temp+1;
	while(str[j]!=1)
		{
		j++;
		}
	rs=j-temp-1;
	//cout<<"vall="<<ls<<" "<<rs<<'\n';
	cout<<max(ls,rs)<<" "<<min(ls,rs)<<'\n';
	}
}