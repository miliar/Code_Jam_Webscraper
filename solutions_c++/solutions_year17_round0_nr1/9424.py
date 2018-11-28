#include <iostream>
#include <cstring>
#include <cstdio>

using namespace std;

int main(){
  freopen("input.txt","r",stdin);
  freopen("output.txt","w",stdout);
  int T ;
  scanf("%d\n",&T);

  for(int tt = 1 ; tt <= T ; ++ tt){
    char s[1010] ;
    int k ; 
    scanf("%s %d\n",s,&k);
    int n = strlen(s);
    int ans = 0;
    for(int i = 0; i <= n - k ; ++ i)
      if(s[i] == '-'){
	++ ans;
	for(int j = 0; j < k ; ++ j)
	  if(s[i + j] == '+')
	    s[i + j] = '-' ;
	  else
	    s[i + j] = '+' ;
      }
    printf("Case #%d: ",tt);

    bool flag = 1;
    for(int i = 0; i < n ;++ i) flag &= s[i] == '+';
    if(flag)
      cout << ans << endl;
    else
      puts("IMPOSSIBLE");
    
  }
}
