#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;
int main()
{ 
	freopen("B-small-attempt0.in","r",stdin);
    freopen("output.out","w",stdout);
  
  string s,s1,s3,s2;
  long long int i,j,k,n,m,t,z=1;
  cin>>t;
  while(t)
  {
  	cin>>s;//cout<<s;
  	int zxw=0;
  	for(i=0;i<s.length();i++)
  	{  
	  if(s[i]<=s[i+1]|| i==s.length()-1)//cout<<s1[i];
     { s1[i]=s[i];
	 }
	 else
	 { if(s[i]-1==48)
	   {  for(j=i;j>=0;j--)
	      {  if(s[j]-1==48 && j!=0)//cout<<s1[j];
	         { s1[j]=57;
			 }
			 else
			 { s1[j]=s[i]-1;
			   break;
			 }
		  }
	   }
	   else
	   s1[i]=s[i]-1;
	   for(i=i+1;i<s.length();i++)
		  { //cout<<"h";
		    s1[i]=57;
		  }//cout<<s1[j];
	 }
  }
  long long int sdef=0;
   for(i=0;i<s.length()-1;i++)
   {  if(s1[i]>s1[i+1])
      {s1[i]=s1[i+1];
        for(j=i+1;j<s.length();j++)//cout<<s1[j];
         s1[j]=57;
      }
   }		  
  
  cout<<"Case #"<<z<<": ";
  int f=0;
  for(i=0;i<s.length();i++)
   { if(s1[i]!=48 || f!=0)
     { cout<<s1[i];
       f=1;
	 }
   }
   cout<<"\n";//allenite
   z++;
   t--;
  }
}
