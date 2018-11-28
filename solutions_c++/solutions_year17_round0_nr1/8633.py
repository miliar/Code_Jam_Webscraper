#include "stdio.h"
#include <iostream>

int main(){
  FILE* entrada;
  FILE* saida;

  entrada = fopen("entrada.txt", "r");
  saida = fopen("saida.txt", "w");

  int n;
  fscanf(entrada, " %d ", &n);

  char s[5000];

  int cont = 1;

  while (!feof(entrada)) {
    int i = 0;
    char t;
    do {
      fscanf(entrada, "%c", &t);
      s[i] = t;
      ++i;
    } while(t != ' ');
    s[i] = 0;

    int size = i-1;

    int k;

    fscanf(entrada, " %d ", &k);

    i = 0;

    bool achou = true;

    int op = 0;

    while (i < size && achou){
      int l = i;
      while (i<l+k){
        if (s[i] == '-'){
          achou = false;
          break;
        }
      ++i;
      }

      if (!achou && i+k < size+1){
        ++op;
        achou = true;
        for (int j = i; j < i+k; ++j){
          if(s[j] == '+')
            s[j] = '-';
          else {
            s[j] = '+';
          }
          //fprintf(saida, "%s %d %d\n", s, k, size);
        }
        ++i;
      }
    }

    if (achou)
      fprintf(saida, "Case #%d: %d\n", cont, op);
    else
      fprintf(saida, "Case #%d: IMPOSSIBLE\n", cont);
    cont++;
  }
}
