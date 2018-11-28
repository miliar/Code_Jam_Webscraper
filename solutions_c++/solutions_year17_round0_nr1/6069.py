#include <bits/stdc++.h>

using namespace std;

int main() {
	int t;
	cin>>t;
	for(int q=1; q<=t; q++) {
		string s;
		int k;
		cin>>s>>k;
		int n = s.size();
		int a[n], count=0;
		for(int i=0; i<n; i++)
			a[i] = (s[i] == '+')?1:0;
		for(int i=0; i<n-k+1; i++) {
			if(!a[i]) {
				count++;
				for(int j=i; j<i+k; j++)
					a[j] = (a[j]+1)%2;
			}
		}
		bool flag = false;
		for(int i=n-k+1; i<n; i++) {
			if(!a[i]) {
				flag = true;
				break;
			}
		}
		if(flag) {
			cout<<"Case #"<<q<<": IMPOSSIBLE\n";
		}
		else {
			printf("Case #%d: %d\n", q, count);
		}
	}
	return 0;
}