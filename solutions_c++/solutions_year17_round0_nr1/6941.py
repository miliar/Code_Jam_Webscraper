#include <bits/stdc++.h>
using namespace std;


int Min_flip(string &S,int K)
{
    int flipvalue = 0;
    int N = S.length();
    queue<int> q;
    
    for(int i=0;i<N;i++)
    {
        if(!q.empty() && q.front() <= i-K)
        q.pop();
        
        if((q.size() % 2 == 0 && S[i] == '-' ) || (q.size() %2 == 1 && S[i] == '+') )
        {
            if(i > N - K)
            return -1;
            
            flipvalue++ ;
            q.push(i);
        }
    }
    return flipvalue;
}
int main() {
	int t;
	cin>>t;
	for(int C = 1;C <=t;C++)
	{
	    int K;
	    string S;
	    cin>>S>>K;
	    
	    int flipvalue = Min_flip(S,K);
	    cout<<"Case #"<<C<<": ";
	    if(flipvalue != -1)
	    {
	        cout<<flipvalue<<endl;
	    }
	    else
	    {
	        cout<<"IMPOSSIBLE\n";
	    }
	  
	}
	return 0;
}
