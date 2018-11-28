#include<iostream>

using namespace std;

long int check(long int);
int main()
{
	long int x=1,y,ans,T;
	cin>>T;
	while(x<=T)
	{
		cin>>y;
		ans=check(y);
		if(y=='\0')
		break;
    	cout <<"Case #"<<x<<": "<<ans<<endl;
    	x++;
	}
	return 0;
}
long int check(long int y)
{
	long int i,k,last,prev,flag;
	i=y;
	if(y/10==0)
	return y;
	while(i>0)
	{
	k=i;
	prev=k%10;
	k=k/10;
	while(k>0)
	{   flag=0;
		last=prev;
		prev=k%10;
		if(last<prev)
		{
		 flag=1;
		 break;
	    }
     	k/=10;
 	}
 	if(flag==0)
 	{
 		break;
	}
	i--;
   }
   return i;
}
