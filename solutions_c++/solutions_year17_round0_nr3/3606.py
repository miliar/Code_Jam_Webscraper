#include<bits/stdc++.h>
using namespace std;
int main(){
	ios_base::sync_with_stdio(false);
	cin.tie(0);
    int T;
    cin>>T;
    for (int t=1;t<=T;t++)
    {
    	long long n,k;
    	cin>>n>>k;
    	multiset<int> s;
    	auto it = s.insert(n);
    	for(int i=1;i<k;i++)
    	{
			int x = *s.rbegin();
			auto it = s.end();
			it--;
    		s.erase(it);
    		int a = (x-1)/2;
    		int b = x/2;
    		if(b)
    			s.insert(s.begin(),b);
    		if(a)
    			s.insert(s.begin(),a);
		}
		int x = *s.rbegin();
		int a = (x-1)/2;
		int b = x/2;
		cout<<"Case #"<<t<<": "<<b<<' '<<a<<'\n';
	}
    return 0;
}
