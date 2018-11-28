#include<iostream>
#include<string>

using namespace std;
void invert(string &str,int l,int r)
{
	for(int i=l;i<r;i++)
	{ 		str[i]=(int('+'+'-')-(int)str[i]);	}
}
bool check(string s)
{
	for(int i=0;i<s.size();++i)
	{ 		if(s[i]=='-'){return false;		}	}
	return true;
}

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	string s;
	int n,t,i,j,k,ctrf,ctre;
	cin>>t;
	for(i=0;i<t;++i)
	{
	  cin>>s;
	  cin>>n;
	  string s1=s,s2=s;
	  ctrf=0;ctre=0;
	  //froward
      for(j=0;j<s1.size()-n+1;++j)  
      {
      	if(s1[j]=='-'){ invert(s1,j,j+n);++ctrf; 		  }
	  }
	  for(j=s2.size()-1;j>0+n-2;--j)  
      {
      	if(s2[j]=='-'){ invert(s2,j-n+1,j+1);++ctre; 		  }
	  }
	  
      if(check(s1)||check(s2))
      {
      	cout<<"case #"<<i+1<<": "<<min(ctrf,ctre)<<"\n";
	  }
	  else
	  { 	  	cout<<"case #"<<i+1<<": IMPOSSIBLE\n";	  }
	  
	}
	
	return 0;
}

