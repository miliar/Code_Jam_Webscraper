#include<bits/stdc++.h>
using namespace std;
int main(){
	ios_base::sync_with_stdio(false);
	cin.tie(0);
    int T;
    cin>>T;
    for (int t=1;t<=T;t++)
    {
    	string s;
    	int k;
    	cin>>s>>k;
    	int n = s.size();
    	int ans = 0;
    	for(int i=0;i+k-1<n; i++)
    	{
    		while(i+k-1<n && s[i] == '+')
    			i++;
    		if(i+k-1<n)	// s[i] == '-'
    		{
    			for(int j=0;j<k;j++)
    				s[i+j] = (s[i+j]=='+') ? '-' : '+' ;
    			ans++;
			}
		}
		if(s.substr(n-k+1,k-1) == string(k-1,'+'))
			cout<<"Case #"<<t<<": "<<ans<<'\n';
		else
			cout<<"Case #"<<t<<": "<<"IMPOSSIBLE"<<'\n';
	}
    return 0;
}
