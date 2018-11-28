#include <bits/stdc++.h>
using namespace std;


int Min_flip(string &S,int K)
{
    int flip = 0;
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
            
            flip++ ;
            q.push(i);
        }
    }
    return flip;
}
int main() {
	int T;
	cin>>T;
	for(int C = 1;C <=T;C++)
	{
	    int K;
	    string S;
	    cin>>S>>K;
	    
	    int flip = Min_flip(S,K);
	    cout<<"Case #"<<C<<": ";
	    if(flip != -1)
	    {
	        cout<<flip<<endl;
	    }
	    else
	    {
	        cout<<"IMPOSSIBLE\n";
	    }
	  
	}
	return 0;
}
