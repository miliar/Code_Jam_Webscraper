#include<iostream>
#include<cstring>
using namespace std;

int main()
{
	int t,x,last,count,j=1;
	long long int n,nine,result,ten;
	cin>>t;
	while(t--)
	{
		cin>>n;
		count = 0;
		last = 9;
		nine = 0;
		ten = 1;
		result = n;
		while(n!=0)
		{
			x = n%10;
			if(x<=last)
			{
				n = n/10;
				last = x;
				count+=1;
			}
			else
			{
				for(int i=0 ; i<count ; i++)
				{
					nine = (nine*10) + 9;
					ten = ten*10;
				}
				n = n-1;
				n = (n*ten) + nine;
				count = 0;
				result = n;
				last = 9;
				nine = 0;
				ten = 1;
			}
		}
		
		cout<<"Case #"<<j++<<": ";
		cout<<result<<endl;
	}
}
