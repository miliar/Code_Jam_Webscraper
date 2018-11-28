#include <iostream>
using namespace std;
int check(unsigned long long int num1)
{
	int mod ,mod1,ind=0,l=0;
	unsigned long long int temp;
	temp = num1;
	while(temp!=0)
	{
		l++;
		temp = temp/10;
	}
	while(num1!=0)
	{
		mod = num1%10;
		num1 = num1/10;
		mod1 = num1%10;
		if(mod1 <mod || mod1 == mod)
		{
			ind++;
		}
		else
		{
			return 1;
		}
	}
	if(ind == l)
	{
		return 0;
	}
}
int main()
{
	int t,i;
	cin>>t;
	unsigned long long int num;
	for(i = 0;i<t;i++)
	{
		cin>>num;
		if(num>=1 && num<=19)
		{
			cout<<"Case #"<<(i+1)<<":"<<" "<<num<<endl;
		}
		else
		{
			while(check(num))
			{
				num = num-1;
			}
			cout<<"Case #"<<(i+1)<<":"<<" "<<num<<endl;	
		}
	}		
	return 0;
}