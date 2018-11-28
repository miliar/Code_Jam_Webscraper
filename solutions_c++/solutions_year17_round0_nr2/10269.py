#include<iostream>
using namespace std;
int asc(int);
int main()
{
	freopen("B-small-attempt1.in","r",stdin);
   freopen("practice.out","w",stdout);
	int T,N[100],i,val,chk;
	cin>>T;
	for(i=0;i<T;i++)
	{
	
		cin>>N[i];
	
	}
    for(i=0;i<T;i++)
	{
	
    val=asc(N[i]);			
	cout<<"Case #"<<i+1<<": "<<val<<endl;
	}

}
int asc(int n)
{
	int temp,store;
int ascending = 1;
store=n;

temp = n%10;

while (n>0)
{
    
	n = n/10;
    if (temp < n % 10)
    {
        ascending = 0;
    }
    temp=n%10;
}

if (ascending!=0)
	{
		
		return store; 
      
	}
else 
	{

	asc((store-1));
    }
}
