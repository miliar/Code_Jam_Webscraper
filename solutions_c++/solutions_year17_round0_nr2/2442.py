#include <iostream>
#include <string>
using namespace std;

int main()
{
	int t,i,j,x=0;
	char tmp;
	string s;
	scanf("%d",&t);
	while(t--)
	{
		cin >> s;
		for(i=0;i<s.size()-1;i++)
			if(s[i]>s[i+1]) break;
		if(i==s.size()-1)
		{
			printf("Case #%d: %s\n",++x,s.c_str());
			continue;
		}
		j=s.size()-i-1,i=0;
		while(j-->0 || (s.size()>1 && s.back()==s[s.size()-2]))
		{
			i++;
			tmp=s.back();
			s.pop_back();
		}
		if(s.back()=='1') s.pop_back();
		else s[s.size()-1]--;
		while(i--) s.push_back('9');
		printf("Case #%d: %s\n",++x,s.c_str());
	}
} 
