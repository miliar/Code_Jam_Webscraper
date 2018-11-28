#include <bits/stdc++.h>
using namespace std;

int main() {
	// your code goes here
	//ios::sync_with_stdio(0);
	int t;
	long long n;
	freopen("input.in","r",stdin);
	cin>>t;//to be replaced by file input
	for(int u=1;u<=t;u++)
	{

	    cin>>n;//to be replaced by file input
	    long long temp=n;
	    int x,a[19],i=0,j;
	    while(temp!=0)
	    {
	        a[i]=temp%10;
	        temp=temp/10;
	        i++;
	    }
	    for(j=0;j<i-1;j++)
	    {
	        if(a[j]>=a[j+1])
	        continue;
	        else
	        {
	            for(int k=0;k<=j;k++)
	            {
	                a[k]=9;
	            }
	            a[j+1]-=1;
	        }
	    }
	    temp=0;
	    for(j=i-1;j>=0;j--)
	    {
	        temp=temp*10+a[j];
	    }
	    freopen("output.txt","a",stdout);
	    cout<<"Case #"<<u<<": "<<temp<<"\n";
	}
	return 0;
}
