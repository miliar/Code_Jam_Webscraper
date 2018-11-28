#include <iostream>
using namespace std;
int check(int n)
{
	int digit=n%10;
	n=n/10;
	int flag=0;
	while(n>0)
	{
		if(digit<n%10)
		{
			flag=1;
			break;
		}
		else
		{
			digit=n%10;
			n=n/10;
		}
	}
	if(flag==0) return 1;
		else return 0;
}
int main()
{
	int t;
	cin>>t;
	int n;
	for(int i=0;i<t;i++)
	{
		cin>>n;
		int p;
		cout<<"Case #"<<i+1<<": ";
		while(true)
		{
			 p=check(n);
			 if(p>0)
			 {
			 	cout<<n<<endl;
			 	break;
			 }
			 else n=n-1;
		}

	}
}