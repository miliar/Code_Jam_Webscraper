#include <iostream>
using namespace std;


int check(long long ret)
{
	while(ret)
	{
		int temp=ret%10;
		ret/=10;
		if(temp<ret%10)
			return 1;
	}
	return 0;
}


int main() 
{
int t,tt;
long long ret;
cin>>t;
tt=t;
while(tt--)
{
	cin>>ret;
	while(check(ret))
		 ret--;
	cout<<"Case #"<<t-tt<<": "<<ret<<endl;
}
return 0;
}