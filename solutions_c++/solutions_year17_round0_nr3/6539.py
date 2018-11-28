#include<bits/stdc++.h>
using namespace std;
int lcalc(int bath[],int i)
{
	int count=0;
	for(int j=i-1;j>=0;j--)
	{
		if(bath[j]==0)count++;
		else
		if(bath[j]==1)break;
	}
	return count;
}
int rcalc(int bath[],int i,int n)
{
	int count=0;
	for(int j=i+1;j<n+2;j++)
	{
		if(bath[j]==0)count++;
		else
		if(bath[j]==1)break;
	}
	return count;
}
int main()
{
	freopen("a.in","r",stdin);
    freopen("b.out","w",stdout);
	int t,n,k,*bath,*sol,index;
	cin>>t;
	for(int i=1;i<=t;i++)
	{
		cin>>n>>k;
		bath=new int[n+2];
		sol=new int[n+2];
		for(int j=0;j<n+2;j++)
		  bath[j]=0;
		bath[0]=1;
		bath[n+1]=1;
		for(int j=0;j<k;j++)
		{
			for(int l=0;l<n+2;l++)
			  sol[i]=0;
			for(int l=0;l<n+2;l++)
			{
				if(bath[l]==0)
				    sol[l]=min(lcalc(bath,l),rcalc(bath,l,n+2));
				else
				   sol[l]=-1;
			}
			int h=INT_MIN;
			int count=0;
			int ind=0;
			for(int l=0;l<n+2;l++)
			{
				if(h<sol[l]){
			  	h=sol[l];
			  	ind=l;
			    }  
			}
			for(int l=0;l<n+2;l++)
			  if(sol[l]==h)count++;
			if(count<=1){
				bath[ind]=1;
				index=ind;
			}
			else
			{
			    for(int l=0;l<n+2;l++)
			     {  
				    if(bath[l]==0 && sol[l]==h)
				       sol[l]=max(lcalc(bath,l),rcalc(bath,l,n+2));
			     }
				 h=INT_MIN;
			     ind=0;
			     for(int l=0;l<n+2;l++)
			     {
				    if(h<sol[l]){
			  	    h=sol[l];
			  	    //count++;
			  	    ind=l;
			       }  
			     }
			    bath[ind]=1;
				index=ind;   	
			}
				
		}
			
		/*for(int j=0;j<n+2;j++)
		  cout<<bath[j]<<" ";*/	
		cout<<"Case #"<<i<<": "<<rcalc(bath,index,n+2)<<" "<<lcalc(bath,index)<<endl;
		
	}
	return 0;
}
