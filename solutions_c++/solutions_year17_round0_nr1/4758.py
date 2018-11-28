    #include<bits/stdc++.h>
    using namespace std;
    
    int main()
    {
    	ios::sync_with_stdio(0);
    	freopen("input.in", "r", stdin); 
    	freopen("output.out", "w", stdout);
    	int T;
    	cin>>T;
    	for(int k=1; k<=T; k++)
    	{
    	    string S;
    	    cin>>S;
    	    int count=0, K;
    	    cin>>K;
    	    int N = S.length();
    	    for(int i=0; i<=N-K; i++)
    	    {
    	        if(S[i]=='-')
    	        {
    	            for(int j=i; j<i+K; j++)
    	            {
    	                if(S[j]=='+')
    	                {
    	                    S[j]='-';
    	                }
    	                else
    	                {
    	                    S[j]='+';
    	                }
    	            }
    	            count++;
    	        }
    	    }
    	    bool check = true;
    	    for(int i=0; i<N; i++)
    	    {
    	        if(S[i]=='-')
    	        {
    	            check = false;
    	            break;
    	        }
    	    }
    	    if(!check)
    	        cout<<"Case #"<<k<<": "<<"IMPOSSIBLE\n";
    	    else
    	        cout<<"Case #"<<k<<": "<<count<<"\n";
    	}
        return 0;
    }
