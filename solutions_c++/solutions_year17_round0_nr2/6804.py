#include<iostream>
using namespace std;

int main()
{
	int t;
	cin>>t;
	int h=0;
	for(int i=0;i<t;i++)
	{
		long long int value;
		long long int value1;
		cin>>value;
		value1 = value;
		long long int x = 1;
		long long int y = 10;
		int digit=1;
		while(1)
		{
			if(value>=x && value<y)
			{
				break;
			}
			else
			{
				digit++;
				x*=10;
				y*=10;
			}
		}
	//	cout<<digit<<endl;
		int a[digit];
		int digit1 = digit;
		while(value!=0)
		{
			a[digit1-1] = value%10;
			value = value/10;
			digit1--;
		}
	
		int flag=0;
		int j;
		for(j=0;j<digit-1;j++)
		{
			if(a[j]<=a[j+1])
			{
				continue;
			}
			else
			{
				flag=1;
				break;
			}
		}
		if(flag==0)
		{
			//cout<<"he"<<endl;
			printf("Case #%d: %lld\n",i+1,value1);
			continue;
		}
		a[j]--;
		for(int k = j+1;k<digit;k++)
		{
			a[k] = 9;
		}
		for(int k=j;k>0;k--)
		{
			if(a[k]<a[k-1])
			{
				a[k-1]--;
				a[k] = 9;
			}
		}
		for(int k=0;k<digit;k++)
		{
			value = value*10 + a[k];
		}
		printf("Case #%d: %lld\n",i+1,value);
		//h++;
	}
	return 0;
}
