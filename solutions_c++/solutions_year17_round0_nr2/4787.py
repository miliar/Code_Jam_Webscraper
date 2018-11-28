#include <cstdio>
#include <cstring>
using namespace std;

char s[20];
int main(){
  int N; scanf("%d\n",&N);
  for(int i = 1 ; i <= N; i++){
    scanf("%s\n",s);
    int a = 0, b =1;
    bool done = false;
    if(strlen(s) == 1) done = true;
    while(!done){
      int yi = s[a] - '0'; int er =  s[b] - '0';
      if(yi > er){
        s[a] = '0'+yi-1;
        for(int zz = b; zz < strlen(s);zz++){
          s[zz] = '0'+9;
        }
        a--;
        b--;
      }
      else{
        a++;
        b++;
      }
      if(a == strlen(s)-1 && b == strlen(s)) done = true;
    }
    long long num = 0;
    for(int j = 0 ; j < strlen(s); j++){
      num = num * 10 + (s[j] - '0');
    }
    printf("Case #%d: %lld\n",i,num );
    fflush(stdout);
  }
  return 0;
}
