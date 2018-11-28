#include<bits/stdc++.h>
using namespace std;
int tab[1005];
int main(){
  int test;
  scanf("%d",&test);
  for(int t = 1; t <= test; t ++){
	int n, k;
	scanf("%d %d", &n, &k);
	tab[0] = 1;
	tab[n + 1] = 1;
	for(int i = 1; i <= n; i ++ ) tab[i] = 0;
	int maxi,mini;
	while(k--){
	  int px = -1, py = -1, msce = 0;
	  for(int i = 1; i <= n; i ++ ){
		if ( tab[i] ) continue;
		int x = 0, y = 0;
		for(int j = i - 1;; j -- ){
		  if ( tab[j] ){
			x = i - j - 1;
			break;
		  }
		}
		for(int j = i + 1;; j ++ ){
		  if ( tab[j] ){
			y = j - i - 1;
			break;
		  }
		}
		if ( px == -1 or min(x,y) > min(px, py) ){
		  px = x;
		  py = y;
		  msce = i;
		}
		else if ( min(x,y) == min(px, py) ){
		  if ( max(x,y) > max(px,py) ){
			px = x;
			py = y;
			msce = i;
		  }
		}
	  }
	  maxi = max(px,py);
	  mini = min(px,py);
// 	  printf("msce %d\n", msce);
	  tab[msce] = 1;
	}
	printf("Case #%d: %d %d\n", t, maxi, mini );
  }
}