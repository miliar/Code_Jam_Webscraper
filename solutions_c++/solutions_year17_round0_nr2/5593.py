#include<iostream>
#include<math.h>
#include<conio.h>
using namespace std;
int main()
{
		freopen("B-large.in","r",stdin);
	freopen("out6.txt","w",stdout);
	int t,m,r,count,d,s,x=1;
	long long i,n,tidy,p,j,z,k;
	cin>>t;
	while(t--)
	{
		cin>>n;
		s=0;
		for(z=n;z>0;z=z/10)
		{
			s++;
		}
		
		for(i=n;i>0;i--)
		{   
		    
		 p=pow(10,(s-1));
		 if(p==i)
		 {
		 	s=s-1;
		 }
			j=i;      
			count=0;
			d=0;
			m=0;
			while(p>0)
			{                                                                                                                                                                        ;
			    r=j/p;            
			     if(r>=m)         
			     {
			     	count++;     
			     }
			     else
			     {   k=pow(10,(s-count));
			     	i=i-(i%k);
			     	m=0;
			     }
			     d++;             
			     m=r; 
				 j=j%p; 
				 p=p/10;          

		    }
		    
		    if(count==d)
		    {
		    	tidy=i;
		    	break;
		    }
		}
		cout<<"Case #"<<x<<": "<<tidy<<endl;
		x++;
	}
	return 0;
}
