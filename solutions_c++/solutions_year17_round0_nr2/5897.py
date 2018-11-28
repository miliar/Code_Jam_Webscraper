#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int main() {
	ifstream input;
	ofstream output;
	output.open("cj#bo122.txt");
	input.open("B-small-attempt0.txt");
	int c = 1;
	try
	{
		string s;
		getline(input,s);
		string str;
		while(getline(input,str))
		{
			int len = str.length();
			int i = 0;
			if(len==1)
			{
				output<<"Case #"<<c<<": "<<str<<"\n";
				c++;
			}
			else
			{
				while(i<len-1)
				{
					if(str[i]>str[i+1])
					{
						int num = str[i]-'0';
						num--;
						str[i] = '0'+num;
						int j = i+1;
						int cc = i;
						while(j<len)
						{
							str[j] = '9';
							++j;
							++i;
						}
						while(str[cc]>0&&str[cc]<str[cc-1])
						{
							str[cc] = '9';
							int num = str[cc-1] - '0';
							num--;
							str[cc-1] = '0'+num;
							cc--;
						}
					}
					++i;
				}
				if(str[0]=='0')
					str.erase (str.begin(), str.begin()+1);
				output<<"Case #"<<c<<": "<<str<<"\n";
				++c;
			}
		}
	}
	catch(char const* msg)
	{
		cout<<msg;
	}
	return 0;
}
