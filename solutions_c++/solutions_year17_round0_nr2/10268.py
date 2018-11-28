#include<iostream>
using namespace std;

bool isTidy(unsigned long long n)
{
	int digit;
	int last_digit = n%10;
	unsigned long long temp = n/10;
	
	while(temp>0)
	{
		digit = temp%10;
		if(last_digit<digit)
		{
			return false;
		}
		last_digit = digit;
		temp/=10;
	}
	return true;
}

int main()
{
	unsigned short t;
	unsigned long long N;
	cin>>t;
	for(int c = 1; c<=t; c++)
	{	
		cin>>N;
		for(unsigned long long i=N; i>=1; i--){
			if(isTidy(i)){
				cout<<"Case #"<<c<<": "<<i<<'\n';
				break;
			}
		}
	}
	return 0;
}
