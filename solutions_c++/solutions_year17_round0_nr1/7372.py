#include <cstdio>
#include <iostream>
#include <vector>

using namespace std;

int main() {
	ios_base::sync_with_stdio(false);
	freopen("A-large.in","r",stdin);
	freopen("output_large.out","w",stdout);
	int t;
	cin>>t;
	int tt;
	vector<int> trace(1010,0);
	for(tt=1;tt<=t;tt++) {
		string s;
		int k;
		cin>>s;
		int flipCount=0;
		cin>>k;
		fill(trace.begin(),trace.end(),0);
		int ans=0;
		for(int i=0;i<s.length();i++) {
			flipCount += trace[i];
			if(s[i] == '+' && flipCount%2==0) continue;
			if(s[i] == '-' && flipCount%2!=0) continue;
			if(s.length()-i<k) {
				ans = -1;
				break;
			}
			flipCount++;
			trace[i+k] += -1;
			ans++;
			//cout<<"test "<<s<<endl;
		}
		if(ans==-1) {
			cout<<"Case #"<<tt<<": IMPOSSIBLE"<<endl;
		} else {
			cout<<"Case #"<<tt<<": "<<ans<<endl;
		}
	}
}