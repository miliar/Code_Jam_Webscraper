#include <iostream>
#include <cstring>
using namespace std;

int main() {
	long long t;
	cin>>t;
	char s[20];
	for (long long ti = 1; ti <= t; ++ti) {
		cout<<"Case #"<<ti<<": ";
		cin>>s;
		int l = strlen(s);
		for (int i = l-1; i >= 0; --i) {
			if (i > 0) {
//				cout<<s[i-1]<<" "<<s[i]<<endl;
				if (s[i] < s[i-1] || s[i] == '0') {
					s[i] = '0'+9;
					s[i-1] = ((s[i-1]-'0') +9)%10 + '0';
					
					if (i <l-1 && s[i] > s[i+1]) {
						for (int j = i+1; j < l; ++j) s[j] = '9';
					}
				}
			}
		}
		if (s[0] == '0') strcpy(s,s+1);
		cout<<s;
		cout<<"\n";
	}
}
