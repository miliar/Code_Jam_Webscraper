#include<cstdio>
#include<algorithm>
#include<stdlib.h>
#include<vector>
#include<iostream>
#include<map>
#include<queue>
#include<cstdlib>
#include<cstring>
#include<string>
#include<set>

using namespace std;

const int maxn = 1024;
char line[maxn];
int arr[maxn];
int size, flipper;

typedef long long int huge;

void flip(int i){
  //printf("\ni %d flipper %d size %d", i, flipper, size);
  if(i + flipper <= size)
    for(int j = i; j<i+flipper; ++j)
      if(arr[j])
        arr[j] = 0;
      else
        arr[j] = 1;
}

void print_arr(){
  for(int i = 0; i<size; ++i){
    printf("%d", arr[i]);
  }
  printf("\n");
}


int main(){
  int t, count = 0, possible, flips;
  char aux;

  scanf("%d%*c", &t);

  while(t--){
    printf("Case #%d: ", ++count);
    gets(line);

    for(size = 0; line[size]; ++size){
      sscanf(line+size, "%c", &aux);

      if (aux != ' ')
        if (aux == '-')
          arr[size] = 0;
        else
          arr[size] = 1;
      else{
        sscanf(line+size+1, "%d", &flipper);
        break;
      }
    }

    flips = 0;
    for(int i = 0; i<size; ++i){
      if(!arr[i])
        flip(i), ++flips;
    }

    possible = 1;
    for(int i = 0; i<size; ++i)
      if(!arr[i])
        possible = 0;

    if(possible)
      printf("%d\n", flips);
    else
      printf("IMPOSSIBLE\n");
    //print_arr();
  }

  return 0;
}
