#include <iostream>
#include <cstring>
#include<bits/stdc++.h>
#define ll long long int
# define mp make_pair
 const ll M = 1e9+7;
#define pb push_back 
using namespace std;
int main()
{
    freopen ("B-large.in", "r", stdin);
    freopen ("outb.txt", "w", stdout);
    int t;
    cin>>t;
    for(int e=1;e<=t;e++){
	string a;
	int n,i,x;   
    cin>>a;
    n=a.size();
    for(i=0;i<n-1;i++)
	if(a[i]>a[i+1])
	   break;
	   
	   
	 //  cout<<i;
	     cout<<"Case #"<<e<<": ";
	     if(n==1||i==n-1)
	     {
		 cout<<a<<endl;
	     }
	   else if(a[i]>'1')
	   {
	       x=a[i];
		  for(i=0;i<n;i++)   {
		   if(a[i]==x)   {
		     a[i]=a[i]-1;
		     cout<<a[i];
		     for(i=i+1;i<n;i++)
		     cout<<"9";
		     }
		     else
		     cout<<a[i];
		  }
		  cout<<endl;
		     
	   }
	   else
	   {
	       i=0; 
	       while(a[i]=='0')
	       i++;
		for(i=i+1;i<n;i++)
		cout<<"9";
		cout<<endl;
	   }
    
   
    }
    return 0;
}
