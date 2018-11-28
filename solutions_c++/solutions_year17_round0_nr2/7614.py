#include<iostream>

using namespace::std;

int istidy(long num)
{
	long val=0,prev_val=10;
	while(num)
	{
		val = num % 10;
		num= num / 10;
		if(prev_val < val)
			return 0;
		prev_val = val;
	}
	return 1;
}
int main()
{
	int n;
	cin>>n;
	long num;
	for(int i=0;i<n;i++)
	{
		cin >> num;
		
		for(long j = num ; j >0 ;j--)
		{
			//cout<<j<<endl;
			if(istidy(j)==1)
			{
				cout<<"Case #"<<i+1<<": "<<j<<'\n';
				break;
			}
		}
	}
	return 0;
}
