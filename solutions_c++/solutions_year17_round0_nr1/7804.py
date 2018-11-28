#include <string>
#include <iostream>
#include <cstdio>

using namespace std;

#define forsn(i,s,n) for(int i=(s); i<(int)(n); i++)
#define forn(i,n) forsn(i,0,n)

char inverso(char c){
	if(c=='+') return '-';
	return '+';
}

int main(){
	int T;
	cin >> T;
	forn(t,T){
		int total = 0;
		string s;
		cin >> s;
		int k; cin >> k;
		forn(i,s.size()-k+1){
			if(s[i] == '-'){
				forn(j,k){
					s[i+j] = inverso(s[i+j]);
				}
				total++;
			}
		}
		bool res = true;
		forn(i,s.size()){
			if(s[i] == '-') res = false;
		}
		cout << "Case #" << t+1 << ": ";
		if(res){
			cout << total << endl;
		} else {
			cout << "IMPOSSIBLE\n";
		}
	}
}
