#include <bits/stdc++.h>
typedef long long ll;

using namespace std;
string rep[11][20];
void main2(){
	for(int i=0;i<11;i++){
		for(int j=1;j<20;j++){
			rep[i][j] = rep[i][j-1];
			rep[i][j].push_back('0'+i);
		}
	}
	string s;
	cin >> s;
	int n = s.length();
	string ans = rep[s[0]-'0'][n];
	if(ans>s){
		if(s[0]=='1'){
			cout << rep[9][n-1];
		} else {
			cout << (s[0]-'0'-1);
			cout << rep[9][n-1];
		}
		return;
	}
	string res = "";
	res.push_back(s[0]);
	for(int i=1;i<n;i++){
		bool isOk = false;
		for(int j=0;j<10;j++){
			string cur = res + rep[j][n-i];
			if(cur>s){
				res.push_back('0'+j-1);
				isOk = true;
				break;
			}
		}
		if(!isOk){
			res.push_back('9');
		}
	}
	cout << res;
}

int main(int argc, char const *argv[]){
	int T;
	cin >> T;
	for(int t=0;t<T;t++){
		cout << "Case #" << t+1 << ": ";
		main2();
		cout << endl;
	}
	return 0;
}