#include<iostream>
#include<conio.h>
using namespace std;
struct p
{
	char s[1000];
	int k;
	int c;
};
int main()
{	
	int t;
	cin>>t;
	p ob[100];
	for(int i=0;i<t;i++)
	{
		cin>>ob[i].s>>ob[i].k;
		ob[i].c=0;
	}
	for(int i=0;i<t;i++)
	{
		for(int j=0;ob[i].s[j+(ob[i].k)-1]!='\0';j++)
		{
			if(ob[i].s[j]=='-')
			{
				for(int k=0;k<ob[i].k;k++)
				if(ob[i].s[j+k]=='+')ob[i].s[j+k]='-';
				else ob[i].s[j+k]='+';
				ob[i].c++;
			}
		}
	}
	for(int i=0;i<t;i++)
	{
		for(int j=0;ob[i].s[j]!='\0';j++)
		if(ob[i].s[j]=='-')ob[i].c=-1;
	}
	for(int i=0;i<t;i++)
	{
		cout<<"Case #"<<i+1<<": ";
		if(ob[i].c!=-1)cout<<ob[i].c;
		else cout<<"IMPOSSIBLE";
		cout<<endl;
	}
	getch();
	return 0;

}
