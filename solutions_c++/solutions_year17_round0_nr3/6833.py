#include<bits/stdc++.h>
#include<iostream>
using namespace std;

int minl(int a[], int pos)
{
	int count=0;
	for(int i=pos-1;i>=0;i--)
	{	
		if(a[i]==0)
			count++;
		else
		 return count;
	}
	return count;
}

int minr(int a[], int pos,int n)
{
	
	int count=0;
	for(int i=pos+1;i<n;i++)
	{	
		if(a[i]==0)
			count++;
		else
		 return count;
	}
	return count;
}

int min(int a, int b)
{
	if(a>=b)
		return b;
	return a;
}

int max(int a, int b)
{
	if(a>=b)
		return a;
	return b;
}



main()
{
	int t;
	cin>>t;
	long long int a[101];
	long long int b[101]; 
	for(int i=0;i<t;i++)
	{
		cin>>a[i]>>b[i];
	}
		
	
	int pos;
	for(int z=0;z<t;z++)
	{
		int N;
		N=a[z];
		int a[N+2]={0};
	
		int large=0;
		a[0]=1;
		a[N+1]=1;
		
		int people;
		people=b[z];
		
		for(int j=0;j<people;j++)
		{
			pos=0;
			large=0;
			int lar=0;
				for(int i=1;i<N+1;i++)
				{
					if(a[i]==0)
					{
				
						int m=min(minl(a,i), minr(a,i,N+2));
						if(m>=large)
						{
							large=m;
							pos=i;
						}
					}
				}
				
		
				for(int i=N;i>=1;i--)
				{
					if(a[i]==0 && min(minl(a,i), minr(a,i,N+2))==large)
					{
						if(max(minl(a,i), minr(a,i,N+2))>=lar)
						{
							lar=max(minl(a,i), minr(a,i,N+2));
							pos=i;
					
						}
					}
				}
		
				a[pos]=1;
				
			
				if(j==people-1)
				{
					cout<<"Case #"<<z+1<<": "<<max(minl(a,pos), minr(a,pos,N+2))<<" "<<min(minl(a,pos), minr(a,pos,N+2))<<endl;;
			
				}
	}
		
		
		
		
	}//end of test loop
}
