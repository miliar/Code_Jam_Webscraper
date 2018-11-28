#include<bits/stdc++.h>
using namespace std;
int main(){
	freopen("A-large.in", "r", stdin);
	
	int t,k;cin>>t;
	string s;
	for(int v=1;v<=t;v++){
		int c=0,i=0;
		cin>>s;
		cin>>k;
		cout<<"Case #"<<v<<": ";
		for( i=0;i<s.length()-k;i++){
			if(s[i]=='-')
			{
				int j=0;
				while(j<k){
					if(s[i+j]=='+')
					s[i+j]='-';
					else
					s[i+j]='+';
					j++;}
				c++;
				}
			}
			int x=0,f=0;
			//cout<<s;
			if(s[i]=='-'){
				for(;i<s.length();i++)
				if(s[i]=='-')
				x++;
				//cout<<x;
				if(x==k)
				c++;
				else
				{f=1;
				cout<<"IMPOSSIBLE"<<'\n';
		}
			}
			else
	{	for(;i<s.length();i++)
				if(s[i]=='+')
				x++;
				//cout<<x;
				if(x!=k)
				{f=1;
				cout<<"IMPOSSIBLE"<<'\n';
		}
			}		
			
			if(f==0)
			cout<<c<<'\n';
		
		}
		}
		
	
