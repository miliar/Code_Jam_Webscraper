#include<iostream>
#include<string>

using namespace std;

int main()
{
  int t,n,k;
  size_t f;
  string str;
  cin>>t;
  for(int p=1; p<=t; p++)
    {
      cin>>str>>k;
      n = str.length();      
      int count=0;
      while(1)
		{
		  f = str.find("-");
		  if(f==string::npos)
			break;
		  
		  for(int i=f; i<f+k; i++)
			if(str[i] == '-')
			  str.replace(i,1,"+");
			else
			  str.replace(i,1,"-");
		  count++;
		  
		  f = str.find("-");
		  if(f==string::npos)
			break;
		  
		  if(f+k>n)
			break;
		  
		}
	  f = str.find("-");
      cout<<"Case #"<<p<<": ";
	  
      if(f!=string::npos)
        cout<<"IMPOSSIBLE"<<endl;
      else
		cout<<count<<endl;
      
    }
}
