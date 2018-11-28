#include <bits/stdc++.h>
using namespace std;


int fun(string &str,int k)
{
    int ans = 0;
    int n = str.length();
    queue<int> Q;
    
    for(int i=0;i<n;i++)
    {
        if(!Q.empty() && Q.front() <= i-k)
        Q.pop();
        
        if((Q.size() % 2 == 0 && str[i] == '-' ) || (Q.size() %2 == 1 && str[i] == '+') )
        {
            if(i > n- k)
            return -1;
            
            ans++ ;
            Q.push(i);
        }
    }
    return ans;
}
int main() {
	int t;
	cin>>t;
	for(int count = 1;count <=t;count++)
	{
	    int k;
	    string str;
	    cin>>str>>k;
	    
	    int ans = fun(str,k);
	    cout<<"Case #"<<count<<": ";
	    if(ans != -1)
	    {
	        cout<<ans<<endl;
	    }
	    else
	    {
	        cout<<"IMPOSSIBLE\n";
	    }
	  
	}
	return 0;
}
