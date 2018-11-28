#include<iostream>
#include<math.h>
#include<conio.h>
#include<stdio.h>
using namespace std;
int main()
{	
	int t,i;
	cin>>t;
	int a[100];
	for(i=0;i<t;i++)
	{
		cin>>a[i];
	}
	int m,d1,d2,f,u,v,z;
	for(int j=0;j<t;j++)
	{
		m=a[j];
		f=0;u=0;z=0;
		while(m>9)
		{
			z++;
			d1=m%10;
			d2=(m/10)%10;
			if((d1==d2&&f==1)||d1<d2){f=1;u=z;}
			m=m/10;
		}
		v=pow(10,u);
		if(f==1)a[j]=a[j]-(a[j]%v)-1;
	}
	for(int k=0;k<t;k++)
	{
		cout<<"Case #"<<k+1<<": "<<a[k];
		cout<<endl;
	}
	getch();
	return 0;
}
