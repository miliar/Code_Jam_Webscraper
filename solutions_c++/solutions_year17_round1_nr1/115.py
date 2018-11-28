#include "bits/stdc++.h"
using namespace std;
const int N = 30;
int t;
int n , m;
char str[N][N];
int ptr;
int main(){
	scanf("%d" , &t);
	for(int tc = 1 ; tc <= t ; ++tc){
		printf("Case #%d:\n" , tc);
		scanf("%d %d" , &n , &m);
		for(int i = 1 ; i <= n ; ++i){
			scanf("%s" , str[i] + 1);
		}
		ptr = 1;
		for(int i = 1 ; i <= n ; ++i){
			bool ok = 0;
			for(int j = 1 ; j <= m ; ++j){
				if(str[i][j] != '?'){
					ok = 1;
				}
			}
			if(ok){
				int ptr2 = 1;
				for(int j = 1 ; j <= m ; ++j){
					if(str[i][j] != '?'){
						while(ptr2 <= j){
							str[i][ptr2] = str[i][j];
							++ptr2;
						}
					}
				}
				for(int j = ptr2 ; j <= m ; ++j){
					str[i][j] = str[i][ptr2 - 1];
				}
				while(ptr < i){
					for(int j = 1 ; j <= m ; ++j){
						str[ptr][j] = str[i][j];
					}
					++ptr;
				}
				++ptr;
			}
		}
		for(int i = ptr ; i <= n ; ++i){
			for(int j = 1 ; j <= m ; ++j){
				str[i][j] = str[ptr - 1][j];
			}
		}
		for(int i = 1 ; i <= n ; ++i){
			for(int j = 1 ; j <= m ; ++j){
				printf("%c" , str[i][j]);
			}
			printf("\n");
		}
	}
}