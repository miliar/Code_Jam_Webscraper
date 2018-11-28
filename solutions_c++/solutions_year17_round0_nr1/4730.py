#include<iostream>
#include<algorithm>
using namespace std;


bool isSorted(string str)
{
	int len=str.length();
	for(int i=0; i<len; i++)
	{
		if(str[i]=='-')
			return false;

	}
	return true;
}

int main()
{

	int T=0;
	cin>>T;

	for(int t=1; t<=T; t++)
	{

		string str;
		int pan;

		cin>>str;
		cin>>pan;

		cout<<"Case #"<<t<<": ";
		//cout<<str<<"\t"<<pan<<"\n";

		int count=0;
		int len = str.length();

		int loop = 2;
		while(loop--)
		{
		//	cout<<loop<"\n";
		for(int i=0; i+pan <= len; i++)
		{
			if( str[i] == '-' )
			{
				count++;
				//cout<<"index ; "<<i<<"\n";
				int max = i+pan;
				for(int j=i; j<max; j++)
				{
					if ( str[j] == '-')
						str[j] = '+';
					else
						str[j] = '-';
				}
				//cout<<str<<"\n";
			}

		}
		}	


		if(isSorted(str))
			cout<<count;
		else
			cout<<"IMPOSSIBLE";
		cout<<"\n";
	}
	return 0;
}
