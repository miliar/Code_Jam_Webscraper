#include <iostream>
#include <cstring>
using namespace std;
int main(){
	int tc;
	cin >> tc;
	for (int t=1;t<=tc;t++){
		string s, ans;
		cin >> s;

		int l= s.size();
		for (int j=0;j<l;j++){
			bool flag = false;
			for (int i=0;i<l-1;i++){
				if (s[i]> s[i+1]){
					if (!flag) {
						s[i]--;
					}
					flag = true;
					s[i+1] = '9';
				}
			}
		}
		ans = s;
		if (ans[0]=='0'){
			ans = ans.substr(1);
		}
		cout << "Case #" << t << ": "<< ans << endl;
	}
	return 0;
}
