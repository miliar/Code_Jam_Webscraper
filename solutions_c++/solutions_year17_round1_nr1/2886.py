#include<iostream>
#include<algorithm>
#include<stdlib.h>
using namespace std;

typedef long long int ll;
//cout<<"Case #"<<test<<": "<<i-1<<endl;


int main()
{

//freopen("input.in","r",stdin);
//freopen("output.txt","w",stdout);	

int test;
cin>>test;

for(int q=1 ; q<=test ; q++)
{
	
	int n,p;
	cin>>n>>p;
	
	int ig[n];
	int packet[n][p];
	
	
	for(int i=0 ; i<n ; i++)
	cin>>ig[i];
	
	for(int i=0 ; i<n ; i++)
	{
		for(int j=0 ; j<p ; j++)
		{
		cin>>packet[i][j];	
		}
	}
	
	int lower[n];
	int upper[n];
	
	
	
	
	for(int i=0 ; i<n ; i++)
	{
		lower[i]=(ig[i]*90)/100;
		upper[i]=(ig[i]*110)/100;
	}

int no_packets1[n][p];
int no_packets2[n][p];
int check[n][p];

for(int i=0 ; i<n ; i++)
{
	for(int j=0 ; j<p ; i++)
	{
		check[i][j]=0;
	}
}

for(int i=0 ; i<n ; i++)
{
	for(int j=0 ; j<p ; j++)
    { 
    if(packet[i][j]%lower[i]==0)
    no_packets1[i][j]=packet[i][j]/lower[i];
    
    if(packet[i][j]%upper[i]==0)
    no_packets2[i][j]=packet[i][j]/upper[i];
	
	else
	no_packets2[i][j]=packet[i][j]/upper[i]+1;	
    }
}

int temp,count=0;
for(int i=0 ; i<p ; i++)
{   check[0][i]=1;
    temp=no_packets1[0][i];
	for(int j=0 ; j<p ; j++)
    {
	if(temp>=no_packets2[1][j] && check[0][i]==0 && check[1][j]==0)
	
	{
	count++;
	check[1][j]=1;
	break;
    }
    
	}
}


cout<<count;

}	
	
	
}
