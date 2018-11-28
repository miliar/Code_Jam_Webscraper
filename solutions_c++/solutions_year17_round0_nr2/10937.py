#include<iostream>
#include<math.h>
using namespace std;
int main()
{


//tt bs ye store kr rha ki kitne cases h(output me dikhane ke liey, & nn me input ko dobara store kiya
	
	int tt,t,n,temp1,temp2,j,m,nn,q;
	
	cin>>t;
	tt=t;
	while(t)
	{
	
	cin>>n;
	nn=n;
	j=0,m=0;
	
		temp1 = n%10;
		n = n/10;
		m++;
		
	while(n>0)
	{
	
		temp2 = n%10;
		n = n/10;
		m++;
		if(temp2>temp1)
		 j=m;	
		
		temp1=temp2;
		

  }  
 
 
 
if(j>1)
{
		nn = nn/pow(10,j-1);
 q = nn%10;
	nn=nn/10;
	nn= (nn*10+q-1)*pow(10,j-1);
	

	
	 q=9;
	for(int i=0;i<j-2;i++)
	q = q*10+9;
	nn =nn+q;
	
}

		cout<<"Case #"<<tt-(--t)<<": "<<nn<<endl;
	

	
	
		
}	





}

