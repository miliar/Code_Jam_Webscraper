#include <iostream>

using namespace std;

int main()
{
	long long t;
	cin>>t;
	long long test = t;
	while(t--)
	{
		string x;
		cin>>x;
		long long k;
		cin>>k;
		long long count = 0;
		for(long long i=0;i<x.size();i++)
		{
			//cout<<i<<endl;
			if(x[i]=='-')
			{
				if(i+k>x.size())
					break;
				count++;
				for(long long j = i;j<i+k;j++)
				{
					if(x[j]=='-')
					{
						x[j]='+';
					}
					else
					{
						x[j] = '-';
					}

				}
			}
		}

		bool flag = false;

		for(long long i=0;i<x.size();i++)
		{
			if(x[i]=='-')
			{flag = true;break;}

		}

		if(flag)
		cout<<"Case #"<<test-t<<": "<<"IMPOSSIBLE";
		else
		cout<<"Case #"<<test-t<<": "<<count;
		cout<<endl;
	}
}