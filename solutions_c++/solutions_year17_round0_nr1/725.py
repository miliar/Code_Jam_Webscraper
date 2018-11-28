#include <iostream>
#include <cstdlib>
#include <cstring>
#include <cstdio>
using namespace std;
int pancake[1111];
int work() {
	char c;
	int n=0;
	int ans = 0;
	int k;
	getchar();
	while(true) {
		cin.get(c);
		if(c == ' ') break;
		pancake[n++] = (c=='+') ? 1 : 0;
	}
	cin>>k;
	//getchar();
	for(int i = 0; i < n; i++) {
		if(pancake[i] == 0) {
			if(i+k > n) return -1;
			ans++;
			for(int j = 0; j < k ; j++) 
				pancake[i+j] = !pancake[i+j];
		}
		// for(int w = 0; w < n; w++)
		// 	cout<<pancake[w]<<" ";
		// cout<<endl;
	}
	return ans;
}
int main() {
	int t;
	int i =1;
	cin>>t;
	while(t) {
		int ans = work();
		if (ans == -1)
			cout<<"Case #"<<i<<": IMPOSSIBLE\n";
		else 
			cout<<"Case #"<<i<<": "<<ans<<endl;
		t--;
		i++;
	}
}