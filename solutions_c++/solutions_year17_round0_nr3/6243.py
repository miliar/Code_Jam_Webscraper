#include<bits/stdc++.h>
using namespace std;
int main()
{
        //ofstream myfile;
        //myfile.open ("mycode2.txt");
	long long int t,it=1;
	cin>>t;
	while(t!=0)
	{
		long long int n,k;
		cin>>n>>k;
		long long int x=(log2(k));
		long long int a,b,c,d;
		if(n%2==0)
		{
			a=(n/2)-1;
	                b=(n/2);
			c=1;
			d=1;
		}
		else
		{
			a=(n/2);
                        b=(n/2);
			c=1;
			d=1;
		}
		long long int t1,t2;
		for(int i=1;i<x;i++)
		{
			int not1=0,not2=0;
			
		
				if(a%2==0)
				{
		                 a=(a/2)-1;
		                 t1=c;
			         not1=1;
				}
		                else
				{
			         a=a/2;
			         c=c*2;
				}
					
				if(b%2==0)
				{
					b=b/2;
					t2=d;
					not2=1;
				}
				else
				{

					b=b/2;
					d=d*2;
				}	
				if(not1==1)
				{
					d=d+t1;			
				}
				if(not2==1)
				{
					c=c+t2;
				}
			}
			long long int z=k-pow(2,x)+1,sol;
	        if(d>=z)
                sol=b;
                else
                sol=a;
		if(k==1)
		  sol=n;
		if(sol%2==0)
		  cout<<"Case #"<<it<<": "<<(sol/2)<<" "<<(sol/2)-1<<endl;
                  //myfile<<"Case #"<<it<<": "<<(sol/2)<<" "<<(sol/2)-1<<endl;
		else
		  cout<<"Case #"<<it<<": "<<(sol/2)<<" "<<(sol/2)<<endl;
                  //myfile<<"Case #"<<it<<": "<<(sol/2)<<" "<<(sol/2)<<endl;
           it++;
           t--;
	}
       //myfile.close();
       return 0;
}
