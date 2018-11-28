#include <bits/stdc++.h>
using namespace std;
int T;
int N;
int a[30];
string s;
int main(){
	freopen("large.in", "r", stdin);
	freopen("large.out", "w", stdout);
	cin >> T;
	for(int i = 1; i <= T; i++){
		cin >> s;
		cout << "Case #" << i << ": ";
		int len = s.size();
		//if(len == 1){
		//	cout << s[0] << endl;
		//	continue;
		//}
		for(int j = 0; j < s.size(); j++){
			a[j + 1] = s[j] - '0';
		}
		int k = 1000000002;
		for(int j = 1; j <= len - 1; j++){
			if(a[j + 1] < a[j]){
				a[j]--;
				k = j + 1;
				break;
			}
		}
		for(int j = k; j <= len; j++){
			a[j] = 9;
		}
		for(int j = len; j >= 2; j--){
			if(a[j] < a[j - 1]){
				a[j - 1]--;
				a[j] = 9;
			}
		}
		k = 1;
		while(a[k] == 0) k++;
		for(int j = k; j <= len; j++){
			cout << a[j];
		}
		cout << endl;
	}
return 0;
}

