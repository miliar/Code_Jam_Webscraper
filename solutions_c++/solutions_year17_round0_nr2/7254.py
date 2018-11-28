#include<iostream>
#include<string>
using namespace std;

int main()
{
  int t;
  cin >>t;
  for(int k=1;k<=t;k++)
    {
      string s;
      cin >> s;

      int l=s.length();
      int rev;
      int flag=0;
      if(l>1)
	{
	  for(int i=0;i<l-1;i++)
	    {
              if(s[i]>s[i+1])
		{ flag=1;
		  rev=i;
		  //s[i]=s[i]-1;
		  for(int j=i+1;j<l;j++)
		    s[j]='9';
		  break;
		}
	      }
	  if(flag)
	    {while(rev>0&&s[rev]==s[rev-1])
		s[rev--]='9';
	      s[rev]=s[rev]-1;
	    }}
      int i=0;
      while(i<l)
	{if(s[i]!='0')break;
      i++;}
      cout<<"Case #" <<k << ": "<<s.substr(i)<<endl;
	  

    }

}
