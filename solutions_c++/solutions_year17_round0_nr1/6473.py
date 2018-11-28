#include<iostream>
#include<stdio.h>
#include<string.h>
using namespace std;
int checkS(char S[])							//return 1 if string isn't solved
{
	for(int j=0;S[j]!='\0';j++)
	{
		if(S[j]=='-')
			return 1;
	}
	return 0;
}
int Impossible(char S[],int K)					//returns 1 if impossible
{
	for(int j=0;S[j]!='\0'; j++)
	{
		if(S[j]=='-')
		{
			if(strlen(S)-j<K)
				return 1;
			else
				return 0;
		}
	}
}
void output(int x,int i)					//takes number of flips and displays output for particular case
{
	if(x==-1)
		cout<<"Case #"<<i<<": IMPOSSIBLE\n";
	else
		cout<<"Case #"<<i<<": "<<x<<endl;
}
void flip(char &a)							//flips + to - and vice versa
{
	if(a=='+')
		a='-';
	else
		a='+';
}
int main()
{
	int T;
	char S[1001];
	int K;
	cin>>T;
	for(int i=1; i<=T; i++)
	{
		cin>>S;
		cin>>K;
		int flips=0;
		//int len=strlen(S);
		//cout<<checkS(S)<<endl;
		while(checkS(S))
		{
			if(Impossible(S,K))
			{
				flips=-1;
				break;
			}
			for(int p=0;S[p]!='\0';p++)
			{
				if(S[p]=='-')
				{
					flips++;
					for(int z=p;z<p+K;z++)
					{
						flip(S[z]);
					}
					break;
				}
			}
		}
		output(flips,i);
	}
	return 0;
} 
