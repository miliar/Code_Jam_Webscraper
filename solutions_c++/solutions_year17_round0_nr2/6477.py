#include <bits/stdc++.h>
using namespace std;

int main() {
	int T;
	cin>>T;
	for(int count = 1;count <=T;count++)
	{
	    long long N;
	    cin>>N;
	    string N_str = to_string(N);
	    int n = N_str.length();
	    
	    for(int i = n-2;i>=0;i--)
	    {
	        if(N_str[i] <= N_str[i+1])
	        continue;
	        
	        N_str[i] = N_str[i]  - 1  ;
	        for(int j = i+1;j<n;j++)
	        N_str[j] = '9';
	        
	    }
	    
	    cout<<"Case #"<<count<<": ";
	    N = stoll(N_str);
	    cout<<N<<endl;
	}
	return 0;
}
