#include<iostream>
using namespace std;
int p1=0;
int v;
int p2=0;
int cap=0;
int a[100000];
void findspace(int n)
{
	p1=0;
    p2=0;
    cap=0;
	
	for(int i=1;i<n+3;i++)
	{
		if(a[i]==1)
		{
			int k=1;
			while(a[i+k]!=1 && i+k<=n+2)
			{
				k++;
			}
			if(k>cap)
			{
			 p1=i;
			 p2=i+k;
			 cap=k;
			 v=i+(k/2);
			}
		}
	}
}
int main()
{
		int n,k,ls,rs;
		int d=1;
		int u;
		cin>>u;
		while(d<=u)
		{
		cin>>n;
		for(int i=1;i<=n+2;i++)
		a[i]=0;
		a[1]=1;
		a[n+2]=1;
		cin>>k;
		cout<<"Case #"<<d<<": ";
		while(k>0)
		{
			findspace(n);
			 a[v]=1;
			k--;
		}
		for(int i=v+1;i<=n+2;i++)

		if(a[i]==1)
		{
			rs=i-v-1;
			break;
		}
		
		for(int i=v-1;i>0;i--)
		if(a[i]==1)
		{
			ls=v-1-i;
			break;
		}
		if(ls>=rs)
		cout<<ls<<" "<<rs<<endl;
		else
		cout<<rs<<" "<<ls<<endl;
	d++;
}
}
