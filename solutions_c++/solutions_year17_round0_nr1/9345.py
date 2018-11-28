#include<iostream>
#include<fstream>
#include<string.h>
//#include<conio.h>
using namespace std;

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("largeoutput","w",stdout);
	int t,k,cnt=0,i,case_cnt=1,flag=0;
	char s[1001];
	cin>>t;
	while(t--)
	{
	  cin>>s>>k;
	// cout<<s<<"\n";
	  int l = strlen(s);
	  //cout<<l<<"\n";
	  for(i=0;i<l-k+1;i++)
	  {
	   if(s[i]=='-')
	   {
	   	//cout<<i<<"\n";
	   	int j=0,buf=i;
	   	while(j<k)
	   	{
	   	 if(s[buf]=='+')
	   	 {
	   	  s[buf] = '-';
	   	  buf++;
		 }
		 else
		 {
		 	s[buf]='+';
		 	buf++;
		 }
		 j++;
	   	}
	   	cnt++;
	   }
	  // cout<<s<<"\n";
	  }
	 // cout<<l-k+1<<"\n";
	  for(i=l-k+1;i<l;i++)
	  {
	  	if(s[i]=='-')
	  	{
	  	 cout<<"Case #"<<case_cnt<<": IMPOSSIBLE\n";
		 break;  	
	  	}
	  	if(i==l-1)flag=1;
	  }
	  if(flag)cout<<"Case #"<<case_cnt<<": "<<cnt<<"\n";
	  flag=0;
	  cnt=0;
	  case_cnt++; 
	}
    return 0;	
}

