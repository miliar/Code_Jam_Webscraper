#include <bits/stdc++.h>

using namespace std;
int ntest,k;
string s;

void solve(int test){	
	cout << "Case #" << test+1 << ": ";
	cin.ignore();
	cin >> s >> k;
	int res = 0;
	for(int i=0; s[i+k-1]; i++ ){
		if(s[i] == '-'){
			for(int j=0; j<k; j++){
				if(s[i+j] == '-') s[i+j] = '+';
				else s[i+j] = '-';
			}
			res++;		
		}
	}
	for(int i=0; s[i]; i++){
		if(s[i] == '-') {		
			cout << "IMPOSSIBLE" << endl; return;
		}
	}
	cout << res << endl;
}


int main(){
	freopen("A-large.in","r",stdin);
	freopen("test.out","w",stdout);	
	cin >> ntest;
	for(int test=0; test<ntest; test++){
		solve(test);
	}
	return 0;
}
