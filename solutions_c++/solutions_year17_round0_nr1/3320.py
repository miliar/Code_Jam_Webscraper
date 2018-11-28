#include <bits/stdc++.h>

using namespace std;

string s;

void swap(int &j, int &n){
	for(int i=j; i<j+n; i++){
		if(s[i] == '-')
			s[i] = '+';
		else
			s[i] = '-';
	}
}

int main(){
	int n;
	int f =0;
	cin >> n;
	while(n--){
		int k;

		cin >> s >> k;
		int j = 0;
		for(int i=0; i<s.size() - k + 1; i++){
			if(s[i] == '-'){
				swap(i, k);
				j++;
			}
		}
		printf("Case #%d: ", ++f);
		if(s.find('-') == string::npos)
			printf("%d\n", j);
		else
			printf("IMPOSSIBLE\n");
	}
}
