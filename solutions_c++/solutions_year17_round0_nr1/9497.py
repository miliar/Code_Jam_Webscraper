#include<iostream>
#include<string.h>
#include<conio.h>
#include<fstream>
using namespace std;
fstream fout("JAM1.txt",ios::out);
char S[1001];
int count=0;
int flag=0;
int K;
/*REMOVE GETCH*/
void flip(int i)
{       int z=0;
	while(z<K)
	{
		S[i]=((S[i]=='-')?'+':'-');
		i++; z++;
	}
}
void check()
{
for(int q=0;q<strlen(S);q++)
{
	if(S[q]=='-')
	{
	flag=1;
	break;
	}
}
}
int main()
{

	int T;
	cin>>T;
	for(int temp=0;temp<T;temp++)
	{
		count=0;flag=0;
		cin>>S;	cin>>K;
		for(int i=0;i<=strlen(S)-K;i++)
		{
			if(S[i]=='-')
			{
				flip(i);      count++;
			}
		}
	check();
	if(flag!=1)
	{
		fout<<"Case #"<<temp+1<<": "<<count<<endl;
	}
	else
		fout<<"Case #"<<temp+1<<": IMPOSSIBLE"<<endl;
	}

return 0;
}
