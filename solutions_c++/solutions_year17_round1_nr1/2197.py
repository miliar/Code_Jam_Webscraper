#include <cstdio>
#define max_c 30

int T,r,c;
char cake[max_c][max_c];

void init(){
	for(int i = 0 ;i < r; i++){
		for(int j = 0; j < c; j ++){
			cake[i][j] = '\0';
		}
	}
}

void p(int i){
	printf("Case #%d:\n",i);
	for(int i = 0; i < r; i ++){
		printf("%s\n", cake[i]);
	}
}

void solve(){
	for(int i = 0; i < r ; i ++){
		for(int j = 0; j < c; j++){
			if(cake[i][j] != '?'){
				for(int k = i - 1; k > -1; k--){
					if(cake[k][j] == '?') {	cake[k][j] = cake[i][j];}
					else{ break;}
				}
				for(int k = 1 ; k < r - i; k ++){
					if(cake[i + k][j] == '?') {cake[i+k][j] = cake[i][j];}
					else {break;}
				}
			}
		}
	}


	for(int j = 0; j < c; j++){
		bool filled = false;
		if(cake[0][j] == '?'){
			for(int k = j ; k > -1; k--){
				if(cake[0][k] != '?'){
					for(int s = k ; s < j + 1; s++){
						for(int i = 0; i < r; i ++){
							cake[i][s] = cake[i][k];
						}
					}
					filled = true;
					break;
				}
			}
			if(!filled){
				for(int k = j ; k < c ; k++){
					if(cake[0][k] != '?'){
						for(int i = 0; i < r; i++){
							cake[i][j] = cake[i][k];
						}
						break;
					}
				}
			}
		}
	}

}



int main(){
	scanf("%d",&T);
	for(int j = 0; j < T ; j++){
		init();
		scanf("%d %d", &r, &c);
		for(int i = 0; i < r; i++){
			scanf("%s", cake[i]);
		}
		solve();
		p(j+1);
	}
}
