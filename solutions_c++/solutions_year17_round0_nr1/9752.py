#include<iostream>
#include<cstdio>
#include<cstring>
#include<fstream>
using namespace std;
int main()
{
	int t,s;
	scanf("%d",&t);
	s=t;
	while(t--)
	{
		int k;
		string a;
		ofstream file;
		file.open("myfile.out",std::ios_base::app);
		cin>>a;
		scanf("%d",&k);
		int i=0,count=0;
		while(a[i]!='-')
		i++;
		while(i+k<=a.length())
		{
			int j=i,next=i;
			while(j<i+k)
			{
				if(a[j]=='+')
				{
					a[j]='-';
					if(next==i)
					next=j;
				}
				else
				a[j]='+';
				j++;
			}
			if(next==i)
			{
				i=i+k;
				while(a[i]!='-')
				i++;
			}
			else
			i=next;
		     count++;
		}
		i=a.length()-2;
		int  flag=0;
		while(i>=0&&i>=a.length()-k)
		{
			if(a[i]!=a[i+1])
			{
				flag=1;
				break;
			}
			i--;
		}
		if(!flag)
		file<<"Case #"<<s-t<<": "<<count<<endl;
		else
		file<<"Case #"<<s-t<<": IMPOSSIBLE"<<endl;
	}
	return 0;
}
