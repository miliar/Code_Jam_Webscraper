#include<bits/stdc++.h>
using namespace std;
int tab[10];
int main(){
  int test;
  scanf("%d", &test);
  for(int t = 1; t <= test; t ++ ){
	for ( int i = 0 ;i < 5; i ++ ) tab[i] = 0;
	
	int n, p;
	scanf("%d %d", &n, &p);
	
	for(int i = 0; i < n; i ++){
	  int x;
	  scanf("%d", &x);
	  tab[x%p] ++;
	}
	int ans = tab[0];
	if ( p == 2 ) {
	  ans += ( tab[1] + 1 ) / 2;
	}
	if ( p == 3 ) {
	  int d = min (tab[1], tab[2]);
	  ans += d;
	  tab[1] -= d;
	  tab[2] -= d;
	  ans += ( tab[1] + 2 ) / 3;
	  ans += ( tab[2] + 2 ) / 3; //zaczete
	}
	if ( p == 4 ){
	  int d = tab[2] / 2;
	  ans += d; //pełne 2,2
	  tab[2] %= 2;
	  
	  d = min ( tab[1], tab[3] );
	  ans += d; //pełne 1,3
	  tab[1] -= d;
	  tab[3] -= d;
	  
	  int k = 1;
	  if ( tab[3] ) k = 3;
	  
	  if ( tab[2] and tab[k] > 1) { //pełne 2,1,1 lub 2,3,3
		ans ++;
		tab[2] = 0;
		tab[k] -= 2;
	  }
	  
	  ans += ( tab[k] + 3 ) / 4; //pełne 1,1,1,1 i zaczęte
	  if ( tab[k] % 4 == 0 and tab[2] ) ans ++;
	}
	printf("Case #%d: %d\n", t, ans );
  }
}