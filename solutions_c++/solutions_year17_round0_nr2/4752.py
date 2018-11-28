#include<iostream>
#include<sstream>
#include<string>
#include<string.h>
using namespace std;

int main()
{
	int t;
	cin>>t;
	for(int i = 0  ; i < t ; i++)
	{
		string st;
		cin>>st;
		int prev = 0;
		int equal_index = -1;
		for(int j = 0 ; j < st.length() ; j++)
		{
			if(j == 0)
			{

				prev = st.at(0);
				equal_index = j;
			}
			else
			{
				if(st.at(j) > prev)
				{
					equal_index = j;
				}
				else if(st.at(j) < prev)
				{
					
					//int temp = st.at(equal_index)-'0';
					//cout<<temp<<endl;
					//temp--;
					//char ch = char(temp);
					//st.at(equal_index) = ch;
					st.at(equal_index)--;
					for(int k = equal_index+1 ; k < st.length() ; k++)
					{
						st.at(k) = '9';
					}
					break;
				}
				prev = st.at(j);
			}
		}

		cout<<"Case #"<<i+1<<":"<<" ";
		if(st.at(0) == '0')
		{
			for(int j = 1 ; j < st.length() ; j++)
			{
				cout<<st.at(j);
			}
		}
		else
		{
			for(int j = 0 ; j < st.length() ; j++)
			{
				cout<<st.at(j);
			}
		}
		cout<<endl;
	}
}