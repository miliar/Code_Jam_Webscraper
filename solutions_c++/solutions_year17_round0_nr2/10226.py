#include<iostream>
#include<conio.h>
#include <fstream>
using namespace std;
std::ifstream infile("B-small-attempt0.in");
int flag=0;
int digit(int n)
{
	long int a=n,b1,b2;
	while(a>0)
	{
		b1=a%10;
		a=a/10;
		b2=a%10;
		//cout<<"b1 is: "<<b1<<"\tb2 is: "<<b2<<endl;
		if(b1>=b2)
		flag=1;
		else
		{
			flag=0;
			return flag;
		}
	}
	return flag;
}

int main()
{
	int t;
	infile>>t;
	int x=t+1;
	while(t>0)
	{

	int n;
	infile>>n;
	if(n/10==0)
	{
		cout<<"Case #"<<x-t<<": "<<n<<endl;
		t--;
		continue;
	}
	for(int i=n;i>0;i--)
	{
		//cout<<"number is : "<<i<<endl;
		flag=digit(i);
		if(flag==1)
		{
			cout<<"Case #"<<x-t<<": "<<i<<endl;
			break;
		}
	}
	
	t--;
	}
}
