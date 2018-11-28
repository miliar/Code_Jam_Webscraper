#include <bits/stdc++.h>
using namespace std;

int main(){
	int Test, n, k;
	char cad[1010];
	scanf("%d\n", &Test);
	for(int test=1; test<=Test; test++){
		scanf("%s %d\n", cad, &k);
		n = strlen(cad);
		
		int cnt = 0;
		for(int i=0; i<n-k+1; i++){
			if(cad[i]=='-'){
				for(int j=i; j<i+k; j++){
					cad[j] = ((cad[j]=='-')?'+':'-');
				}
				cnt++;
			}
		}
		int sw = 1;
	   
		for(int i=0; i<n; i++)
			if(cad[i]=='-') sw=0;
		if(sw)
			printf("Case #%d: %d\n", test, cnt);
		else
			printf("Case #%d: IMPOSSIBLE\n", test);
	}
	
	
	return 0;
}
