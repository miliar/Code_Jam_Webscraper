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
	    long long int N, K;
	    cin>>N>>K;
	    priority_queue<long long int> Q;
	    Q.push(N);
	    while(K-->1)
	    {
	        long long int temp = Q.top();
	        Q.pop();
	        if(temp%2==1)
	        {
	            Q.push(temp/2); Q.push(temp/2); 
	        }
	        else
	        {
	            Q.push(temp/2); Q.push(temp/2-1);
	        }
	    }
	    long long int temp = Q.top();
	    if(temp%2==1)
	        cout<<"Case #"<<k<<": "<<temp/2<<" "<<temp/2<<endl;
	    else
	        cout<<"Case #"<<k<<": "<<temp/2<<" "<<temp/2-1<<endl;
	}
    return 0;
}
