#include<iostream>

using namespace std;

int main()
{
	int tc,i;
	cin>>tc;
	for(i=1;i<=tc;i++)
	{
		long long int n,j;
		cin>>n;
		long long tmp=n;
		string s=to_string(n);
		int ln=s.length();
		int a[ln];
		for(j=ln-1;j>=0;j--)
		{
			a[j]=tmp%10;
			tmp=tmp/10;
		}

		for(j=ln-1;j>0;j--)
		{
			if(a[j]<a[j-1])
			{
				for(int k=j;k<ln;k++)
				{
					if(a[k]!=9)
					a[k]=9;
				}
				a[j-1]--;
			}
		}
		j=0;
		if(a[j]==0)
		j++;
		cout<<"Case #"<<i<<": ";
		for(;j<ln;j++)
		{
			cout<<a[j];
		}
		cout<<endl;
	}
}
