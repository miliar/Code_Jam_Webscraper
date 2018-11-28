#include <iostream>
#include <string>
using namespace std;


int main(void)
{
	string input;
	int test;
	int k;
	int imp=0,ctr=0;

	cin>>test;

	int j=0;
	while(j<test)
	{	
		ctr=0;
		imp=0;
		cin>>input>>k;
		
		for (int i = 0; i < input.length(); ++i)
		{
			while(input[i]=='+')
				++i;

			int start=i,end=input.length();
			if(end-start < k)
			{
				for (int i = start; i < end; ++i)
				{
					if(input[i]=='-')
						++imp;
				}
			}
			else
			for (int i = 0; i < k; ++i)
			{
				if(input[start+i]=='+')
					input[start+i]='-';
				else
					input[start+i]='+';
			}

			++ctr;			
		}

/*		for (int i = 0; i < input.length(); ++i)
		{
			cout<<" "<<input[i];
		}
		cout<<endl;*/
		if(imp>0)
			cout<<"Case #"<<j+1<<": "<<"IMPOSSIBLE"<<endl;
		else
			cout<<"Case #"<<j+1<<": "<<ctr-1<<endl;

		++j;
	}
}
