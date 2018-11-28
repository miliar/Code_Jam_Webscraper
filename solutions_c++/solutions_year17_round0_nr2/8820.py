#include<iostream>
#include<string>

using namespace std;

int main()
{
	unsigned long long n,num;
	int t,temp=1,bp,len;
	string s;
	char comp;
	cin>>t;

	while(t--)
	{
		cin>>n;

		s = to_string(n);

		len = s.length();
		bp=len;
		comp=0;
		//cout<<"\n"<<len<<"\n";
		for(int i = 1;i < len;i++)
		{
			if(s[i]<s[comp])
			{
				s[comp]=s[comp]-1;
				
				bp=comp+1;
				break;
				
			}
			else if(s[i]>s[comp])
			{
				comp=i;
			}
			
		}

		for(int i = bp;i < len;i++)
			s[i]='9';

		num=stoll(s);
		cout<<"Case #"<<temp<<": "<<num<<"\n";
		temp++;
		

	}
	return 0;
}
