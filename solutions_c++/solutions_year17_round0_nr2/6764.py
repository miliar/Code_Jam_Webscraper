#include <bits/stdc++.h>
using namespace std;

int main()
{
  freopen("B-large.in","r",stdin);
  freopen("B-large.out","w",stdout);
  int t;
  cin>>t;

  for(int k=1;k<=t;k++)
  {
  	long long num;
  	cin>>num;
  	long long temp=num;
  	long long temp2=num;
  	int l=1;
  	if(temp>9)
  	{
      for(l=1;temp>9;l++)
      {
      	temp=temp/10;
      }
  	}
   vector<long long>v(l);
   for(int i=l-1;i>=0;i--)
   {
   	temp2=num%10;

   	v[i]=temp2;
   	num=num/10;

   }

   if(l==1)
   {
      cout<<"Case #"<<k<<":"<<" ";
       cout<<v[0];
       cout<<"\n";
   }

else
  {
   for(int i=0;i<l;i++)
    {

        if(v[i]>v[i+1])
    	{
    	  	v[i]=v[i]-1;
    	  for(int j=i+1;j<l;j++)
    	  	{v[j]=9;}
    	  	i=i-2;
    	  	if(i<0)
            {i=-1;}

        }

   }

   if(v[0]==0)
   {
    cout<<"Case #"<<k<<":"<<" ";
  	for(int i=1;i<l;i++)
  		{cout<<v[i];}
  	cout<<"\n";
   }

  else
        {
            cout<<"Case #"<<k<<":"<<" ";
  	for(int i=0;i<l;i++)
  		{cout<<v[i];}
  	cout<<"\n";
        }

  }

  }
return 0;
  }
