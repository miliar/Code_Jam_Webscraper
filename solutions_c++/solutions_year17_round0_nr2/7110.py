#include<stdio.h>
#include<iostream>
#include<fstream>
#include<string.h>
using namespace std;
main()
{
	int i,j,k,flag=0,t,u;
    char s[6];
	strcpy(s,"Case #");
	char f[2];
	strcpy(f,": ");
	unsigned long long n=0;
	int a[20];
	cin>>t;
	ofstream fout("fuckoff.txt",ios::app|ios::out);
	for(u=0;u<t;u++)
	{
	 i=0,j=0,k=0;
	cin>>n;
	while(n)
	{
		a[i]=n%10;
		n=n/10;
		i++;
	}
	for(j=0;j<i-1;j++)
	{
		if(a[j]<a[j+1])
		{
			a[j]=9;
			a[j+1]--;		
		}
	}
	fout<<s<<u+1<<f;
	cout<<"Case #"<<u+1<<": ";
	while(a[i-1]==0)
	i--;
	for(j=i-1;j>=0;j--)
	{
		if(a[j]==9){
		break;
	}
		printf("%d",a[j]);
		fout<<a[j];
	}
	
		for(k=j;k>=0;k--)
		{
			fout<<"9";
			printf("9");
		}
	fout<<"\n";
	printf("\n");
	}
	fout.close();
}
