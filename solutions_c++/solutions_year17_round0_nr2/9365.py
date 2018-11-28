#include<bits/stdc++.h>
using namespace std;
bool asc(int number)
{
	int last=number%10;
	number /=10;
	while(number)
	{
		int digit=number%10;
		if(digit > last)
			return false;
		last=digit;
		number /=10;
	}
	return true;
}
int main()
{
	int t;
	cin>>t;
	int count=0;
	while(t--)
	{
	count++;
	int n;
	cin>>n;
	while(n)
	{
		if(asc(n))
			{
			cout<<"Case #"<<count<<": "<<n<<endl;
			break;
			}
		n--;
	}
		//asc(n) ? cout<<"True" : cout<<"False";

	}
}
