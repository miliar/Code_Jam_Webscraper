
#include<iostream>
#include<math.h>
using namespace std;
int main()
{
	long long int T,NT[100];
	cin>>T;
	
	
	for(long long int i=0;i<T;i++)
	cin>>NT[i];
	
	
	for(long long int i=0;i<T;i++)
	{long long int r,n=NT[i],p;
	long long int NTsplit[]={-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1};
		NT[i]++;
	while(NT[i]>1)
	{
		NT[i]--;
		n=NT[i];
		long long int j=0,b=0;
		 while(n!=0)
    	{
               r=n%10;
               n=n/10;
               NTsplit[j]=r;
               j++;
        
    	}
    	if(j==1)
    	break;

			for(long long int k=0;k<j-1;k++)
			 {
			 if(NTsplit[k]>=NTsplit[k+1])
			 {
			 	if(k!=j-2)
			 	continue;
			 	else if(k==j-2)
			 	{
			 		b--;
			 		break;
			 	}
			}
			else if(NTsplit[k]<NTsplit[k+1])
			break;
		}
		
		if(b<0)
		break;
}
	cout<<"Case #"<<i+1<<": "<<NT[i]<<endl;
	}
	
}
