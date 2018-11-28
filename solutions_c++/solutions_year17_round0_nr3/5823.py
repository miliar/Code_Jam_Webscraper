#include<iostream>
using namespace std;
int main()
{
	freopen("C-small-1-attempt1.in","r",stdin);
	freopen("out12.txt","w",stdout);
	int t,x=1,z=0;
	int n,k,i,count,l,m,l1,m1,s,p,q,r;
	cin>>t;
	while(t--)
	{   
		cin>>n>>k;
		
		int a[n+2];
		a[0]=1;
		a[n+1]=1;
		for(i=1;i<n+1;i++)
		{
			a[i]=0;
		}
		count=0;
	
		while(k--)
	    {
	    	s=0;
	    
		        for(i=0;i<n+2;i++)
		       {                     
		         	if(a[i]==0)
		            	{
		        		count++;       
			        	if(count==1)
			           	{ 
			         	   l1=i;       
				         }
		        	}
		         	else
		 	            {
			            	m1=i;         
							if(count==s)
							{   q=m;
								l=r;
								m=m1;
								if(q<m)     
								m=q;
								
							}       
				           if(count>s)
			               	{ 
					            r=l=l1;   
					            m=m1;
					              s=count;   
			             	}
							 	
			                	count=0;
		               	}
	             }
		if((m-l)%2==1)
		p=l+((m-l)/2);
		else
		p=l+((m-l)/2)-1;
		a[p]=1;
	    }
	    l1=0;m1=0;
	    for(i=p+1;i<n+2;i++)
	    {
	    	if(a[i]==0)
	    	l1++;
	    	else 
	    	break;
	    }
	    for(i=p-1;i>=0;i--)
	    {
	    	if(a[i]==0)
	    	m1++;
	    	else
	    	break;
	    }
	    if(l1>=m1)
		{
			l=l1;
			m=m1;
		}
		else
		{
			l=m1;
			m=l1;
		}			
		cout<<"Case #"<<x<<": "<<l<<" "<<m<<endl;
		x++;
	    }
	    
	    x++;
	}




