#include <iostream>
#include <string>
#include <math.h>
using namespace std;

bool check(string s)
{
	
	for(int i = 0;i < s.length()-1;i++)
	{
		if (s[i]> s[i+1])
		{
			return false;
		}
	}
	return true;
}

int main()
{


	int t;
	cin >> t;
	for(int i = 0;i<t;i++)
	{

		string s;
		cin >>s;
		string t;
		t =s;
		int index = 0;
		char equal = ' ';
		int equalindex = -1;
		
		
		while (index <= s.length()-1)
		{
			if (s[index+1] > s[index])
			{
				index ++;
				equalindex = -1;
			}
			else if(s[index+1] == s[index]) 
			{
				if (equalindex == -1)
				{
					equalindex = index;
				}
				index ++;
				
			}
			else
			{
				if ( index >= 1	 && s[index-1] == s[index] )
				{
					index = equalindex;
					s[index] -= 1;
					index ++;
					while(index < s.length())
					{
						s[index ] = '9';
						index ++;
					}	
				}
				else
				{
					s[index] -= 1;
					index ++;
					while (index < s.length())
					{
						s[index ] = '9';
						index ++;

					}
				}
			}
		}

		int h =0;
		cout <<"Case #"<<i+1<<": ";
		if (t.length()==1 || check(t))
		{
			cout <<t<<endl;
		}
		else
		{
			for(h = 0;s[h] == '0';h++)
			{
				//cout<<"a";
			}
			for(int x  = h;x < s.length();x++)
			{
				cout<<s[x];
			}
			cout <<endl;
		}
	}

	return 0 ;
}