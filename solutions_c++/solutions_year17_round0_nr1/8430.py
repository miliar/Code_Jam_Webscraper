#include<iostream>
#include<conio.h>
using namespace std;
int flip(char &a)
{
	if(a=='+')
	a='-';
	else if(a=='-')
	a='+'; 
}
int main()
{
	int t,i=0,c=0,s=0,k[100],m,n,f=0;
	k[0]=3;
	char a[100][1000];
	cin>>t;
	cin.getline(a[s],20);
 	for(s=0;s<=t-1;s++)
	{   
	 	
	  	cin.getline(a[s],20,' ');
	  	cin>>k[s];

	}
    for(s=0;s<=t-1;s++)
    {   
        i=0;c=0;
        n=k[s]-1;
    	while(a[s][i+n]!='\0')
    	 {
    	    if(a[s][i]=='-')
    	    {
    	    	c++;
    	    	for(m=0;m<=(k[s]-1);m++)
			     flip(a[s][i+m]);

    	    }
    	    i++;
	     } 
	     cout<<"Case #"<<s+1<<": ";
	     for(m=0;m<=(k[s]-2);m++)
	     if(a[s][i+m]=='-')
	     {
		  cout<<"IMPOSSIBLE\n";
		  f=1;
		  break;
		 }
		 if(f==0)
		 {
		 	cout<<c<<"\n";
		 	
		 }
		 f=0;
		 
	}
}
