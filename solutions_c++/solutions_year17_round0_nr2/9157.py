#include<iostream>
using namespace std;
main()
{
	int T,a[20],t,p,q,flag;
	long long N,i,j,tn;
	cin>>T;
	for(t=1;t<=T;t++)
	{ 
	  cin>>N;
	  for(i=N;i>=1;i--)	
	  { 
	    p=0; j=i;
	    flag=1;
		while(j)
	  	{ a[p]=j%10;
	  	  p++;  j=j/10;
		}
	    for(q=0;q<p-1;q++)if(a[q]<a[q+1])flag=0;
		if(flag){tn=i; break;}	
	  }
	  cout<<"Case #"<<t<<": "<<tn<<endl;
	}
}
