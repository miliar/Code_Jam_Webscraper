#include <iostream>
#include <stdio.h>
using namespace std;

int main(){
	freopen("salida.out", "w", stdout);
	int n, t, k;
	string s;

	cin >> t;

	for(int z = 1; z<= t; z++){
	   cin >> s >> k;

	   	 bool possible = true;
	   	 int ans = 0;
	     for(int i = 0; i< s.size(); i ++){
	     	if(s[i] == '-'){
	     		int cont = k-2;
	     		ans++;
	     		if(i+k > s.size()){
	     			possible = false;
	     			break;
	     		}
	     		for(int j = i+1; cont >= 0 ; j++, cont--){
	     			if(s[j] == '-') s[j] = '+';
	     			else s[j] = '-';
	     		}

	     	}
	     }
	   
	   cout << "Case #" << z << ": " ;
	   if(possible ) cout << ans << '\n';
	   else cout << "IMPOSSIBLE" << '\n';

	}
	return 0;
}