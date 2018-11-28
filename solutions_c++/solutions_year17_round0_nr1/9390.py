#include <bits/stdc++.h>

using namespace std;

int main(){
	int rep;
	cin >> rep;
	for(int _rep = 0; _rep < rep; _rep++){
		char pank[1000];
		int n;
		scanf("%s", pank);
		scanf("%d", &n);
		int tam;
		tam = strlen(pank);
		int resp = 0;
		for(int i = 0;i < tam - n + 1; i++){
			if(pank[i] == '-'){ //do the flip
				for(int j = i; j< i + n; j++){
					if(pank[j] == '-'){
						pank[j] = '+';
					} else {
						pank[j] = '-';
					}
				}
				resp++;
			}
			//printf("%s\n", pank);
		}
		for(int i = 0;i < tam; i++){
			if(pank[i] == '-'){
				resp = -1;
			}
		}
		cout << "Case #" << _rep+1 << ": ";
		resp != -1 ? printf("%d\n", resp) : printf("IMPOSSIBLE\n");
	}

}