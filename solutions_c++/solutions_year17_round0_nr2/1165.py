#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>
#include <stack>
#include <map>

using namespace std;
typedef long long int LL;
char s[40];
int main() {
	int t;
	cin >> t;
	for(int fm=1;fm<=t;fm++){
		cin >> s;
		int n;
		for(n=0;s[n]!=0;n++);
		for(int i=n-1;i>=1;i--){
			if(s[i] < s[i-1]){
				s[i-1]--;
				for(int j=i;j<n;j++)s[j]='9';
			}
		}
		cout << "Case #" << fm << ": ";
		int k=0;
		for(;k<n;k++){
			if(s[k] != '0')break;
		}
		for(;k<n;k++)cout << s[k];
		cout << "\n";
	}
	return 0;
}