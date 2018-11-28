#include<iostream>

using namespace std;

string tidy_up(string s)
{
	for (int k=s.size()-1;k>0;k--)
	{		
		if (s[k]<s[k-1])
			
			{
				s[k]='9';
				if (s[k-1]=='0')
				{int j=k-1;
				
					while (s[j]=='0' && j>=0)
						{s[j]='9';
							j=j-1;
						}
				}
				else s[k-1]=s[k-1]-1;
				
			if (s[k]=='9')
			{
					for (int i=k;i<s.size();i++)
						{s[i]='9';}
			}			
			}
	}
	s.erase(0,s.find_first_not_of('0'));
	return s;
}
int main()
{
	int t;
	cin >> t;
	string s;
	for (int i=0;i<t;i++)
	{
		cin >> s;
		s=tidy_up(s);
		cout << "Case #" << i+1 <<": "<< s<< endl;
		
	}
	
	return 0;







}
