
#include <stdio.h>
#include <algorithm>
#include <utility>
#include <vector>

using namespace std;

typedef long long ll;
typedef pair<int, int> ii;
typedef vector<ii> vii;
typedef vector<int> vi;

#define INF 1000000000
#define F first
#define S second
#define forn(i,a,b) for(int i = (a); i < (b); i++)
#define rep(i,b) for(int i = 0; i < (b); i++)

using namespace std;


int main(){
	int tests;
	scanf("%d", &tests);
	forn(test,1,tests+1){
		int r,c;
		char mapa[50][50];
		scanf("%d %d", &r, &c);
		char buf[50];
		rep(i,r){
			scanf("%s", buf);
			rep(j,c){
				mapa[i][j] = buf[j];
			}
		}
		rep(j, c){
			char cur = '@';
			for(int i = 0; i < r; i++){
				if(mapa[i][j] != '?'){
					cur = mapa[i][j];
					continue;
				}
				else{
					if(cur != '@') mapa[i][j] = cur;
				}
			}
			cur = '@';
			for(int i = r-1; i >= 0; i--){
				if(mapa[i][j] != '?'){
					cur = mapa[i][j];
					continue;
				}
				else{
					if(cur != '@') mapa[i][j] = cur;
				}
			}
		}
		rep(i, r){
			char cur = '@';
			for(int j = 0; j < c; j++){
				if(mapa[i][j] != '?'){
					cur = mapa[i][j];
					continue;
				}
				else{
					if(cur != '@') mapa[i][j] = cur;
				}
			}
			cur = '@';
			for(int j = c-1; j >= 0; j--){
				if(mapa[i][j] != '?'){
					cur = mapa[i][j];
					continue;
				}
				else{
					if(cur != '@') mapa[i][j] = cur;
				}
			}
		}
		printf("Case #%d:\n", test);
		rep(i,r){
			rep(j,c){
				printf("%c", mapa[i][j]);
			}
			printf("\n");
		}
	}
	return 0;
}
