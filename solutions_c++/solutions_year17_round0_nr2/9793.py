#include<bits/stdc++.h>
using namespace std;
int main()
{
    //ofstream govind;
    //govind.open("code1.txt");
	long long int T,t=0;
	cin>>T;
	while(T>0)
	
	{
    	long long int n,n1,n2;
     	cin>>n;
	    n1=n;
	    n2=n;
	    long long int value=10;
    	while(n!=0)
        	{
		     long long int x=n%10;
	       	 if(x<=value)
		       {
		         value=x;
		         n=n/10;
	           }
	         else
		       {
		       	n=--n2;
		       	n1=n;
		       	value=10;
		        ;
	           }
	
	        }
		cout<<"case #"<<++t<<": "<<n1<<endl;
		//govind<<"case #"<<++t<<": "<<n1<<endl;
		T--;
	}
	//govind.close();
}
