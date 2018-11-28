#include <iostream>
#include <cstring>
#include <cstdio>
using namespace std;
string str;
int n, k;
bool ok(){
	for(int i = 0; i < str.length(); i++) if(str[i] == '-') return false;
	return true;
}

int main(){
	//freopen("a.txt", "r", stdin);
	//freopen("output.txt", "w", stdout);
	cin>>n;
	for(int Case = 1; Case <= n; Case++){
		cin>>str; cin>>k;
		int ans = 0;
		for(int i = 0; i < str.length(); i++){
			if(i+k > str.length()) break;
			if(str[i] == '+') continue;
			ans++;
			for(int j = i; j < i+k; j++){
				str[j] = (str[j] == '+') ? '-' : '+';
			}
		}
		if(ok()) cout<<"Case #"<<Case<<": "<<ans<<endl;
		else cout<<"Case #"<<Case<<": IMPOSSIBLE"<<endl;
	}
}
