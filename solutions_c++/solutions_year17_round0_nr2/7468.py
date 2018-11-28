#include<iostream>
#include<math.h>
using namespace std;
int main()
{
	int t;
	cin>>t;
	int i,j;
	int u[100];
	for(i=0;i<t;i++)
	{
		int n;
		cin>>n;
		int a[4];
		ol:
		int y=n;
		for(j=3;j>=0;j--)
		{
			int u=pow(10,j);
			int z=y/u;
			a[3-j]=z;
			y=y%u;
		}
		int flag=0;
		for(j=0;j<3;j++)
		{
			if(a[j+1]<a[j])
			{
			flag=1;
			break;}
		}
		if(flag==1)
		{
			n--;
			goto ol;
		}
		else
		{
			u[i]=n;
			//cout<<u[i];
		//cout<<"Case #"<<i+1<<": "<<n<<"\n";
		}
	}
	for(i=0;i<t;i++)
		cout<<"Case #"<<i+1<<": "<<u[i]<<"\n";
}
