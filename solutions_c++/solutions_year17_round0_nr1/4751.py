#include<iostream>
#include<string>

using namespace std;

bool isok(string str)
{
    string pat="-";
    size_t found = str.find(pat);
    return (found==string::npos);
}


int main()
{
  int t,n,k;
  string str;
  cin>>t;
  for(int p=1; p<=t; p++)
    {
      cin>>str>>k;
      n = str.length();
      string pat="";
      
      int c=0;
      while(!isok(str))
	{	  
	  string pat="-";
	  size_t found = str.find(pat);
	  
	  for(int i=found; i<found+k; i++)
	    if(str[i] == '-')
	      str.replace(i,1,"+");
	    else
	      str.replace(i,1,"-");
	  c++;
	  
	  found = str.find(pat);
	  if(found==string::npos)
	    break;
	  
	  if(found+k>n)
	    break;
	  
	}


      printf("Case #%d: ",p);
      if(!isok(str))
        cout<<"IMPOSSIBLE\n";
      else
	cout<<c<<"\n";
      
    }
}
