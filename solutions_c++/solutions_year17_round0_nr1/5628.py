#include<bits/stdc++.h>
using namespace std;
int stop[1005];
int main(){
  int test;
  scanf("%d",&test);
  for(int t = 1; t <= test; t ++ ){
	
	char s[1005];
	int k, siz = 0;
	scanf(" %s %d", s, &k);
	
	for(int i = 0; s[i]; i ++) {
	  stop[i] = 0;
	  siz = i + 1;
	}
	
	int ans = 0, flip = 0, ok = 1;
	for(int i = 0; s[i]; i ++ ){
	  flip -= stop[i];
	  
	  int stan = 0;
	  if ( s[i] == '+' ) stan = 1; //happy
	  if ( flip % 2 ) stan = 1 - stan;
	  
	  if ( stan == 0 ){
		if ( i + k > siz ){
		  ok = 0;
		  break;
		}
		flip ++;
		ans ++;
		stop[i + k] = 1;
	  }
	}
	printf("Case #%d: ", t);

	if ( ok ) printf("%d\n", ans );
	else printf("IMPOSSIBLE\n");
  }
  return 0;
}