#include <iostream>
#include <cstdio>
#include <string>
using namespace std;

int main(){
	//freopen("inputla.in", "r", stdin);
	//freopen("outputla.out", "w", stdout);
	int T, N, i, j, k, it, cnt, flag;
	cin >> T;
	string str;
	for(it = 1; it <= T; it++){
		cin >> str;
		cnt = flag = 0;
		cin >> N;
		for(i = 0; i <= str.size() - N; i++){
			if(str[i] == '+'){
				continue;
			}
			else{
				if(i+N > str.size()) break;
				for(j = i; j < i+N; j++){
					if(str[j] == '+') str[j] = '-';
					else str[j] = '+';
				}
				cnt++;
			}
		}
		for(i = 0; i < str.size(); i++){
			if(str[i] == '-'){
				flag = 1;
				break;
			}
		}
		if(flag == 0) cout << "Case #" << it << ": "<<  cnt << "\n";
		else cout << "Case #" << it << ": IMPOSSIBLE \n";
	}
	return 0;
}
