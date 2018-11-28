#include <bits/stdc++.h>

using namespace std;

int main(){
	int t, k;
	string s;
	
	scanf("%d", &t);
	for(int o=1; o<=t; o++){
		unsigned int i, count = 0; bool blankSide = false;
		cin >> s; scanf("%d", &k);
		for(i=0; i<s.size()-k+1; ++i){
			if(s[i]=='-'){
				count++;
				for(int j=0; j<k; j++){
					s[i+j] = (s[i+j]=='-') ? '+' : '-'; 
				}
			}
		}
		for(; i<s.size(); ++i){
			if(s[i] == '-')
				blankSide = true;
		}
		printf("Case #%d: ", o);
		if(blankSide) printf("IMPOSSIBLE\n");
		else printf("%d\n", count);
	}
	return 0;
}
