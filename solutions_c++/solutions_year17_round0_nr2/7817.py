#include <string>
#include <iostream>
#include <cstdio>

using namespace std;

#define forsn(i,s,n) for(int i=(s); i<(int)(n); i++)
#define forn(i,n) forsn(i,0,n)

#define dforsn(i,s,n) for(int i=(n)-1; i>=(int)(s); i--)
#define dforn(i,n) dforsn(i,0,n)

void decrementar(string &s, int i){
	s[i]--;
	forsn(j, i+1, s.size()){
		s[j] = '9';	
	}
}

int main(){
	int T;
	cin >> T;
	forn(t,T){
		string s;
		cin >> s;
		
		dforn(i,s.size()-1){
			if(s[i] > s[i+1]){
				decrementar(s,i);
			}
		}
		int positivo = 0;
		while(positivo < (int)(s.size()) && s[positivo] == '0'){
			positivo++;
		}
		
		cout << "Case #" << t+1 << ": ";
		forsn(i,positivo,s.size()){
			cout << s[i];
		} cout << endl;
	}
}

