#include<iostream>
#include<string>
using namespace std;

int main()
{
  int t;
  cin >>t;
  for(int u=1;u<=t;u++)
    {
      string s;
      int k;
      cin >> s>>k;
      int l=s.length();
      int count =0;
      for(int i=0;i<l-k+1;i++)
	{ 
	  if(s[i]=='-')
	    {
	      count++;
	      for(int j=0;j<k;j++)
                if(s[i+j]=='-')
		  s[i+j]='+';
		else
		  s[i+j]='-';
	    }


	}
      int flag=0;
      for(int i=0;i<l;i++)
	if(s[i]=='-')flag=1;
      if(flag)
	cout <<"Case #"<<u<<": IMPOSSIBLE"<<endl; 
	  else
      cout <<"Case #"<<u<<": "<< count <<endl;


    }




}
