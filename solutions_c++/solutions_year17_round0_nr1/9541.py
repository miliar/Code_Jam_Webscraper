#include <bits/stdc++.h>
using namespace std;

int main() {
	
	long long int i,n,k,d,a,t,j=1,p=0;
	char s[500000];
	
	cin>>t;
	
	while(t--)
	{ 
		p=0;int c=0;
		cin>>s>>k;
		n=strlen(s);
		
		for(i=0;i<n-k+1;i++)
		 {
		 	if(s[i]=='-')// && (i+k-1)<n)
		 	  {
		 	  	for(a=i;a<k+i;a++)
		 	  	  {
		 	  	  if(s[a]=='+')
	 	            s[a]='-';
	           	else
	 	            s[a]='+';
		 	  	  	   
		 	  	  }
		 	  	 c++; 
		 	  }
		 }
		 
	//	 cout<<c;
		 for(i=0;i<n;i++)
		  { if(s[i]=='-')
		       p=1;
		   //  cout<<s[i];
		  }   
		   //cout<<p;    
	cout<<"Case #"<<j++<<": ";
	if(p!=1)
	  cout<<c;
	 else
	  cout<<"IMPOSSIBLE";
	 cout<<"\n"; 
		
	}
	
	return 0;
}
