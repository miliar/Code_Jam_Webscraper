#include<iostream>
#include <fstream>
#include<string.h>
#include<vector>
#include <algorithm> 
using namespace std;
void trier(char *T,int pos)
{
	char tmp;
	int i,j;
	for(i=pos;i<19;i++)
	{
		for(j=i+1;j<19;j++)
		{
			if(T[j]<T[i])
			{
				tmp=T[j];
				T[j]=T[i];
				T[i]=tmp;
			}
		}
	}
}
int populate(unsigned long long int n,char*T, char*R)
{
	int i=18;
	do
	{
		R[i]=T[i]=n%10;
		i--;
		n/=10;
	}while(n);
	return i;
}

int Check(char *T,char *R,int pos)
{
	int i;
	for(i=pos;i<19&&R[i]>=T[i];i++);
	if(i==19)
	return 1;
	return 0;
}
int aqual(char *T,char *R,int pos)
{
    int i;
	for(i=pos;i<19&&R[i]==T[i];i++);
	if(i==19)
	return 1;
	return 0;	
}
int doit(char*T,char *R,int pos)
{

	trier(R,pos);

	int x=pos+1,y;
	if(aqual(T,R,pos))
	return x;
	y=x;
	R[x]=T[x];
	int i;
	for(i=x;i<19;)
	{
		if(Check(T,R,pos))
		R[i]=(R[i]+9)%10;
		
		else
		{
		if(R[i]==0)
		 y++;
		 i++;
		 R[i]=9;	
		}
		
	}
	return y;
}

int main()
{
	unsigned long long int n;
	unsigned int cs,i;
	
	
	int flag=0;
	cin>>cs;
	for(i=0;i<cs;i++)
	{
		cin>>n;
	if(n/10==0)
	{
		cout<<"Case #"<<i+1<<": "<<n<<"\n";
	}
	else
	{
	char T[19]={0};
	char Rx[19]={0};
	int x=populate(n,T,Rx);
	int y=doit(T,Rx,x);
	cout<<"Case #"<<i+1<<": ";
	for(int j=y;j<19;j++)
	{
		cout<<(int)Rx[j];
	}
	
	cout<<"\n";
	}
	}
	return 0;
}
