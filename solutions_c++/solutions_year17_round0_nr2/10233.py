#include<stdio.h>
#include<string.h>
#include <iostream>
#include <fstream>
using namespace std;
ofstream myfile;

bool ch(char in[],char la)
{
	if(strlen(in)==0)
	{
		return true;
	}
	else
	{
		if(in[strlen(in)-1]>la)
		return false;
		else 
		{
			la=in[strlen(in)-1];
			in[strlen(in)-1]='\0';
			return ch(in,la);
		}
	}
}
char te,bo[100];
int len,i;
int thi(char in[])
{
	if(strlen(in)==1&&in[0]=='0')
	{
		printf("0\n");
		return 0;
	}
	te=in[strlen(in)-1];
	strcpy(bo,in);
	in[strlen(in)-1]='\0';
	while(ch(in,te)==false)
	{
		//printf("in wh\n");
		len=strlen(bo)-1;
		while(bo[len]=='0'&&len>=0)
		{
			bo[len]='9';
			len--;
		}
		bo[len]=bo[len]-1;
		te=bo[strlen(bo)-1];
		//printf("%d ",strlen(bo));
		strcpy(in,bo);
		//cout<<in<<"\n";
		te=in[strlen(in)-1];
		in[strlen(in)-1]='\0';
		
	}
	//printf("OUT\n");
	//cout<<in;
	if(bo[0]>'0')
	myfile<<bo[0];//printf("%c",bo[0]);
	for(i=1;i<=strlen(bo);i++)
	{
		//printf("%c",bo[i]);
		myfile<<bo[i];
	}
	myfile<<"\n";//printf("\n");
	return 0;
}

int main()
{
	myfile.open ("example.txt");
	char inp[100];
	int tesres;
	cin>>tesres;
	for(int j=1;j<=tesres;j++)
	{
		cin>>inp;
		//printf("Case #%d: ",j);
		myfile<<"Case #"<<j<<": ";
		thi(inp);
	}
	myfile.close();
	return 0;
}
