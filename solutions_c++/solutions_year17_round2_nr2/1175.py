#include<bits/stdc++.h>
using namespace std;
int tab[1005];
int main(){
  int test;
  scanf("%d",&test);
  for(int t = 1; t <= test; t ++){
	int n, r,o,y,g,b,v;
	scanf("%d",&n);
	scanf("%d%d%d%d%d%d", &r,&o,&y,&g,&b,&v);
	
	bool ok = 1;
	r -= g;
	b -= o;
	y -= v;
	int m = 0;
	if ( r < 0 or b < 0 or v < 0 ) ok = 0;
	else{
	  m = r + b + y;
	  vector<pair<int,int> > x;
	  x.push_back(make_pair(r, 1));
	  x.push_back(make_pair(b, 2));
	  x.push_back(make_pair(y, 3));
	  sort(x.begin(),x.end());
	  
	  if ( x[2].first * 2 > m ) ok = 0;
	  else{
		for(int i = 0; i < m; i ++ ) tab[i] = 0;
		
		for(int i = 0; i < m and x[2].first; i += 2 ) {
		  tab[i] = x[2].second;
		  x[2].first --;
		}
		int k = 0;
		for(int i = m -1; i >= 0; i -- ){
		  if ( tab[i] ) continue;
		  if ( x[k].first ){
			tab[i] = x[k].second;
			x[k].first --;
			k = 1-k;
		  }
		  else{
			k = 1-k;
			tab[i] = x[k].second;
			x[k].first --;
		  }
		}
	  }
	  if ( m == 0 ){
		if ( g and o ) ok = 0;
		if ( o and v ) ok = 0;
		if ( v and g ) ok = 0;
	  }
	}
	printf("Case #%d: ", t);
	if ( !ok ) puts("IMPOSSIBLE");
	else{
	  for(int i = 0; i < m; i ++ ) {
		if ( tab[i] == 1 ){
		  printf("R");
		  if ( g ){
			printf("GR");
			g --;
		  }
		}
		if ( tab[i] == 2 ){
		  printf("B");
		  if ( o ){
			printf("OB");
			o --;
		  }
		}
		if ( tab[i] == 3 ){
		  printf("Y");
		  if ( v ){
			printf("VY");
			v --;
		  }
		}
	  }	  
	  while(g--) printf("GR");
	  while(o--) printf("OB");
	  while(v--) printf("VY");
	  puts("");
	}
  }
  return 0;
}