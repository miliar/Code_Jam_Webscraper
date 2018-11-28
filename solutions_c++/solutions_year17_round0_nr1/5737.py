#include <bits/stdc++.h>
using namespace std;

int main(){
	int T,K,cont;
	bool possible;
	string pank;
	cin >> T;
	
	for (int testCase = 1; testCase<=T; ++testCase){
		possible = true;
		cont = 0;
		cin >> pank;
		cin >> K;
		for (int i = 0; i < pank.size();++i){
			if (pank[i] == '-'){
				if (i<=pank.size()-K)
				for (int k = i; k < i+K;++k){
					if (pank[k] == '+')
						pank[k] = '-';
					else pank[k] = '+';
				}
				else possible = false;
				cont ++;
			}
		} 
		if (possible) printf("Case #%d: %d\n",testCase,cont);
		else printf("Case #%d: IMPOSSIBLE\n",testCase) ;
	}
	
	return 0;
}
