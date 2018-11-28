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
		bool flag = false;
		long long pos = 0;
		string temp ;
		for(long long i=x.size()-1;i>0;i--)
		{
			//cout<<i<<" "<<x[i]<<" "<<i-1<<" "<<x[i-1]<<endl;
			if(x[i-1]>x[i])
			{
				x[i] = '9';
				x[i-1] = x[i-1] -1;
				pos  = i-1;
				flag = true;
			}
		}

		if(flag)
		{
			// x[pos] = x[pos];

		    for(long long i=pos+1;i<x.size();i++)
		    {
		    	x[i] = '9';
		    }
		}

		cout<<"Case #"<<test-t<<": ";
		bool flag1 = false;
		for(long long i=0;i<x.size();i++)
		{
			if(x[i]!='0')
			{
				flag1 = true;
			}
			if(flag1)
				cout<<x[i];
		}
		cout<<endl;


	}
}