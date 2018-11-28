#include <iostream>
#include <cstring>
using namespace std;

int main() {
	long long t;
	cin>>t;
	char s[1002],s1[1002];
	int k,l;
	for (long long ti = 1; ti <= t; ++ti) {
		cout<<"Case #"<<ti<<": ";
//		cout<<"Case #"<<ti<<": ";
		cin>>s1>>k;
		l = strlen(s1);
		for (int i = 0; i < l; ++i) {
			s[i] = s1[i] == '+' ? 1 : 0;
		}
		
		int c = 0;
		int ll = l-k;
		for (int i = 0; i <= ll; ++i) {
			if (s[i]) continue;
			
			for (int j = 0; j < k; ++j) {
				s[i+j] = !s[i+j];
			}
			++c;
		}
		bool yes = true;
		for (int i = 0; i < l; ++i) {
			if (!s[i]) {
				yes = false;
				break;
			}
		}
		
		if (yes) {
			cout<<c;//(c1<c?c1:c);
		}
		else {
			cout<<"IMPOSSIBLE";
		}
//		cout<<" "<<s1<<" "<<k;
		cout<<"\n";
	}
}
