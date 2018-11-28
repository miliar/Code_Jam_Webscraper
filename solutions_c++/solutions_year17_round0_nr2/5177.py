#include <bits/stdc++.h>
using namespace std;
bool check(long long a){
	string s = to_string(a);
	int n = s.size();
	for(int i=1;i<n;i++){
		if(s[i-1] > s[i])return false;
	}
	return true;
}
void solve(){
	long long a;
	cin >> a;
	string s = to_string(a);
	int n = s.size();
	int start = 0;
	for(int i=1;i<n;i++){
		if(s[i-1] < s[i]){
			start = i;
		}else if(s[i-1] > s[i]){
			s[start] = s[start] - 1;
			for(int j=start+1;j<n;j++){
				s[j] = '9';
			}
		}
	}
	for(int i=0;i<n;i++){
		if(s[i]!='0'){
			cout << s.substr(i);
			break;
		}
	}
}
int main(void){
	int T;
	cin >> T;
	for(int i=0;i<T;i++){
		cout << "Case #" << i+1 << ": ";
		solve();
		cout << endl;
	}
	return 0;
}