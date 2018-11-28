#include <iostream>
#include <cstdio>

using namespace std;

int main() {
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int t, i, cases = 1, j;
	long long sum;
	string s;
	cin>>t;
	while(t--) {
		cin>>s;
		for(i = 0; i < s.length() - 1; i++) {
			if(s[i] > s[i+1]) {
				for(j = i + 1; j < s.length(); j++) 
					s[j] = '9';
				s[i]--;
				i--;
				while(i >= 0 && s[i] > s[i+1]) {
					s[i+1] = '9';
					s[i]--;
					i--;
				}
				break;
			}
		}
		sum = 0;
		for(i = 0; i < s.length(); i++) {
			sum = sum * 10 + s[i] - '0';
		}
		cout<<"Case #"<<cases<<": "<<sum<<"\n";
		cases++;
	}
	return 0;
}