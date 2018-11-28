#include <bits/stdc++.h>

using namespace std;

int n;

void mark(int x, int y, bool bishop[110][110]){
	int a = x-(y-1);
	if(a>0){
		bishop[a][1] = true;
	}
	a = x+(y-1);
	if(a<=n){
		bishop[a][1] = true;
	}
	a = x - (n-y);
	if(a>0){
		bishop[a][n] = true;
	}
	a = x + (n-y);
	if(a<=n){
		bishop[a][n] = true;
	}
	a = y-(x-1);
	if(a>0){
		bishop[1][a] = true;
	}
	a = y+(x-1);
	if(a<=n){
		bishop[1][a] = true;
	}
	a = y - (n-x);
	if(a>0){
		bishop[n][a] = true;
	}
	a = y + (n-x);
	if(a<=n){
		bishop[n][a] = true;
	}
}

void solvre(){
	int m;
	scanf("%d %d", &n, &m);
	int x, y;
	char ch;
	char original[110][110] = {0};
	char final[110][110] = {0};
	bool bishop[110][110] = {false};
	bool col[110] = {false};
	bool row[110] = {false};
	int a, b;
	int pontos = 0;

	for(int i = 0; i<m; i++){
		scanf(" %c %d %d", &ch, &x, &y);
		original[x][y] = final[x][y] = ch;
		if(ch=='+'){
			pontos++;
			mark(x, y, bishop);
		}else if(ch=='x'){
			pontos++;
			row[y] = true;
			col[x] = true;
		}else{
			pontos++;
			mark(x, y, bishop);
			pontos++;
			row[y] = true;
			col[x] = true;
		}
	}
	//fsdjkl flkçsadjfkljs dalkfj lkçsdajfklj sdlçfj
	//fsdjkl flkçsadjfkljs dalkfj lkçsdajfklj sdlçfj
	//fsdjkl flkçsadjfkljs dalkfj lkçsdajfklj sdlçfj
	// printf("\n");
	// for(y = 1; y<=n; y++){
	// 	for(x = 1; x<=n; x++){
	// 		if(final[x][y]==0) final[x][y] = '.';
	// 		printf("%c", final[x][y]);
	// 	}
	// 	printf("\n");
	// }


	//fsdjkl flkçsadjfkljs dalkfj lkçsdajfklj sdlçfj
	//fsdjkl flkçsadjfkljs dalkfj lkçsdajfklj sdlçfj


	for(y = 1; y<=n; y++){
		if(row[y]) continue;
		for(x = 1; x<=n; x++){
			if(!col[x]){
				row[y] = col[x] = true;
				pontos++;
				if(final[x][y]=='+'){
					final[x][y] = 'o';
				}else final[x][y] = 'x';
				break;
			}
		}
	}
	y = 1;
	for(x = 1; x<=n; x++){
		if(!bishop[x][1]){
			mark(x, y, bishop);
			pontos++;
			if(final[x][1] == 'x') final[x][1] = 'o';
			else final[x][1] = '+';

		}
	}	
	y = n;
	for(x = 2; x<n; x++){
		if(!bishop[x][n]){
			mark(x, y, bishop);
			pontos++;
			if(final[x][n] == 'x') final[x][n] = 'o';
			else final[x][n] = '+';
		}
	}
	x = 1;
	for(y = 1; y<=n; y++){
		if(!bishop[x][y]){
			mark(x, y, bishop);
			pontos++;
			if(final[x][y] == 'x') final[x][y] = 'o';
			else final[x][y] = '+';
		}
	}	
	x = n;
	for(y = 2; y<n; y++){
		if(!bishop[x][y]){
			mark(x, y, bishop);
			pontos++;
			if(final[x][y] == 'x') final[x][y] = 'o';
			else final[x][y] = '+';
		}
	}


	int cont = 0;
	for(y = 1; y<=n; y++){
		for(x = 1; x<=n; x++){
			if(final[x][y] != original[x][y] && final[x][y]!='.') cont++;
		}
	}
	//fsdjkl flkçsadjfkljs dalkfj lkçsdajfklj sdlçfj
	//fsdjkl flkçsadjfkljs dalkfj lkçsdajfklj sdlçfj
	//fsdjkl flkçsadjfkljs dalkfj lkçsdajfklj sdlçfj
	// printf("\n");
	// for(y = 1; y<=n; y++){
	// 	for(x = 1; x<=n; x++){
	// 		if(final[x][y]==0) final[x][y] = '.';
	// 		printf("%c", final[x][y]);
	// 	}
	// 	printf("\n");
	// }


	//fsdjkl flkçsadjfkljs dalkfj lkçsdajfklj sdlçfj
	//fsdjkl flkçsadjfkljs dalkfj lkçsdajfklj sdlçfj



	printf("%d %d\n", pontos, cont);
	for(y = 1; y<=n; y++){
		for(x = 1; x<=n; x++){
			if(final[x][y] != original[x][y]){
				printf("%c %d %d\n", final[x][y], x, y);
			}
		}
	}
}

int main(){
	int t;
	cin>>t;
	for(int i = 1; i<=t; i++){
		printf("Case #%d: ", i);
		solvre();
	}

}