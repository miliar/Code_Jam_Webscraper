#include <bits/stdc++.h>
using namespace std;

int main() {
	int T;
	cin>>T;
	for(int C = 1;C <=T;C++)
	{
	    long long N;
	    cin>>N;
	    string S = to_string(N);
	    int n = S.length();
	    
	    for(int i = n-2;i>=0;i--)
	    {
	        if(S[i] <= S[i+1])
	        continue;
	        
	        S[i] = S[i]  - 1  ;
	        for(int j = i+1;j<n;j++)
	        S[j] = '9';
	        
	    }
	    
	    cout<<"Case #"<<C<<": ";
	    N = stoll(S);
	    cout<<N<<endl;
	}
	return 0;
}
