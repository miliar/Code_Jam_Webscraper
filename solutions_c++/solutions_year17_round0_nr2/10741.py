#include <stdio.h> 
#include <iostream>
#include <string.h>
#include <stdlib.h>
using namespace std;

int isMultipleOfTen(char *ptr) {
    if (*ptr != '1') 
        return 0;
    else {
        ptr++;
        while (*ptr) {
            if (*ptr != '0') 
                return 0;
            ptr++;
        }
    }
    return 1; 
}

char *GetNormalCase(char *strNum) {
    int length; 
    int pos;
    char *p = strNum;

    length = strlen(strNum);
    pos = 1;

    while (*(p+1)) {  
       if (*p > *(p+1)) {
            int goFwd = 0;
            if (pos > 1) {
                if (*p > *(p-1))
                    goFwd = 1;
            }
            if (pos == 1 || goFwd == 1) {
                *p = *p - 1;
                p++;
                while (*p) {
                    *p = '9';
                    p++;
                }
                return p;
            }
            else {
                char *fp, *bp;
                char cn;
                int bpos = pos-1;
                bp = p-1;
                fp = p;
                cn = *p;

                while (*fp) {
                    *fp = '9';
                    fp++;
                }
                //puts("being");                
                while ((*(bp) == cn) && (bpos)) {
                    if (bpos > 1) 
                        *bp = '9';
                    else 
                        *bp = *bp-1;
                    bpos--;
                    bp = bp - 1;
                }
            }
       } 
       pos++;
       p++;
    }
    return strNum;
}


int main(int argc, char* argv[]) {

  FILE* fptr;
  int nCases;
  int caseIdx;

  char c;
  char strNum[20] = "";

  fptr = fopen(argv[1], "r");//fptr = fopen(argv[1],"r");
  fscanf(fptr,"%d",&nCases);

  for (caseIdx = 1; caseIdx <= nCases; caseIdx++) {
      fscanf(fptr,"%s",strNum);

      if (strlen(strNum) == 1) 
      {
          printf("Case #%d: %s\n", caseIdx, strNum);
      }
      else if (isMultipleOfTen(strNum)) 
      {
         long long a = atoll(strNum);
         a--;
         printf("Case #%d: %lld\n", caseIdx, a);
      }
      else 
      {
         char *p = GetNormalCase(strNum);
         printf("Case #%d: %s\n", caseIdx, strNum);
      }
  }
  return 1;
}
