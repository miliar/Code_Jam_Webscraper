#include <cstdio>
#include <cstdlib>
using namespace std;
int n,m;
char x[30][30];
void input(){
	scanf("%d %d",&n,&m);
	for(int i = 0 ;i < n ;i++)scanf("%s",x[i]);
}
void solve2(){
	for(int i = 0 ;i < n ;i++){
		char qaq = '\0';
		for(int j = 0 ;j < m ;j++){
			if(x[i][j] != '?'){
				qaq = x[i][j];
				goto nexx;
			}
		}
		continue;
		nexx:;
		for(int j = 0 ; j < m ; j++){
			if(x[i][j] == '?'){
				x[i][j]=qaq;
			}else{
				qaq = x[i][j];
			}
		}
	}
	for(int i = 0 ;i < n-1 ; i++){
		if(x[i][0] != '?' && x[i+1][0] == '?') {
			for(int j = 0 ;j < m ;j++){
				x[i+1][j] = x[i][j];
			}
		}
	}
	for(int i = n-1 ;i >= 1 ; i--){
		if(x[i][0] != '?' && x[i-1][0] == '?') {
			for(int j = 0 ;j < m ;j++){
				x[i-1][j] = x[i][j];
			}
		}
	}
	for(int i = 0 ;i < n ;i++){
		puts(x[i]);
	}
}

int main(){
	int T;
	scanf("%d",&T);
	for(int i = 1 ;i <= T ;i++){
		printf("Case #%d:\n",i);
		input();
		solve2();
	}
}
