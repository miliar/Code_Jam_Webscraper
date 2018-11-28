#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char ans[100];

int is_tidy(int n){
    char buff[100];
    //itoa(n,buff,10);
    sprintf(buff, "%d", n);
    char *c = buff;
    while(*c){
        char *nextc = c+1;
        if(*nextc && *nextc < *c)
            return 0;
        c++;
    }
    return 1;
}

void solve(unsigned long long N){
    char buff[100];
    int digits[100];

    sprintf(buff, "%llu", N);

    int i=0;
    char *c=buff;

    while(*c){
        digits[i++] = *c - '0';
        c++;
    }

    int nd = i;

    while(1){
        //Find Answer
        int updated = 0;
        for(int i=0; i<nd-1; i++){
            if(digits[i]>digits[i+1]){
                digits[i]--;
                for(int j=i+1; j<nd; j++)
                    digits[j] = 9;
                updated = 1;
                break;
            }
        }
        if(!updated) break;
    }

    //Write answer
    int ai=0;
    for(int i=0; i< nd; i++){
        if(digits[i]){
            ans[ai++] = '0'+digits[i];
        }
    }
    ans[ai] = '\0';
}

int
main ()
{
  int T;
  long long unsigned N;
  //freopen("input.txt","r",stdin);
  //freopen("output.txt","w",stdout);
  scanf ("%d", &T);



  for(int t=1; t<=T; t++)
    {
      scanf ("%llu", &N);
      solve (N);
      printf ("Case #%d: %s\n",t, ans);
    }
  return 0;
}
