#include <bits/stdc++.h>
using namespace std;

int main() {
	// your code goes here
	long o,t,i,n,k,x;
	multiset<long> s;
	multiset<long>::iterator it;
	
    cin>>t;
	for(o=1;o<=t;o++)
	{
	    cin>>n>>k;
	    s.insert(n);
	    for(i=0;i<k-1;i++)
	    {
	        x=(*(s.rbegin()));
	        it=(s.end());
	        //cout<<x;
	        s.erase(--it);
	        if(x%2 == 1)
	        {
	            if(x/2 > 0)
	            {
	            s.insert(x/2);
	            s.insert(x/2);
	            }
	        }
	        else
	        {
	            if(x/2 >0)
	            s.insert(x/2);
	            if(x/2 > 1)
	            s.insert((x/2)-1);
	        }

	        
	    }
	    x=(*(s.rbegin()));
	    
	    cout<<"Case #"<<o<<": ";
	    if(x%2 == 1)
	    {
	        cout<<x/2<<" "<<x/2<<endl;
	        
	    }
	    else
	    {
	        cout<<x/2<<" "<<((x/2)-1)<<endl;
	        
	    }
	    s.clear();
	    
	}
	return 0;
}
