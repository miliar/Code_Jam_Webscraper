#include <bits/stdc++.h>
using namespace std;


string int2str(int a)
{
	stringstream ss;
	ss << a;
	return ss.str();
}


bool tidy(int num)
{
	string num_str=int2str(num);
	int num_len=int(num_str.length());
	for(int j=0;j<(num_len-1);j++)
	{
		if(int(num_str.at(num_len-j-1))<int(num_str.at(num_len-j-2)))
			return false;
	}
	return true;
}


int main()
{
	int test_case;
	cin>>test_case;
	for(int abc=0;abc<test_case;abc++)
	{
		int num;
		cin>>num;
		for(int i=num;i>0;i--)
		{
			if(tidy(i))
			{
				cout<<"Case #"<<(abc+1)<<": "<<i<<endl;
				break;
			}
		}					
	}
	return 0;
}

