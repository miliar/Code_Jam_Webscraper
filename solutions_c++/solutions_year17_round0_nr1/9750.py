#include <bits/stdc++.h>
using namespace std;
int main () {
	#ifndef ONLINE_JUDGE
		freopen("in", "r", stdin);
	#endif
		freopen("out", "w", stdout);
    int t, co = 0; 
    cin >> t; while(t--) {
		string str; int k; 
		cin>>str>>k; int cnt = 0;
		for(int i=0; i<str.size()-k+1; i++) {
			if(str[i] == '-') {
				for(int j=i; j<i+k; j++) {
					if(str[j] == '-') 
						str[j] = '+';
					else str[j] = '-';
				} cnt++; 
			} 
		} int f=1;
		cout<<"Case #"<<++co<<": ";
		for(int i=str.size()-1; i>0; i--) {
			if(str[i] == '-') {
				f = 0, cout<<"IMPOSSIBLE\n"; 
				break;
			}
		} if(f) cout<<cnt<<endl;
    }
}
