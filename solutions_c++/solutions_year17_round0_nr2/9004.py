#include<bits/stdc++.h>
using namespace std;

string s;

bool isNoDecreasing(string s){
	for(int i = 1; i < s.length(); i++)
		if(s[i - 1] > s[i])
			return false;
	return true;
}

int main(){

	ofstream cou("AS.o");
	int cases = 1, t;
	cin >> t;

	while(t--){
		cin >> s;
		while(!isNoDecreasing(s)){
			bool flag = true;
			for(int i = 1; i < s.length(); i++){
				while(s[i] < s[i - 1]){
					if(s[i] - 48 - 1 == -1){
						s[i] = 9 + 48;
						if(flag){
							s[i - 1]--;
							flag = !flag;
						}
					}else{
						s[i]--;
					}
				}
			}
		}
		cout << "Case #" << cases++ << ": ";
		int i = 0;
		while(s[i] == 48)
			i++;
		for(; i < s.length(); i++)
			cout << s[i];
		cout << endl;

	}

	return 0;
}