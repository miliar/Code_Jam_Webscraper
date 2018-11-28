#include<iostream>
#include<string>
using namespace std;
string calculate(string s)
{
	int flag = 0;
	int i,j;
	for(i=0;i<s.size()-1;i++)
	{
		if(s[i]>s[i+1])
		{
			s[i]=s[i]-1;
			for(j=i+1;j<s.size();j++)	
				s[j]='9';
			flag=1;
			break;
		}
		/*else
			flag=0;*/
	}
	if(flag==1)
	{
		return calculate(s);
	}
	else if(flag==0)
		return s;
}
int main()
{
	int t,j,x;
	string s,final;
	cin>>t;
	long long int number;
	char *pEnd;
	for(x=1;x<=t;x++)
	{
		cin>>s;
		final = calculate(s);
		number = strtoll(final.c_str(),&pEnd,10);
		//cout<<number<<endl;
		cout<<"Case #"<<x<<": "<<number<<endl;
	}
}