#include<iostream>
#include <fstream>
#include<string.h>
using namespace std;
int Cont(char*T)
{
	int i;
	for(i=0;T[i]&&T[i]!='-';i++);
	return T[i];
}
void getPos(char*T,int&x,int m)
{
	int n=strlen(T);
	int i=0,j;
	
	for(i=n-1;i>=0;i--)
	{
		if(T[i]=='-')
		break;
	}
	if(i<0)
	{
		return;
	}
	if(i<m-1)
	{
		if(Cont(T))
		x=-1;
		return;
	}
	for(j=i;j>i-m;j--)
	{
		T[j]=T[j]=='+'?'-':'+';
	}
	x++;
	
	getPos(T,x,m);
}



int main(int narg,char*args[])
{
	int T,i,x=0;
   int n;
	char X[1001];
	cin>>T;
	for(i=0;i<T;i++)
	{
	cin>>X;
	cin>>n;
		getPos(X,x,n);
		if(x==-1)
		cout<<"Case #"<<i+1<<": IMPOSSIBLE";
		else
		cout<<"Case #"<<i+1<<": "<<x;
		x=0;
		if(i+1!=T)
		cout<<"\n";
	}
	//printCase(1,1692);
}
