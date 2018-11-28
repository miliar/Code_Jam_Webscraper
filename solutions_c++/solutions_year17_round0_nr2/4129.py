#include <bits/stdc++.h>
using namespace std;
int main () {
#ifndef ONLINE_JUDGE
	freopen("in", "r", stdin);
	freopen("out", "w", stdout);
#endif
	int t, co = 0; cin>>t; while(t--) {
		string num; cin>>num;
		int n = num.size(); 
		for(int i=n-1; i>0; i--) {
			if(num[i] < num[i-1]) {
				num[i-1]--;
				for(int j=i; j<n; j++) 
					num[j] = '9';
			}
		} long long number = 0;
		for(int i=0; i<n; i++) 
			number = number*10 + num[i] - '0';
		cout<<"Case #"<<++co<<": " <<number<<endl;
	}
}
