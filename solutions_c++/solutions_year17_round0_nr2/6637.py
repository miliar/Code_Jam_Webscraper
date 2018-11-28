#include <iostream>

using namespace std;

bool check(string s)
{
	for(int i=0;i<s.length()-1;i++)
	{
		if(s[i] > s[i+1])
			return false;
	}
	
	return true;
}

int main()
{
	char ch[10] = {'1','2','3','4','5','6','7','8','9','0'} ;
	int t;
	cin >> t;
	for(int t_i = 1 ; t_i <=t ; t_i++)
	{
		string s;
		cin >> s;
		for(int i=s.length()-1;i>=0;i--)
		{
			if(s[i] < s[i-1])
			{
				for(int j=i;j<s.length();j++)
					s[j] = '9';
				
				s[i-1]--;
			}
			
		}
		if(check(s) == false)
		{
			s[0]--;
			if(s[0]!='0')
				cout << "Case #" << t_i << ": " << s << endl;
			else
				cout << "Case #" << t_i << ": " << s.substr(1,s.length()) << endl;
		}
		else
		{
			if(s[0]!='0')
				cout << "Case #" << t_i << ": " << s << endl;
			else
				cout << "Case #" << t_i << ": " << s.substr(1,s.length()) << endl;
		}
		
		
	}
	
	return 0;
}
