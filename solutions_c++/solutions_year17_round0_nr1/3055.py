#include<stdio.h>
#include<string.h>

using namespace std;

char cambio(char a){
	return a == '+' ? '-' : '+';
}

int main(){
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	int t,l,k,lim,con;
	char cad[1020];
	scanf("%d",&t);
	getchar();
	for (int c = 1; c <= t; c++){
		scanf("%s",cad);
		getchar();
		l = strlen(cad);
		scanf("%d",&k);
		getchar();
		lim = l - k;
		con = 0;		
		for (int i = 0; i <= lim; i++){
			if (cad[i] == '-'){
				for (int j = 0; j < k; j++){
					cad[j + i] = cambio(cad[j+i]);
				}
				con++;
			}
		}
		bool ok = true;
		for (int i = lim + 1; i < l; i++){
			if (cad[i] != '+'){
				ok = false;
				break;
			}
		}
		if (ok){
			printf("Case #%d: %d\n",c,con);
		}
		else{
			printf("Case #%d: IMPOSSIBLE\n", c);
		}
	}
	return 0;
}