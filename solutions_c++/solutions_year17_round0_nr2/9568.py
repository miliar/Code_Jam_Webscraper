using namespace std;
#include<iostream>
#include<fstream>
int func()
{
	unsigned long long int T,a,b,c,n,d,flag=1;
	ifstream f1;
	ofstream f2;


	f1.open("B-small-attempt0.in");
	f2.open("B-small-attempt0.out");
	f1>>T;

	for(int i=1;i<=T;i++)
	{
		f1>>a;
		for(n=a;n>=0;n--)
		{
			b=n;
			flag=1;
			while(b>=9)
			{
				c=b%10;
				b=b/10;
				d=b%10;
				if(d<=c)
				{
					flag=1;
				}
				else
				{
					flag=0;
					break;
				}
			}
			if(flag==1)
			{
				f2<<"Case #"<<i<<": "<<n<<endl;
				break;
			}
		}
	}
	f1.close();
	f2.close();
	return 0;
}
int main()
{
	func();
	return 0;
}
