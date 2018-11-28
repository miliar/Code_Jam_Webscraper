#include <cstdlib>
#include <cstdio>
#include <iostream>
#include <string>
#include <cstring>
#include <vector>
#include <algorithm>
#include <queue>
#include <climits>
#include <map>
#include <set>
#define llu long long 
using namespace std;


vector<llu> res(llu n,llu k)
{		
		priority_queue<llu> pq;
	    map<llu,llu> mp;
	    llu count=1,l,r;
	    
	    if((n%2))
	    {
	        l=n/2;
	        r=l;
	    }
	    else
	    {
	        l=(n/2)-1;
	        r=n/2;
	    }
	    if(mp[l]==0)
        pq.push(l);
        mp[l]+=1;
        if(mp[r]==0)
        pq.push(r);
        mp[r]+=1;
	    while(count<k)
	    {
	        n=pq.top();
	        pq.pop();
	        count+=mp[n];
	        if(n%2)
    	    {
    	        l=n/2;
    	        r=l;
    	    }
    	    else
    	    {
    	        l=(n/2)-1;
    	        r=n/2;
    	    }
    	    if(mp[l]==0)
            pq.push(l);
            mp[l]+=mp[n];
            if(mp[r]==0)
            pq.push(r);
            mp[r]+=mp[n];
    	    
	    }
	    vector<llu>ret;
	    ret.push_back(l);
	    ret.push_back(r);
	    return ret;
}
	    
	    
	    
int main()
{
	llu t,cn=1;
	cin>>t;
	while(t--)
	{
		llu n,k;
	   cin>>n>>k;
	    
	    vector<llu>result=res(n,k);
	    cout<<"Case #"<<cn<<": ";
	    cn++;
	    cout << result[1] << " " << result[0] << endl; 
	}
	return 0;
}

