#include<bits/stdc++.h>
using namespace std;
int main(){
  int test;
  scanf("%d", &test);
  for(int t = 1; t <= test; t ++ ){
	vector<int>v[3];
	int n, m, c;
	scanf("%d %d %d", &n, &c, &m);
	while ( m -- ) {
	  int p, b;
	  scanf("%d %d", &p, &b);
	  v[b].push_back(p);
	}
	int siz = max ( v[1].size(), v[2].size() );
	int co[3], ile[3], maxi[3];
	for(int k = 1; k <= 2; k ++ ){
	  sort(v[k].begin(), v[k].end());
	  co[k] = -1;
	  ile[k] = 0;
	  maxi[k] = 0;
	  
	  for(int i = 0; i < v[k].size(); i ++ ){
		if ( i and v[k][i] != v[k][i-1] ) {
		  if ( ile[k] > maxi[k] ) {
			maxi[k] = ile[k];
			co[k] = v[k][i-1];
		  }
		  ile[k] = 0;
		}
		ile[k] ++;
	  }
	  if ( ile[k] > maxi[k] ) {
		maxi[k] = ile[k];
		co[k] = v[k].back();
	  }
	}
	int ileco[3];
	ileco[1] = maxi[1];
	ileco[2] = maxi[2];
	for(int i = 0; i < v[1].size(); i ++ ) if ( v[1][i] == co[2] ) ileco[2] ++;
	for(int i = 0; i < v[2].size(); i ++ ) if ( v[2][i] == co[1] ) ileco[1] ++;
	int swapy = 0;
	for ( int k = 1; k <= 2; k ++ ){
	  if ( ileco[k] > siz ){
		if ( co[k] == 1 ) siz = ileco[k];
		else swapy += ileco[k] - siz;
		break;
	  }
	}
	printf("Case #%d: %d %d\n", t, siz, swapy );
  }
}