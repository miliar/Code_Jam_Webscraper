#include<bits/stdc++.h>
using namespace std;
void asc(long long int dig[],long long int &sol,long long int i,long long int count,long long int num){
	if(i==count-1)
	{
		//only one element
		if(i==0)
		{
		    int j=9;
		    while(1){
			    if((sol*10+j)<=num){
				sol=sol*10+j;
				break;
			}
			else
			  j--;
		}
		return;
	    }
	    else
	    {
	    	if(dig[i]>=dig[i-1]){
	    	     int j=9;
		         while(1){
			       if((sol*10+j)<=num){
				  sol=sol*10+j;
				   break;
			    }
			    else
			      j--;
		}
		return;	
			}
			else{
			     dig[i-1]--;
			     for(int k=i;k<count;k++)
			       dig[k]=9;
			     sol/=10;
			     i--;
			     asc(dig,sol,i,count,num);	
			}
		}
	    
    }
	else
	{
	  if(i==0)
	  {
		sol=sol*10+dig[i];
		asc(dig,sol,i+1,count,num);
	  }	
	  else
	  {
		if(dig[i]>=dig[i-1]){
			sol=sol*10+dig[i];
			asc(dig,sol,i+1,count,num);
		}
		else{
			dig[i-1]--;
			for(int k=i;k<count;k++)
			  dig[k]=9;
			sol/=10;
			i--;
			asc(dig,sol,i,count,num);
		}
      }
   }
	
}
int main()
{
	freopen("a.in","r",stdin);
    freopen("b.out","w",stdout);
	int t;
	long long int num;
	cin>>t;
	for(int i=1;i<=t;i++)
	{
		cin>>num;
		long long int count=0,temp=num;
		while(temp!=0)
		{
			temp/=10;
			count++;
		}
		long long int *digit=new long long int[count];
		long long int sol=0;
		long long int a=count;
		temp=num;count--;
		while(temp!=0)
		{
			digit[count--]=temp%10;
			temp/=10;
		}
		asc(digit,sol,0,a,num);
		/*for(int i=0;i<a;i++)
		 cout<<digit[i]<<" ";
		int num3=0;
		for(int j=1;j<a;j++)
		{
			num3=num3*10+9;
		}
		int ans;
		if(num3>sol && num3<=num)
		   ans=num3;
		else
		  ans=sol;*/
		cout<<"Case #"<<i<<": "<<sol<<endl;
	}
	return 0;
}

