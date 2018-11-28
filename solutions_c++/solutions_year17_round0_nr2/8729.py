#include "stdio.h"
#include <iostream>
FILE* entrada1;
FILE* saida1;

int tomb(int &tot, int &pos){
  char leit;
  ++tot;
  int id = tot;
  fscanf(entrada1, "%c", &leit);
  int supnum = leit-'\n';
  if (leit == '\n'){
    tot = 0;
    return -1;
  }
  int num  = tomb(tot, pos);
  if (num == -1)
    return supnum;
  if (supnum > num){
    if (id < pos || pos == -1){
      pos = id;
    }
    return supnum-1;
  }
  return supnum;
}

int main(){


    entrada1 = fopen("entrada1.txt", "r");
    saida1 = fopen("saida1.txt", "w");

    int n;
    fscanf(entrada1, " %d ", &n);
    int tombs[500];

    for (int i = 1; i <=n; ++i){
      int tot = 0;
      int pos = -1;
      tomb(tot, pos);
      tombs[i] = pos;
    }
    fclose(entrada1);
  entrada1 = fopen("entrada1.txt", "r");


    fscanf(entrada1, " %d ", &n);
    for (int i = 1; i <=n; ++i){
      char t;
      bool tombA = false;
      fprintf(saida1, "Case #%d: ", i);
      do{
        fscanf(entrada1, "%c", &t);
        if (t=='\n')
          break;
        if ((tombs[i] > 1 || tombs[i] < 0)&&!tombA){
          fprintf(saida1, "%c", t);
          tombs[i]--;
        }
        else if (tombs[i] == 1 && !tombA){
          if (t -'1' > 0)
            fprintf(saida1, "%d", (t-'1'));
          tombA = true;
        }
        else{
          fprintf(saida1, "9");
        }
      }while(t != '\n');
      fprintf(saida1, "\n");
    }
}
