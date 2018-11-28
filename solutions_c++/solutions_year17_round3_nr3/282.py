#include<bits/stdc++.h>
using namespace std;
double tab[55], eps = 1e-6;
int main(){
  int test;
  scanf("%d",&test);
  for(int t = 1; t<= test; t ++){
	int n, k;
	scanf("%d %d", &n, &k);
	double u;
	scanf("%lf", &u);
	for(int i = 1; i <= n; i ++) scanf("%lf", &tab[i]);
	sort(tab + 1, tab + n + 1);
	tab[n + 1] = 1.0;
	int indeks = 1;
	for(int i = 1; i <= n; i ++ ){
	  double diff = tab[i + 1] - tab[i];
	  diff *= i;
	  if ( diff - u < eps ){
		indeks = i + 1;
		u -= diff;
	  }
	  else{
		u /= i;
		for(int j = 1; j <= i; j ++ ) tab[j] = tab[indeks] + u;
		indeks = -1;
		break;
	  }
	}
	if ( indeks != -1 ) for ( int j = 1; j < indeks; j ++ ) tab[j] = tab[indeks];
	double prob = 1.0;
	for(int i = n; i; i -- ) prob *= tab[i];
	printf("Case #%d: %.7lf\n", t, prob/1.0);
  }
  return 0;
}