#include<iostream>
#include<limits.h>
using namespace std;

int get_ls(int *occ,int n,int s)
{
int ls=0;
for(int j=s-1;j>0;j--)
	{
	if(occ[j]==0)
		ls++;
	else 
		break;
	}
return ls;
}
int get_rs(int *occ,int n,int s)
{
int rs=0;
	for(int j=s+1;j<n+1;j++)
	{
		if(occ[j]==0)
			rs++;
		else
			break;
	}
return rs;
}

int getmin(int a,int b)
{
if(a<b)
	return a;
else
	return b;
}
int getmax(int a,int b)
{
if(a>b)
	return a;
else
	return b;
}
int main()
{
int T;
cin>>T;
for(int l=0;l<T;l++)
{
int n,k,ans1,ans2,p;
cin>>n>>k;
int *occ=new int[n+2];
int *choice1=new int[n+2];
int *choice2=new int[n+2]; 
for(int i=0;i<n+2;i++)
	occ[i]=0;
occ[0]=occ[n+1]=1;

for( p=0;p<k;p++)
{
int maxmin=-1,ans,maxmax=-1;
for(int s=1;s<n+1;s++)
	{	
	int ls=0,rs=0;
	if(occ[s]!=0)
		continue;
	ls=get_ls(occ,n,s);
	rs=get_rs(occ,n,s);
	choice1[s]=getmin(ls,rs);
	choice2[s]=getmax(ls,rs);
	if(choice1[s]>maxmin)
		{
		maxmin=choice1[s];
		}
	}
for(int s=1;s<n+1;s++)
	{
if(occ[s]!=0)
	continue;
	if(choice1[s]==maxmin)
		{
		if(choice2[s]>maxmax)
			{
			maxmax=choice2[s];
			}
		}
	}
for(int s=1;s<n+1;s++)
	{
if(occ[s]!=0)
	continue;
	if(maxmax==choice2[s] && choice1[s]==maxmin)
		{
			ans=s;
			break;	
		}
	}
occ[ans]=1;
ans1=choice1[ans];
ans2=choice2[ans];
}
cout<<"Case #"<<l+1<<": "<<ans2<<" "<<ans1<<endl;
}

return 0;
}
