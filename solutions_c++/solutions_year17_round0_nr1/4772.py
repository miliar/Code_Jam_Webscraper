#include<iostream>
using namespace std;

int main()
{
	int t;
	cin>>t;
	for(int i = 0 ; i < t ; i++)
	{
		string st;
		cin>>st;
		int k;
		cin>>k;
		int count = 0;
		int flag = 0;
		for(int j = 0 ; j < st.length() ; j++)
		{
			if(st.at(j) == '-')
			{
				if(j+k <= st.length())
				{
					count++;
					for(int n = j ; n < j+k ; n++)
					{
						if(st.at(n) == '-')
							st.at(n) = '+';
						else
							st.at(n) = '-';
					}
				}
				else
				{
					flag = 1;
					break;
				}
			}
		}
		if(flag == 0)
		{
			cout<<"Case #"<<i+1<<":"<<" "<<count<<endl;
		}
		else
		{
			cout<<"Case #"<<i+1<<":"<<" "<<"IMPOSSIBLE"<<endl;
		}
	}
}