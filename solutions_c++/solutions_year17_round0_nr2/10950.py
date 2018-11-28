#include<iostream>
using  namespace std;

int main()
{
	int T=0,N=0,temp=0,temp1=0,ld1=0,ld2=0,flag=0,max_no;
	cin>>T;
	for (int i = 1; i <= T; i++)
	{
    	cin>>N;
		
		
		for (int j = 1; j <= N; j++)
		{
		    temp=j;
			while(temp!=0)
			{
				ld1=temp%10;
				temp1=temp/10;
				ld2=temp1%10;
				if (ld2<=ld1)
				{
					flag=1;
				}
				else
				{
					flag=0;
					break;
				}
			
			    temp=temp/10;
			}
			if (flag==1)
			{
				max_no=j;
			}
			
		}
		cout<<"Case #" << i << ": "<<max_no<<"\n";
	    
	}
	return 0;
}	
