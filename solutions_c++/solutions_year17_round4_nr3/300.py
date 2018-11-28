#include<bits/stdc++.h>
using namespace std;
//-1 #
//0 .
//1 . zabezpieczony
//2 -|

//5 |
//6 -
int tab[55][55];
char xx[55][55];
bool check ( int x, int y ){
  int a, b, h = 0, v = 0;
  
  a = x;
  b = y - 1;
  while ( tab[a][b] == 0 ) b --;
  if ( tab[a][b] > 0 ) v = 1;

  a = x;
  b = y + 1;
  while ( tab[a][b] == 0 ) b ++;
//   printf("%d\n\n", tab[a][b]);
  if ( tab[a][b] > 0 ) v = 1;
  
  a = x + 1;
  b = y;
  while ( tab[a][b] == 0 ) a ++;
  if ( tab[a][b] > 0 ) h = 1;
  
  a = x - 1;
  b = y;
  while ( tab[a][b] == 0 ) a --;
  if ( tab[a][b] > 0 ) h = 1;
  
//   printf("%d %d -- h %d b %d\n", x, y, h, v );
  if ( h and v ) return 0;
  if ( h ) tab[x][y] = 6;
  if ( v ) tab[x][y] = 5;
  return 1;
}
bool empty ( int x, int y ){
  int a, b;
  
  a = x;
  b = y - 1;
  while ( tab[a][b] == 0 ) b --;
  if ( tab[a][b] == 6 ){
	tab[x][y] = 1;
	return 1;
  }
  if ( tab[a][b] == 2 ) return 1;

  a = x;
  b = y + 1;
  while ( tab[a][b] == 0 ) b ++;
  if ( tab[a][b] == 6 ){
	tab[x][y] = 1;
	return 1;
  }
  if ( tab[a][b] == 2 ) return 1;
  
  a = x + 1;
  b = y;
  while ( tab[a][b] == 0 ) a ++;
  if ( tab[a][b] == 2 or tab[a][b] == 5){
	tab[a][b] = 5;
	tab[x][y] = 1;
	return 1;
  }
  
  a = x - 1;
  b = y;
  while ( tab[a][b] == 0 ) a --;
  if ( tab[a][b] == 2 or tab[a][b] == 5 ){
	tab[a][b] = 5;
	tab[x][y] = 1;
	return 1;
  }  
  return 0;
}
int main(){
  int test;
  scanf("%d", &test);
  for(int t = 1; t <= test; t ++ ){
	int r, c;
	scanf("%d %d", &r, &c);
	for ( int i = 1 ;i <= r; i ++ ) scanf(" %s", xx[i] + 1);
	
	for ( int i = 0; i <= r+1; i ++ )
	  for ( int j = 0; j <= c+1; j ++ ){
		if ( !i or !j or i == r+1 or j == c+1 or xx[i][j] == '#' ) tab[i][j] = -1;
		else if ( xx[i][j] == '|' or xx[i][j] == '-' ) {
		  tab[i][j] = 2; 
// 		  v.push_back ( make_pair ( i, j ) );
		}
		else {
		  tab[i][j] = 0;
// 		  e.push_back ( make_pair ( i, j ) );
		}
	  }
	  
	bool ok = 1;
	for ( int i = 1; i <= r and ok; i ++ )
	  for ( int j = 1; j <= c and ok; j ++ ) 
		if ( tab[i][j] == 2 ) ok = check ( i, j ); // sprawdzam, czy musi być jakeis konkretne
		
	bool again = 1;
	while (again and ok){
	  again = 0;
	  for ( int i = 1; i <= r and ok; i ++ )
		for ( int j = 1; j <= c and ok; j ++ ) 
		  if ( tab[i][j] == 0 ) { // jeszcze niezabezpiecozny 
			if ( empty (i, j) == 0 ) ok = 0;
			if ( tab[i][j] == 1 ) again = 1;
		  }
	}//puts("1");
	if ( ok ) 
	  for ( int i = 1; i <= r; i ++ )
		for ( int j = 1; j <= c; j ++ ) 
		  if ( tab[i][j] == 2 ) tab[i][j] = 6;
		
	if ( ok ) {
	  printf("Case #%d: POSSIBLE\n", t );
	  for ( int i = 1; i <= r; i ++ ){
		for ( int j = 1; j <= c; j ++ ) {
		  if ( tab[i][j] == 0 or tab[i][j] == 1 ) printf(".");
		  if ( tab[i][j] == -1 ) printf ("#");
		  if ( tab[i][j] == 5 ) printf("|");
		  if ( tab[i][j] == 6 ) printf("-");
		}
		puts("");
	  }
	}
	else printf("Case #%d: IMPOSSIBLE\n", t );	
  }
}