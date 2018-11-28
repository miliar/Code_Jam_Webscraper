#include<bits/stdc++.h>
#define ll long long int
#define debug 0
#define mp make_pair
using namespace std;

int main() {
	// your code goes here
	 int n,m,t,i,j,q,type,l,r,len,siz,ans,res,sum,a,b,c,k1,t1=0;
    
    ll ans1,ans2;
    
    vector<ll>::iterator it;
    priority_queue<pair<int,char> > pqr;
	if(debug)
	cout<<"YEs";
	map<char,int> freq;
	pair<int,char> k;
 sum=0;
	cin>>t;
	 pair<int,int> top;
	 deque< pair<int,int> > dq;
	while(t--)
    {
        t1++;
    	cout<<"Case #"<<t1<<": ";
    	if(debug)
	cout<<"YEs";
	if(debug)
	cout<<"YEs";
    	freq.clear();
    	if(debug)
	cout<<"YEs";
	if(debug)
	cout<<"YEs";
    	cin>>n;
    	sum=0;
    	for(i=0;i<6;i++)
    	{
    		cin>>k1;
    		sum+=k1;
    		if(!k1)
    		continue;
    		if(debug)
	cout<<"YEs";
	if(debug)
	cout<<"YEs";
    		if(i==0)
    		{
    			freq['R']=k1;
    			if(debug)
	cout<<"YEs";if(debug)
	cout<<"YEs";
			}
			else if(i==1)
			{
				freq['O']=k1;
			}
			else if(i==2)
			{
				freq['Y']=k1;
			}
			else if(i==3)
			{
				freq['G']=k1;
			}
			else if(i==4)
			{
				freq['B']=k1;
			}
			else if(i==5)
			{
				freq['V']=k1;
				
			}
		}
    	
    	for(char i='A';i<='Z';i++)
	    {
	        if(freq[i])
	        {
	            pqr.push(mp(freq[i],i));
	        }
	        if(debug)
	cout<<"YEs";
	    }
	    
	    pair<int,char> p={-1,'A'};
	    
	    string ptr="";
	    if(debug)
	cout<<"YEs";
	    while(!pqr.empty())
	    {
	        k=pqr.top();
	        sum+=k1;
	        ptr+=k.second;
	        sum+=k1;sum+=k1;sum+=k1;sum+=k1;
	        pqr.pop();
	        sum+=k1;sum+=k1;sum+=k1;sum+=k1;
	        if(p.first>0)
	        pqr.push(p);
	        sum+=k1;sum+=k1;sum+=k1;sum+=k1;
	        k.first--;
	        p=k;
	       sum+=k1;sum+=k1;sum+=k1;sum+=k1;
	        if(debug)
	cout<<"YEs";
	    }
	    
	    //cout<<ptr<<"\n";
	    
	     if(ptr.length()==n)
	     {
	         len=ptr.length();
	        sum+=k1;sum+=k1;sum+=k1;sum+=k1;
	    
	       if(ptr[0]==ptr[len-1])
	       {
	          sum+=k1;sum+=k1;sum+=k1;sum+=k1;
	           if(debug)
	cout<<"YEs";
	if(debug)
	cout<<"YEs";
	           if(len>=3 && ptr[len-1]!=ptr[len-3])
	           {
	               swap(ptr[len-1],ptr[len-2]);
	               cout<<ptr<<"\n";
	           }
	           else if(len>=4 && ptr[len-1]!=ptr[len-4] && ptr[len-1]!=ptr[len-3])
	           {
	               swap(ptr[len-1],ptr[len-3]);
	               cout<<ptr<<"\n";
	           }
	           else if(len>=5 && ptr[len-1]!=ptr[len-5] && ptr[len-1]!=ptr[len-4])
	           {
	               swap(ptr[len-1],ptr[len-4]);
	               cout<<ptr<<"\n";
	           }
	           else
	           cout<<"IMPOSSIBLE\n";
	           if(debug)
	cout<<"YEs";
	if(debug)
	cout<<"YEs";
	sum+=k1;sum+=k1;sum+=k1;sum+=k1;
	sum+=k1;sum+=k1;sum+=k1;sum+=k1;
	        }
	       else
	       cout<<ptr<<"\n";
	     }
	    else
	    cout<<"IMPOSSIBLE\n";
	    if(debug)
	cout<<"YEs";
	   sum+=k1;sum+=k1;sum+=k1;sum+=k1;
    	
	}
	return 0;
}

