#include <stdio.h>
#include <assert.h>
#include <iostream>     // std::cout
#include <algorithm>    // std::binary_search, std::sort
#include <vector>       // std::vector
#include <list>       // std::list
#include <string>

int main(){
  FILE *fr, *fw;
  int N, K, i;
  char Number[18];
  fr = fopen("B-large.in", "r");
  fw = fopen("output.txt", "w");
  assert(1 == fscanf(fr, "%d", &N));
  for(i=0; i<N; i++){
      fscanf(fr, "%s", &Number[0]);
      int j = 0;
      bool fillNine = false;
      while(Number[j] != '\0'){
        if(fillNine)Number[j] = '9';
        else if(Number[j+1] != '\0' && Number[j]>Number[j+1]){
          while(j>0 && Number[j] == Number[j-1]){--j;}
          Number[j]=Number[j]-1;
          fillNine = true;
        }
        ++j;
      }
      // while(Number[0] == '0'){Number;}
      while(Number[0] == '0'){
        for(int k = 0; k<j;++k){
          Number[k] = Number[k+1];
        }
      }
      std::cout<< "N["<<j<<"]: "<<Number <<std::endl;


      fprintf(fw, "Case #%d: %s\n",i+1,Number);
      // if(impossible)fprintf(fw, "IMPOSSIBLE\n");
      // else fprintf(fw, "%d\n",flip);

  }

  fclose(fr);
  fclose(fw);
  return 0;

}
