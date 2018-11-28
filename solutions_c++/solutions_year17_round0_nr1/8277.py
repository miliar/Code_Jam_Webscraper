#include <bits/stdc++.h>

using namespace std;

int main(){
	
	int t;

	scanf("%d", &t);

	for(int casos = 1; casos <= t; ++casos){

		string str;

		cin >> str;

		int n;

		scanf("%d", &n);

		printf("Case #%d: ",casos);

		int L,R;

		L = 0;
		R = str.size()-1;

		int resp = 0;

		while(str[L] == '+' and L < str.size()) L++;
		while(str[R] == '+' and R > 0) R--;


		while(L < str.size()){			

			while(str[L] == '+' and L < str.size()) L++;
			while(str[R] == '+' and R > 0) R--;

			if(L == str.size()) break;

			resp++;

			if(R-L+1 < n){
				resp = -1;
				break;
			}

			for(int i = L; i < L+n; i++){
				if(str[i] == '+') str[i] = '-';
				else str[i] = '+';
			}

		}

		if(resp == -1){
			printf("IMPOSSIBLE\n");
		}
		else printf("%d\n",resp);

	}

	return 0;
}