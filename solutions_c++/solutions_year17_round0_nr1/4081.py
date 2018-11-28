#include<bits/stdc++.h>
#include<unordered_set>
#include<unordered_map>
using namespace std;

int t;

char buf[1002];

string s;

bool im[1002];

int coun;
void outt(){
coun++;
	cout << "Case #" << coun << ": ";
}
int main(){
	cin >> t;
	while (t--){
		scanf("%s", buf);
		s = buf;
		int k;
		scanf("%d", &k);
		memset(im, false, sizeof(im));
		int ans = 0;
		for (int i = 0; i < s.size(); i++){
			bool cur = false;
			if (i)im[i] ^= im[i - 1];
			if (s[i] == '-'){
				cur = false;
			}
			else{
				cur = true;
			}
			cur ^= im[i];
			if (cur == false){
				if (i + k <= s.size()){
					im[i + k] ^= 1;
					im[i] ^= 1;
					ans++;
				}
				else{
					ans = -1;
					break;
				}
			}
		}
		outt();
		if (ans == -1){
			puts("IMPOSSIBLE");
		}
		else{
			cout << ans << endl;
		}
	}
	return 0;
}