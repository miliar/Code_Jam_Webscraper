#include <bits/stdc++.h>
using namespace std;

int main() {
	int t,op;
	cin>>t;op=t;
	while(t--)
	{
	    string s;
	    int k;
	    cin>>s;
	    cin>>k;
	    int ans=0;
	    for(int i=0;i<=s.length()-k;i++)
	    {if(s[i]!='+')
	    {for(int j=i;j<i+k;j++)
	    {if(s[j]=='+')
	     s[j]='-';
	     else
	     s[j]='+';
	    }
	    ans++;    
	    }
	        
	    }
	    int flag=0;
	   
	 for(int i=0;i<s.length();i++)
	 if(s[i]=='-')
	 {cout<<"Case #"<< op-t<<": "<<"IMPOSSIBLE"<<endl;
	 flag=1;
	 break;
	 }
	 if(flag==0)
	 cout<<"Case #"<< op-t<<": "<<ans<<endl;
	}
}

