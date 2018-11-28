#include<bits/stdc++.h>
using namespace std;
int main()
{  freopen("input.in","r",stdin);
freopen("output.out","w",stdout);
  int t,p=1;
  cin>>t;
  while(t--)
  {
  	string s;int k,counter=0,v=0;
  	cin>>s;  cin>>k;   int g=s.size();
	  	for(int i=0;i<s.size();i++)
	  	{if(s[i]=='+') v++;
		  }                if(v==g) cout<<"Case #"<<p<<": 0"<<endl;

	   else{
			 bool flag=false;
	  int negpointer=0;
	   while(!flag)
	  {

	  if(s[negpointer]=='-'&&negpointer+k<=g)                                    //  outer for starts
	  {                                    //if starts
	  for(int j=negpointer;j<negpointer+k;j++)
	  {if(s[j]=='-') s[j]='+';
	  else if(s[j]=='+') s[j]='-';
	                  //  inner loop stps
	  }
	  counter++;}
	  if(s[negpointer]=='-'&&negpointer+k>g)   {break;
	  }
	  while(s[negpointer]!='-'&& negpointer<g)     //while starts
  	{   negpointer++; }
	  if(negpointer>=g) {
	  flag=true;}
}
	  //outer loop
					bool f=true;
					for(int i=0;i<s.size();i++)
					{if(s[i]=='-')
					{f=false;break;
					}}
				   if(!f){cout<<"Case #"<<p<<":"<<" IMPOSSIBLE"<<endl;
				   }
				   else{cout<<"Case #"<<p<<": "<<counter<<endl;
				   }
			}  // end of else
  p++;}



return 0;
}
