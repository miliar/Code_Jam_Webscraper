#include <iostream>
#include<stdio.h>
#include<algorithm>
#include<string>
#include<vector>
using namespace std;

int main() {
	// your code goes here
	int t;
	scanf("%d",&t);
	for(int i=0;i<t;i++)
	{
	    long long n,k;
	    scanf("%lld",&n);
	    vector<int> v;
	    long long next=n%10;
	    k=n/10;
	    while(k)
	    {
	        v.push_back(next);
	        next=k%10;
	        k=k/10;
	        
	    }
	    v.push_back(next);
	    for(int j=0;j<v.size()-1;j++)
	    {
	        if(v[j]<v[j+1])
	        {
	            for(int l=j;l>=0;l--)
	            v[l]=9;
	            v[j+1]-=1;
	        }
	    }
	    k=0;
	    for(int j=v.size()-1;j>=0;j--)
	    {
	        k=k*10+v[j];
	    }
	    /*for(long long j=0;j<=n;j++)
	    {
	        long long k=n;
	    long long next=n%10;
	    k=n/10;
	    while(k)
	    {
	        long long prev=k%10;
	        if(prev>next)
	        break;
	        next=prev;
	        k=k/10;
	        
	    }
	    if(k==0)
	    break;
	     n--;   
	    }*/
	    printf("Case #%d: %lld\n",i+1,k);
	}
	return 0;
}
