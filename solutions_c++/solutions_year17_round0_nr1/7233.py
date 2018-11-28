#include<bits/stdc++.h>
using namespace std;
#define pi 3.14159265358979323846
#define ull unsigned long long
#define ll long long
#define MOD 1000000007
int main(){
	#ifndef ONLINE_JUDGE
		freopen("inp.txt","r",stdin);
		freopen("out.txt","w",stdout);
	#endif
	int t,k;
	cin>>t;
	string s;
	int q=1;
	while(t--){
	cin>>s>>k;
	//cout<<s;
    int c=0,f=0;
	 for(int i=0;i<s.length()-k+1;i++)
     {
	 if(s[i]=='-'){
	 	c++;
	 for(int j=i;j<k+i;j++)
     {
      if(s[j]=='-')
	  s[j]='+';
	  else
	  s[j]='-';
	  
	 }
	}
	
	}
	
	 for(int i=0;i<s.length();i++)
      if(s[i]=='-')
     	{
		   f=1;
	    break;
		}
		
	if(f==1)
     cout<<"Case #"<<q<<": IMPOSSIBLE"<<endl;
    else
	 cout<<"Case #"<<q<<": "<<c<<endl; 
    q++;
	}
	return 0;
}

