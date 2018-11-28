#include <iostream>
#include<string>
using namespace std;

int main() {
	int t;
	cin>>t;
	int m=0;
while(t>0)
{
t--;
m++;
cout<<"Case #"<<m<<": ";
	string s;
	cin>>s;
	unsigned long long int k;
	cin>>k;
	unsigned long long int i=0;
	unsigned long long int cnt=0;
	while(i!=s.size())
	{
		if(s[i]=='+')
		{
			i++;
			continue;
		}
		else
		{
			if(i + k  > s.size())
                    break;
			for(unsigned long long int j=0;j<k;j++)
			{
		
			if(s[i+j]=='-')
			s[i+j]='+';
			else
			s[i+j]='-';
			}
		}
		cnt++;
	}
	
	if(i!=s.size())
	cout<<"IMPOSSIBLE"<<endl;
	else
	cout<<cnt<<endl;
	}
	return 0;
}