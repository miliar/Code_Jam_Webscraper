#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
#define OO 1e9
#define md 1000000007

int main()
{
  freopen("input.txt","r",stdin);
  freopen("output.txt","w",stdout);
  int t,k,flips;
  string str;
  bool notCorrect;


  cin>>t;
  for(int tt=1; tt<=t; tt++)
  {
	  notCorrect=false;
	  flips=0;

	  cin>>str>>k;
	  for(int i=0; i<str.size(); i++)
	  {
		  if((str[i]=='-') && ((i+k-1) <str.size()))
		  {
			  flips++;
			  for(int j=i; j<(i+k); j++)
			  {
				  str[j]= (str[j]=='-')?'+' : '-';
			  }
		  }
	  }

	  for(int i=0; i<str.size(); i++)
	  {
		  if(str[i]=='-')
		  {
			  notCorrect=true;
			  break;
		  }
	  }

	  if(notCorrect)
		  cout<<"Case #"<<tt<<": IMPOSSIBLE"<<endl;
	  else
		  cout<<"Case #"<<tt<<": "<<flips<<endl;

  }
  return 0;
}
