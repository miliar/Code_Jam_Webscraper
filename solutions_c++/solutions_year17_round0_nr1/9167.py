#include<iostream>
#include<string>
using namespace std;
int main()
{
	string s;
	int k,t,flip=0;
	cin>>t;
	for(int i=0;i<t;i++)
	{
		flip=0;
		cin>>s;
		cin>>k;
		for(int j=0;j<s.length();j++)
		{
			if(s[j]=='-'&& (j+k)<=s.length())
			{
				flip++;
				for(int L=0;L<k;L++)
				{
					if(s[j+L]=='-')
					{
						s[j+L]='+';
					}
					else
					{
						s[j+L]='-';
					}
				}
			}
		}
		bool ch=true;
		for(int j=0;j<s.length();j++)
		{
			if(s[j]=='-')
			{
				
				ch=false;
				break;
			}
		}
		if(ch)
		{
			cout << "Case #" << i+1 << ": " << flip << endl;
		}
		else
		{
			cout << "Case #" << i+1 << ": " << "IMPOSSIBLE" << endl;
		}
	}
	
}
