#include<iostream>
#include<string>
using namespace std;
int main()
{
	int t,case_num=1;
	cin>>t;

	char num[20];
	string str;
	while(t--)
	{
		cin>>str;
		int  i = 0,j=0;
		if(str.length() <= 1)
		{
			cout<<"Case #"<<case_num++<<": "<<str<<"\n";
			continue;
		}
		for(i=0;i<str.length()-1;++i)
		{
			if(str[i] > str[i+1])
			break;
		}
		if(i < str.length()-1)
		{
			if(i > 0 && str[i] == str[i-1])
			{
				for(j = i-1;j>=0;--j)
				{
					if(str[j] != str[i])
						break;
				}
				if(j >= 0)
				{
					i = j+1;
				}
				else
				{
					i = 0;
				}
			}
			str[i]--;
			for(++i;i<str.length();++i)
			{
				str[i] = '9';
			}

		}
		
		for(i=0;i<str.length();++i)
		{
			if(str[i] != '0')
				break;
		}

		j=0;
		for(;i<str.length();++i)
		{
			num[j++] = str[i];
		}
		num[j] = '\0';
		cout<<"Case #"<<case_num++<<": "<<num<<"\n";
	}
	return 0;
}