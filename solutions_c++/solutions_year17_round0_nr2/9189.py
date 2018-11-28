#include<iostream>
#include<cmath>
using namespace std;
int no;
bool check(int ch[])
{
	
	int j;
	
	for(j=1;j<no;j++)
	{
		if(ch[j-1]<ch[j])
		return 0;
	}
	return 1;
	
}

int * arranged(int a[],int n)
{       if(n<0)
          return a;
        bool flag;
	    flag=check(a);
	    
	    if(flag)
		return a;
		
		long long int digit,pdigit;
		
		  digit=a[n];
			
		  pdigit=a[n+1];
		  			

             a[n]=9;

			if(pdigit)
			{
				a[n+1]--;
				
				
			}
			
			n++;
			a=arranged(a,n);
		
		return a;
	 
}
int main()
{
	long long int a;
	int t;
	cin>>t;
	for(int ti=0;ti<t;ti++)
	{
		cin>>a;
		long long int temp=a;
	
		for(no=0;temp!=0;temp/=10)
		no++;
		int ch[20];
	int i,j;
	for( i=0;a!=0;a=a/10)
	{  
		ch[i]=a%10;
		i++;
		
	}  int * chr;
		
		chr=arranged(ch,0);
		cout<<"Case #"<<ti+1<<": ";
		for(i=no-1;i>=0;i--)
		{
			if(i<no-1)
		cout<<chr[i];
		else{
			if(chr[i]!=0)
			cout<<chr[i];
		}}
		cout<<endl;
		
	 } 
	 return 0;
}
