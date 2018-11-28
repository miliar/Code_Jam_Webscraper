using namespace std;
#include<iostream>
#include<fstream>
#include<string.h>

int main()
{
	ifstream f1;
	ofstream f2;
	
	int T,k=0,l,count=0,flag,i,j,m;
	char s[1000];
	
	f1.open("A-small-attempt0.in");
	f2.open("A-small-attempt0.out");
	
	f1>>T;
	
	for(i=1;i<=T;i++)
	{
		flag=1;
		count=0;
		f1>>s;
		f1>>k;
		
		l=strlen(s);
		
		for(j=0;j<=l-k;j++)
		{
			if(s[j]==45)
			{
				for(m=j;m<j+k;m++)
				{
					if(s[m]==45)
						s[m]=43;
					else
						s[m]=45;	
				}
				count++;
			}
		}
		for(j=0;j<l;j++)
		{
			if(s[j]==45)
				flag=0;
		}
		if(flag==0)
			f2<<"Case #"<<i<<": IMPOSSIBLE"<<endl;
		else
			f2<<"Case #"<<i<<": "<<count<<endl;	
	}   
	
	return 0;
}
