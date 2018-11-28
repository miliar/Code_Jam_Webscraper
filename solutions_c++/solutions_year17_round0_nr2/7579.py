#include <bits/stdc++.h>
using namespace std;
int main() {
	int t,flag,i,k;
	cin>>t;
	string s;
	char c;
	k = 0;
	while(k < t) {
		cin>>s;
		for(i = s.size()-1; i > 0; i--) {
			if(s[i-1] > s[i]) {
                c = '0' + (s[i-1] - '1');
               s[i-1] = c;
				for(int j = i; j < s.size(); j++)
					s[j] = '9';
			}
		}
		for(i = 0; i < s.size(); i++)
			if(s[i] !='0')
				break;
		cout<<"Case #"<<k+1<<": ";
		for(; i < s.size(); i++)
			cout<<s[i];
		cout<<"\n";
		k++;
	}
	return 0;
}