#include <iostream>
#include <cstdio>
using namespace std;

int main()
{
	//freopen("input1.txt", "r", stdin);
	//freopen("output1.txt", "w", stdout);
	long long t, n, c, ans=0, s;
	int a[20];
	cin>>t;
	while(t--)
	{
		s=c=0;
		ans++;
		cin>>n;
		while(n)
		{
			a[c++]=n%10;
			n/=10;
		}
		int temp=0, check=0;
		while(temp<c&&a[temp]==a[0])
			temp++;
		if(temp<c)
		{
			int temp1=a[temp];
			while(temp<c&&a[temp]==temp1)
				temp++;
			if(temp==c&&a[0]<temp1)
				check=1;
		}
		if(check==1)
		{
			a[c-1]--;
			for(int i=0; i<c-1; i++)
			{
				a[i]=9;
			}
		}
		else
		{
			for(int i=c-1; i>0; i--)
			{
				if(a[i]>a[i-1])
				{
					a[i]--;
					i--;
					for(int j=i; j>-1; j--)
					{
						a[j]=9;
					}
					break;
				}
			}
		}
		for(int i=c-1; i>-1; i--)
		{
			s=s*10+a[i];
		}
		cout<<"Case #"<<ans<<": "<<s<<endl;
	}
}