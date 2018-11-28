#include <iostream>
using namespace std;

int main() {
	int n;
	cin>>n;
	int ch = 1;
	while(n--)
	{
		string s;
		cin>>s;
		int len = s.length();
		int i = 0;
		if(len==1)
		{
			cout<<"Case #"<<ch<<": "<<s<<"\n";
			ch++;
		}
		else
		{
			while(i<len-1)
			{
				if(s[i]>s[i+1])
				{
					int num = s[i]-'0';
					num--;
					s[i] = '0'+num;
					int j = i+1;
					int cc = i;
					while(j<len)
					{
						s[j] = '9';
						++j;
						++i;
					}
					while(s[cc]>0&&s[cc]<s[cc-1])
					{
						s[cc] = '9';
						int num = s[cc-1] - '0';
						num--;
						s[cc-1] = '0'+num;
						cc--;
					}
				}
				++i;
			}
			if(s[0]=='0')
				s.erase (s.begin(), s.begin()+1);
			cout<<"Case #"<<ch<<": "<<s<<"\n";
			++ch;
		}
	}
	return 0;
}