#include <stdio.h>

int filas,columnas;
char pastel[25][25];
bool memo[26];

void entrada(){
	for(int i = 0;i < 26;i++) memo[i] = 0;
	scanf("%d %d\n",&filas,&columnas);
	for(int i = 0; i < filas;i++){
		for(int j = 0;j < columnas;j++){
			pastel[j][i] = getchar();
			if(pastel[j][i] != '?'){
				memo[int(pastel[j][i]-'A')] = 1;
			}
		}
		getchar();
	}
}
bool filaLibre(int fila,int minx,int maxx){
	for(int i = minx;i <= maxx;i++){
		if(pastel[i][fila] != '?')
			return false;
	}
	return true;
}
bool columnaLibre(int columna,int miny,int maxy){
	for(int i = miny;i <= maxy;i++){
		if(pastel[columna][i] != '?')
			return false;
	}
	return true;
}
void buscaLetras(char letra){
	int minx,miny,maxx,maxy;
	minx = miny = 1000;
	maxx = maxy = -1;
	for(int i = 0;i < filas;i++){
		for(int j = 0;j < columnas;j++){
			if(pastel[j][i] == letra){
				if(j < minx)
					minx = j;
				if(j > maxx)
					maxx = j;
				if(i < miny)
					miny = i;
				if(i > maxy)
					maxy = i;
			}
		}
	}
	for(int i = miny;i <= maxy;i++){
		for(int j = minx;j <= maxx;j++){
			pastel[j][i] = letra;
		}
	}	
}
void expandeColumnas(char letra){
	int minx,miny,maxx,maxy;
	minx = miny = 1000;
	maxx = maxy = -1;
	for(int i = 0;i < filas;i++){
		for(int j = 0;j < columnas;j++){
			if(pastel[j][i] == letra){
				if(j < minx)
					minx = j;
				if(j > maxx)
					maxx = j;
				if(i < miny)
					miny = i;
				if(i > maxy)
					maxy = i;
			}
		}
	}
	
	for(int i = maxx+1;i < columnas;i++){
		if(columnaLibre(i,miny,maxy)){
			maxx++;
			for(int j = miny;j <= maxy;j++){
				pastel[maxx][j] = letra;
			}
		}else{
			break;
		}
	}
	
	
	for(int i = minx-1;i >= 0;i--){
		if(columnaLibre(i,miny,maxy)){
			minx--;
			for(int j = miny;j <= maxy;j++){
				pastel[minx][j] = letra;
			}
		}else{
			break;
		}
	}
}
void expandeFilas(char letra){
	int minx,miny,maxx,maxy;
	minx = miny = 1000;
	maxx = maxy = -1;
	for(int i = 0;i < filas;i++){
		for(int j = 0;j < columnas;j++){
			if(pastel[j][i] == letra){
				if(j < minx)
					minx = j;
				if(j > maxx)
					maxx = j;
				if(i < miny)
					miny = i;
				if(i > maxy)
					maxy = i;
			}
		}
	}
	for(int i = maxy+1;i < filas;i++){
		if(filaLibre(i,minx,maxx)){
			maxy++;
			for(int j = minx;j <= maxx;j++){
				pastel[j][maxy] = letra;
			}
		}else{
			break;
		}
	}
	
	
	for(int i = miny-1;i >= 0;i--){
		if(filaLibre(i,minx,maxx)){
			miny--;
			for(int j = minx;j <= maxx;j++){
				pastel[j][miny] = letra;
			}
		}else{
			break;
		}
	}
}
void proceso(){
	for(int i = 0;i < 26;i++){
		if(memo[i]){
			buscaLetras((char)i+'A');
		}
	}
	for(int i = 0;i < 26;i++){
		if(memo[i]){
			expandeColumnas((char)i+'A');
		}
	}
	for(int i = 0;i < 26;i++){
		if(memo[i]){
			expandeFilas((char)i+'A');
		}
	}
}
void salida(){
	for(int i = 0;i < filas;i++){
		for(int j = 0;j < columnas;j++){
			printf("%c",pastel[j][i]);
		}
		printf("\n");
	}
}
int main(){
	int t;
	freopen("in","r",stdin);
	scanf("%d",&t);
	for(int i = 1;i <= t;i++){
		entrada();
		proceso();
		printf("Case #%d:\n",i);
		salida();
	}
}
