#include<iostream>
#include<vector>
using namespace std;

char trans(char a)
{
	if(a=='9')
		return '8'; 
	else if(a=='8')
		return '7';
	else if(a=='7')
		return '6';
	else if(a=='6')
		return '5';
	else if(a=='5')
		return '4';
	else if(a=='4')
		return '3';
	else if(a=='3')
		return '2';
	else if(a=='2')
		return '1';
	else if(a=='1')
		return '0';
	else if(a=='0')
		return '9';
}/*
void print()
{
	if(flag==true)
		{
			cout<<"Case #"<<i+1<<": "; 
			for(int b=0;b<strlen(st)-1;b++)
				cout<<st[b];
			cout<<endl;
			flag=false;
		}
		else{
			cout<<"Case #"<<i+1<<": "; 
			for(int b=0;b<strlen(st);b++)
				cout<<st[b];
			cout<<endl;}
}*/
int main()
{
	int n;
	cin>>n;
	for(int i=0;i<n;i++)
	{
		int flag=false;
		char st[20];
		cin>>st;
		while(flag==false)
		{
			if(strlen(st)==1)
				break;
			for(int j=0;j<strlen(st);j++)
			{
				if(j==strlen(st)-1)//마지막 체크 안함
					break;
				
				if(st[j]>st[j+1])
				{
					flag=false;
					st[j]=trans(st[j]);
					for(int a=j+1;a<strlen(st);a++)
					{
						st[a]='9';
					}
					break;
				}
				flag=true;
			}
		}
		if(strlen(st)==1){
			cout<<"Case #"<<i+1<<": "; 
			cout<<st[0]<<endl;
		}
		else{
		cout<<"Case #"<<i+1<<": "; 
		for(int j=0;j<strlen(st);j++){
			if(st[j]=='0')
				continue;
			cout<<st[j];}
		cout<<endl;
		}
	}
}