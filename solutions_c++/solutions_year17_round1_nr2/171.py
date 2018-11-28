#include <bits/stdc++.h>

#define eps 1e-9
using namespace std;

int ing[60][60];
bool used[60][60];
int need[60];
long long low[60], high[60];

main(){
  int t;
  scanf("%d", &t);

  for(int c=1;c<=t;c++){
    int n, p;
    scanf("%d %d", &n, &p);

    for(int i=0;i<n;i++)
      scanf("%d", &need[i]);

    for(int i=0;i<n;i++){
      for(int j=0;j<p;j++){
        scanf("%d", &ing[i][j]);
        used[i][j] = false;
      }
      sort(ing[i], ing[i]+p);
    }

    int ans = 0;
    long long receitas = 1;

    while(1){
      int cont = p-ans;
      bool parar = false;

      for(int i=0;i<n;i++){
        low[i] = long(0.9*receitas*need[i]) + (0.9*receitas*need[i]-eps > long(0.9*receitas*need[i]));
        high[i] = long(1.1*receitas*need[i]); 
      }

      for(int i=0;i<n;i++){
        int cont_atu = 0;
        for(int j=0;j<p;j++)
          if(!used[i][j] && ing[i][j] >= low[i] && ing[i][j] <= high[i])
            cont_atu++;
        cont = min(cont_atu, cont); 
        parar |= ing[i][p-1] < low[i];
      }

      ans += cont;
      for(int i=0;i<n;i++){
        int mud = 0;
        for(int j=0;j<p && mud<cont;j++){
          if(!used[i][j] && ing[i][j] >= low[i] && ing[i][j] <= high[i]){
            used[i][j] = true;
            mud++;
          }
        }
      }

      if(parar || ans == p)
        break;

      receitas++;
    }

    printf("Case #%d: %d\n", c, ans);
  }
}