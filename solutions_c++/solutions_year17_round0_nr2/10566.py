#include<iostream>
#include<conio.h>
using namespace std;
int main()
{
	int t=1,n=1,i,j,c,count,ct=1;
	cin>>t; int ar[t];
	while(ct<=t)
	{
		cin>>n;
		for(j=n;j>=1;j--)
		{
			c=9999;count=0;
			for(i=j;i>0;i=i/10)
			{ 
				if(i%10>c)
				{
					count++;
					break;
				}
				else
				{	
					c=i%10;
				}
			}
			if(count==0)
			{  
			ar[ct]=j;
			break;
			}
		}
		ct++;
	}
	for(i=1;i<=t;i++)
	{
		cout<<"case #"<<i<<": "<<ar[i];
		cout<<"\n";
	}
	getch();
	return(0);
}
