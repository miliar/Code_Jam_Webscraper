#include<bits/stdc++.h>
#include<iostream>
#define ll long long int
#define pb push_back
#define mp make_pair
//#define for(i,n) for(int i=0;i<n;i++)
#define start() int t;cin>>t;while(t--)
#define mod 1000000007

using namespace std;
int main(){
//	freopen("B-large.in","r",stdin);
//	freopen(" Tidy Numbers.txt","w",stdout);
	int count=0;
    start()
    {
    	string s;
    	cin>>s;
    	int c=-1;
    	for(int i=0;i<s.size()-1;i++)
    	{
    		if(s[i]>s[i+1])
    		{    c=i   ;
			     s[i]--;
    			for(int j=i+1;j<s.size();j++)
    			  s[j]='9';
			}
		}
		for(int i=c-1;i>=0;i--)
		{
			if(s[i]>s[i+1])
			{
				s[i]--;
				s[i+1]='9';
			}
		}
		if(s[0]=='0')
		{   count++;
		    cout<<"Case #"<<count<<": ";
			for(int i=1;i<s.size();i++)
			cout<<s[i];
			
			cout<<"\n";
		}
		else{
			count++;
		    cout<<"Case #"<<count<<": ";
		for(int i=0;i<s.size();i++)
			cout<<s[i];
			
			cout<<"\n";}
	}

}
