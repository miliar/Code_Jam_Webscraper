#include<iostream>
#include<fstream>
using namespace std;
typedef unsigned long long int ll;
int dd[20]={0},len;
void digits(ll n);
void arrange();
ll formnum();
ifstream fin("rr.in");
ofstream fout("rr.out");
int main()
{
	int t;
	ll n,res;
	fin>>t;
	for(int i=0;i<t;i++)
	{
		fin>>n;
		digits(n);
		arrange();
		res=formnum();
		fout<<"Case #"<<i+1<<": "<<res<<endl;
	}
	return 0;
}

void digits(ll n)
{
	len=0;
	int rr[20];
	for(int i=0;i<20;i++)
		dd[i]=0;
	ll x=n;
	while(x>0)
	{
		rr[len++]=x%10;
		x/=10;
	}
	x=len;
	int i=0;
	while(len>=0){
		dd[i++]=rr[--len];
	}
	len=x;
}

void arrange()
{
	for(int i=len-1;i>0;i--){
		if(dd[i]>=dd[i-1])
			continue;
		else
		{
			dd[i-1]--;
			dd[i]=9;
			for(int j=i+1;j<len;j++)
				dd[j]=9;
		}
	}

}

ll formnum()
{
	ll res=dd[0];
	for(int i=1;i<len;i++)
	{	
		res=res*10+dd[i];
	}
	return res;
}
