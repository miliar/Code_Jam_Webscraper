#include <iostream>
using namespace std;

bool checkOrder(unsigned long long num)
{
	
	int temp1=num%10;
	while(num>0)
	{
	int temp2=num%10;
	if(temp1>=temp2)
	{
		temp1=temp2;
		num/=10;
	}
	else
	return false;
	
	}
	return true;
}

unsigned long long number(unsigned long long num)
{
if(checkOrder(num))
return num;

else
return number(num-1);

}

int main ()
{
int testcase;
cin>>testcase;
unsigned long long num;
for (int i=0;i <testcase;i++)
{
cin>>num;
cout<<"Case #"<<i+1<<": "<<number(num)<<endl;
}
return 0;
}
