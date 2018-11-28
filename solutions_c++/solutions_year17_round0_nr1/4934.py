#include <iostream>
#include <queue>

using namespace std;

void solve() 
{
	int k, n, x = 0, y, ans = 0;
	string s;
	cin>>s>>k;
	n = s.size();
	queue<int> q;
	for(int i=0; i<n-k+1; i++) {
		y = (s[i]=='+' ? 0 : 1);
		if(q.size() && i-q.front()>=k) q.pop(), x ^= 1;
		if(x!=y) ans++, x ^= 1, q.push(i);
	}
	for(int i=n-k+1; i<n; i++) {
		y = (s[i]=='+' ? 0 : 1);
		if(q.size() && i-q.front()>=k) q.pop(), x ^= 1;
		if(x!=y) {
			cout<<"IMPOSSIBLE\n";
			return;
		}
	}
	cout<<ans<<endl;
}

int main()
{
	int T;
	cin>>T;
	for(int i=1; i<=T; i++) 
		cout<<"Case #"<<i<<": ",
		solve();
	return 0;
}