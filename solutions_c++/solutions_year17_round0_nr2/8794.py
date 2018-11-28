#include <iostream>
using namespace std;

int main() {
	int r=1,t,n,a;
	cin>>t;
	while(r<=t)
	{
		cin>>n;
		a=n;
		int m = a%10,count=0,digits = 0,flag=0;
		a=a/10;
		while(a!=0)
		{
			flag=1;
			digits++;
			if(a%10>m)
			{
				count=digits;
			}
			
			else if(a%10 == m && count>0)
			count=digits;
			
			m=a%10;
			a=a/10;
			
		}
	//	count--;
		int position=1,sub;
		for(int i=0;i<count;i++)
		position=position*10;
		
		if(flag)
        {
        	if(count)
        	sub=1;
        	else
        	sub=0;
        }
        else
        {
          	sub=0;
        }
       
		int decrease = (n+sub)%position;
		 
		cout<<"Case #"<<r<<": "<<n-decrease<<endl;
		r++;
	}
	return 0;
}