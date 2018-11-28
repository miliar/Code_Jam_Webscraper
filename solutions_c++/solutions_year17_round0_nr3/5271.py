#include <cstdlib>
#include <cstdio>
#include <iostream>
#include <string>
#include <cstring>
#include <algorithm>
#include <vector>
#include <climits>
#include <queue>
#include <map>
#include <set>

using namespace std;
struct abc{
int a,b;
};
abc result(long long int n,long long int m);


int main()
{
	long long int t,i,n,m1,count=1;
	scanf("%lld ",&t);
	while(t--)
	{
	    cin>>n>>m1;
	    cout<<"Case #"<<count<<": ";
	    count++;
	    long long int arr[2];
	    abc sd=result(n,m1);
	   cout << sd.b << " " << sd.a << endl;
	
	 
	}	return 0;
}

abc result(long long int n,long long int m)
{


	    priority_queue<long long int> qu;
	    map<long long int,long long int> mp;
	    long long int cnt=1,left,right;
	    
	    if(n&1)
	    {
	        left=n/2;
	        right=left;
	    }
	    else
	    {
	        left=(n/2)-1;
	        right=n/2;
	    }
	    if(mp[left]==0)
        qu.push(left);
        mp[left]+=1;
        if(mp[right]==0)
        qu.push(right);
        mp[right]+=1;
       
	    while(cnt<m)
	    {
	        n=qu.top();
	        qu.pop();
	        cnt+=mp[n];
	      
	        if(n&1)
    	    {
    	        left=n/2;
    	        right=left;
    	    }
    	    else
    	    {
    	        left=(n/2)-1;
    	        right=n/2;
    	    }
    	    if(mp[left]==0)
            qu.push(left);
            mp[left]+=mp[n];
            if(mp[right]==0)
            qu.push(right);
            mp[right]+=mp[n];
	    }
	abc re;
	re.a=left;
	re.b=right;
	return re;
}
