#include <bits/stdc++.h>

#define ft first
#define sd second
#define mp make_pair
#define pb push_back

using namespace std;

int v[105];
int cont[105];

main(){
  int t;
  scanf("%d", &t);

  for(int c=1;c<=t;c++){
    int n, p;
    scanf("%d %d", &n, &p);

    for(int i=0;i<n;i++){
      scanf("%d", &v[i]);
      cont[v[i]]++;
    }

    printf("Case #%d: ", c);

    if(p == 1)
      printf("%d\n", n);
    else if(p == 2){
      int ans = 0;
      int impar = 0;
      for(int i=1;i<=100;i++){
        if(i%2==1)
          impar += cont[i];
        else
          ans += cont[i];
      }
      ans += ((impar+1)/2);
      printf("%d\n", ans);
    }
    else if(p == 3){
      int ans = 0;
      int resto1 = 0;
      int resto2 = 0;
      for(int i=1;i<=100;i++){
        if(i%3 == 1)
          resto1 += cont[i];
        else if(i%3 == 2)
          resto2 += cont[i];
        else
          ans += cont[i];
      }
      int aux = min(resto1, resto2);
      resto1 -= aux;
      resto2 -= aux;

      ans += aux + (resto1+2)/3 + (resto2+2)/3;
      printf("%d\n", ans);
    }
    else{
      int ans = 0;
      int resto1 = 0;
      int resto2 = 0;
      int resto3 = 0;

      for(int i=1;i<=100;i++){
        if(i % 4 == 1)
          resto1 += cont[i];
        else if(i % 4 == 2)
          resto2 += cont[i];
        else if(i % 4 == 3)
          resto3 += cont[i];
        else
          ans += cont[i];
      }

      int aux = min(resto1, resto3); // pares 3 1
      resto1 -= aux;
      resto3 -= aux;
      ans += aux;

      // aqui n vai ter 3 e/ou n vai ter 1:

      if(resto1 == 0){ // nao tem + 1, pode ou nao ter 3
        aux = resto2/2; // pares 2 2
        resto2 -= aux*2;
        ans += aux;

        if(resto2 == 1 && resto3 >= 2){ // triplas 2 3 3
          resto2 -= 1;
          resto3 -= 2;
          ans++;
        }
        else if(resto2 == 1 && resto3 % 4 == 0) // sobrou um pacote de 2 no fim
          ans++;

        ans += (resto3 + 3)/ 4; // quadruplas 3 3 3 3
      }
      else{ // nao tem + 3, pode ou nao ter 1
        aux = resto2/2; // pares 2 2
        resto2 -= aux*2;
        ans += aux;
        
        if(resto2 == 1 && resto1 >= 2){ // triplas 2 1 1
          resto2 -= 1;
          resto1 -= 2;
          ans++;
        }
        else if(resto2 == 1 && resto1 % 4 == 0) // sobrou um pacote de 2 no fim
          ans++;
  
        ans += (resto1 + 3) / 4;
      }
      printf("%d\n", ans);
    }

    memset(cont, 0, sizeof cont);
  }
}