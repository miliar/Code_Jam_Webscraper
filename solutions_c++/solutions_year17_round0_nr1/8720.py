#include <bits/stdc++.h>
using namespace std;

string flip(string s, int begin, int end){
	for(int i=begin; i<end; i++){
		if(s[i] == '-')
			s[i] = '+';
		else
			s[i] = '-';
	}
	return s;
}

int main(){
	int T, C=0, ans, k;
	scanf("%d", &T);
	while(C++ < T){
		string vec;
		ans = 0;
		cin >> vec >> k;
		for(int i=0; i<=vec.size()-k; i++){
			if(vec[i] == '-'){
				vec = flip(vec, i,i+k);
				ans++;
			}
		}
		for(int i=vec.size()-1; i>=k; i--){
			if(vec[i] == '-'){
				vec = flip(vec, i-k,i);
				ans++;
			}
		}
		for(int i=0; i<vec.size(); i++){
			if(vec[i] == '-'){
				ans = -1;
				break;
			}
		}
		if(ans == -1){
			printf("Case #%d: IMPOSSIBLE\n", C);
		}else{
			printf("Case #%d: %d\n", C, ans);
		}
	}
	return 0;
}