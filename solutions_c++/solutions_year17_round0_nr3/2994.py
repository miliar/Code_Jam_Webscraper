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
#define lli long long int
using namespace std;


int main()
{
	lli t,i,n,m1,counter=1;
	scanf("%lld ",&t);
	while(t--)
	{
	    scanf("%lld %lld",&n,&m1);
	    printf("Case #%d: ",counter);
	    counter++;
	    priority_queue<lli> q;
	    map<lli,lli> m;
	    lli count=1,x,y;
	    
	    if(n&1)
	    {
	        x=n/2;
	        y=x;
	    }
	    else
	    {
	        x=(n/2)-1;
	        y=n/2;
	    }
	    if(m[x]==0)
        q.push(x);
        m[x]+=1;
        if(m[y]==0)
        q.push(y);
        m[y]+=1;
       // cout << x << " " << y  << endl;
	    while(count<m1)
	    {
	        n=q.top();
	        q.pop();
	        count+=m[n];
	       // cout << n << " ";
	        if(n&1)
    	    {
    	        x=n/2;
    	        y=x;
    	    }
    	    else
    	    {
    	        x=(n/2)-1;
    	        y=n/2;
    	    }
    	    if(m[x]==0)
            q.push(x);
            m[x]+=m[n];
            if(m[y]==0)
            q.push(y);
            m[y]+=m[n];
    	    //m[x]+=m[n];m[y]+=m[n];
    	    //cout << x << " " << y  << endl;
    	    //cout << count << endl;
	    }
	    cout << y << " " << x << endl; 
	}
	return 0;
}