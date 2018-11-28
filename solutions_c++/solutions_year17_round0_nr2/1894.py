#include <iostream>
#include <string>
#include <stack>
#include <algorithm>
using namespace std;
char ans[1000];

int main(){
	freopen("input.txt", "r", stdin);
	//freopen("C:\\Users\\psw\\Desktop\\output.txt", "w", stdout);

	int tc;
	cin >> tc;
	for (int tc_ = 1; tc_ <= tc; tc_++){
		string str;
		ans[str.size()] = '\0';
		cin >> str;
		int pivot = str.size();
		for (int i = str.size()-1; i > 0; i--){
			if (str[i-1] > str[i]) {
				for (int j = i; j < pivot; j++){
					ans[j] = '9';
				}
				pivot = i;
				str[i-1]--;
			} else ans[i] = str[i];
		}
		ans[0] = str[0];
		cout << "Case #" << tc_ << ": " ;
		int start = 0;
		while(ans[start] == '0') start++;
		for (int i = start; i < str.size(); i++){
			cout << ans[i];
		}
		cout << '\n';
	}
	return 0;
}