#include<iostream>
#include<vector>
using namespace std;
int main()
{
 int t,i,j,k,n;
 cin>>t;
 string s;
 vector<int> z;
 for(int l=0;l<t;l++)
 {
  cin>>s;
  cin>>k;
  n=s.length();
  //cout<<n<<endl;
  cout<<endl;
  int c=0,d=0,ctr=0;
 // while(ctr2!=ctr){
  //ctr2=ctr;
  for(i=0;i<=n-k;i++)
  {
   c=0;d=0;
   
   if(s[i]=='-')
    {
      ctr++;
      for(j=i;(j<i+k);j++)
       {
        if(s[j]=='-')
         s[j]='+';
         else
         s[j]='-';
       }
    }

    
  //}
  }
  c=0;
  for(i=0;i<n;i++)
  {
   if(s[i]=='-')
     {
      c=1;
      break;
     }
  }
  
  if(c==1)
   {
    z.push_back(-1);
   }
   else
   {
    z.push_back(ctr);
   }
 }
 for(i=0;i<z.size();i++)
 {
	 if(z[i]==-1)
	  cout<<"Case #"<<i+1<<": IMPOSSIBLE"<<endl;
	 else
	  	  cout<<"Case #"<<i+1<<": "<<z[i]<<endl;

 }
 return 0;
}
