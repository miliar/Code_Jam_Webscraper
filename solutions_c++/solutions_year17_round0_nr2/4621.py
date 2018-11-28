#include<bits/stdc++.h>
using namespace std;
int main()
{ freopen("B-small-attempt1.in","r",stdin);
    freopen("output.out","w",stdout);
  int i,j,k,n,m,t,z=1;
  string s,s1,s2;
  cin>>t;
  while(t)
  {cin>>s;
  for(i=0;i<s.length();i++)
  {  if(s[i]<=s[i+1]|| i==s.length()-1)
     { s1[i]=s[i];
	 }
	 else
	 { if(s[i]-1==48)
	   {  for(j=i;j>=0;j--)
	      {  if(s[j]-1==48 && j!=0)
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
		  }
	 }
  }
   for(i=0;i<s.length()-1;i++)
   {  if(s1[i]>s1[i+1])
      {s1[i]=s1[i+1];
        for(j=i+1;j<s.length();j++)
         s1[j]=57;
      }
   }		  
  int f=0;
  cout<<"Case #"<<z<<": ";
  for(i=0;i<s.length();i++)
   { if(s1[i]!=48 || f!=0)
     { cout<<s1[i];
       f=1;
	 }
   }
   cout<<"\n";
   z++;
   t--;
  }
}
