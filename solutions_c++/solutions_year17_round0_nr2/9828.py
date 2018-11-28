#include<bits/stdc++.h>
using namespace std;
typedef long long int ll;
int main()
{
    freopen("B-small-attempt0.in","r",stdin);
    freopen("output.out","w",stdout);

  string s,s1,s3,s2;
  ll i,j,k,n,m,t,z=1;
  cin>>t;
  while(t)
  {
      int nitxyz=99;
  	cin>>s;   // input  a string
  	for(i=0;i<s.size();i++) // loop uptil lengh of string
  	{
	  if(s[i]<=s[i+1]|| i==s.size()-1)
        s1[i]=s[i];

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
	   for(i=i+1;i<s.size();i++)
		    s1[i]=57;
	 }
  }
      int abhix=0;
   for(i=0;i<s.size()-1;i++)
   {  if(s1[i]>s1[i+1])
      {s1[i]=s1[i+1];
        for(j=i+1;j<s.size();j++)
         s1[j]=57;
      }
   }

  cout<<"Case #"<<z<<": "; // for printiting case
  int f=0;
  for(i=0;i<s.size();i++)
   { if(s1[i]!=48 || f!=0)
     { cout<<s1[i];
       f=1;
	 }
   }
   cout<<"\n";
   z++;
   t--;  // dec of loop
  }
}
