#include <iostream>
using namespace std;

bool isTidy(int n)
{
	if(n<10)
		return true;
	int a=n%10;
	n=n/10;
	int b=n%10;
	while(n)
	{
		if(a<b)
			return false;
		a=b;
		n=n/10;
		b=n%10;
	}
	return true;
}

int main() 
{
	int t,t1,n;
	cin>>t;
	t1=1;
	while(t--)
	{
		cin>>n;
		while(!isTidy(n))
		{
			n--;
		}
		cout<<"case #"<<(t1)++<<": "<<n<<endl;
	}
	return 0;
}
