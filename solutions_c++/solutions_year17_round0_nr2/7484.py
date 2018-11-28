#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;



int main() {
    int n,a[10000];
    cin>>n;
    string s[n];
    for(int i=0;i<n;i++)
    {
    	
    	cin>>s[i];
    	int m=s[i].length();
    	for(int j=m-1;j>0;j--)
    	{
    		if(s[i][j]<s[i][j-1]||s[i][j]=='0')
    		{
    			int k=0;
    			while(s[i][j+k]!='9'&&j+k<m)
    			{
    				s[i][j+k]='9';
    				k++;
    			}
    			s[i][j-1]=(char)((int)s[i][j-1]-1);
    		}
    	}}
    	for(int i=0;i<n;i++)
    	{
    	cout<<"Case #"<<i+1<<": ";
    	int j=0;
    	if(s[i][0]=='0')
    	{
    		j=1;
    	}
    	while(j<s[i].length())
    	{
    		cout<<s[i][j];
    		j++;
    	}
    	cout<<endl;
    }
	}
    
