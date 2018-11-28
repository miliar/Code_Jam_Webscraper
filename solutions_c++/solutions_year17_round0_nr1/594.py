#include <bits/stdc++.h>
typedef long long ll;

using namespace std;
int k;
void flip(string& s, int pos){
	if(pos+k>s.length()){
		return;
	}
	for(int i=pos;i<pos+k;i++){
		if(s[i]=='+'){
			s[i]='-';
		} else {
			s[i]='+';
		}
	}
}
void main2(){
	string s;
	cin >> s;
	cin >> k;
	int tot=0;
	for(int i=0;i<s.length();i++){
		if(s[i]=='-'){
			flip(s,i);
			tot++;
		}
	}
	for(int i=0;i<s.length();i++){
		if(s[i]=='-'){
			tot=-1;
		}
	}
	if(tot==-1){
		cout << "IMPOSSIBLE";
	} else {
		cout << tot;
	}
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