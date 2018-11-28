#include <bits/stdc++.h>
using namespace std;
bool digs(int s) {
	int fl = s%10;
	s = s/10;
	while(s) {
		int a = s%10;
		if(a>fl) return 0;
		s = s/10;
		fl = a;
	}
	return 1;
} 
int main()
{
	int a[1002];
	a[1] = 1;
	for(int i=2;i<1002;i++) {
		if(digs(i)==1) {
			a[i] = i;
		}
		else a[i] = a[i-1];
	}
	int t,h1;
	cin>>t;
	h1 = t;
	while(t--) {
		int n;
		cin>>n;
		cout<<"Case #"<<h1-t<<":"<<" "<<a[n]<<endl;
	}
	return 0;
}
