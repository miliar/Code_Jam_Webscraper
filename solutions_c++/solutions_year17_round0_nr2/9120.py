#include <bits/stdc++.h>
using namespace std;
int main()
{
	freopen("B-small-attempt0.in","r",stdin);
    freopen("A-large-practice.out","w",stdout);
	int test;
	cin>>test;
	for(int i=1;i<=test;i++)
	{
		int n;
		cin>>n;
		long long int a[100000]={0},k=0,digits=0;
		for(int s=n;s>=1;s--)
		{
			int num=s,yes=0,digits=0,k=0;
			while(num>0)
			{
				a[k]=num%10;
				num=num/10;
				digits++;
				k++;
			}
			/*cout<<"digits "<<digits<<endl;
			for(int h=0;h<digits;h++)
				cout<<a[h]<<" ";
			cout<<endl;
			*/
			for(int j=0;j<digits-1;j++)
			{
				if(a[j]>=a[j+1])
					yes++;
			}
			if (yes==digits-1)
			{
				cout<<"Case #"<<i<<": "<<s<<endl;
				break;
			}

		}
	}
}