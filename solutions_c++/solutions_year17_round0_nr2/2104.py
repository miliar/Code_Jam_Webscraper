#include <bits/stdc++.h>

using namespace std;

string func(string str)
{
	for(int i=0;i<str.length()-1;i++)
	{
		if(str[i]-'0'>str[i+1]-'0')
		{
			for(int j=i+1;j<str.length();j++)
				str[j] = '9';
			str[i] = (str[i]-'0'-1)+'0';
		}
	}
	return str;
}

int istidy(string str)
{
	for(int i=0;i<str.length()-1;i++)
	{
		if(str[i]-'0'>str[i+1]-'0')
			return 0;
	}
	return 1;
}

int main()
{
	int t,tt;
	string str;
	cin >> t;
	for(tt=1;tt<=t;tt++)
	{
		cin >> str;
		while(1)
		{
			if(str.length()==1)
				break;
			str = func(str);
			if(str[0]=='0')
			{
				if(istidy(str.substr(1,str.length())))
					break;
			}
			else
			{
				if(istidy(str))
					break;
			}
		}
		cout << "Case #" << tt << ": ";
		if(str.length()==1)
			cout << str << endl;
		else if(str[0]!='0')
			cout << str << endl;
		else
			cout << str.substr(1,str.length()) << endl;
	}
	return 0;
}
