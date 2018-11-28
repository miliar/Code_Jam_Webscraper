#include<stdio.h>
#include<string.h>

int main(){
  int t;
  scanf("%d",&t);
  for(int e = 0 ; e < t ; e++) {
    char s[30];
    scanf("%s",s);
    int n = strlen(s);
    long long ans = 0;
    printf("Case #%d: ",e+1);
    char a[100];
    int ct = 0;
    for(int i = 0 ; i < n ;i++ ){
      if (i < n-1 && s[i] > s[i+1]) {
        a[ct++] = s[i]-1-'0';
        int j = i;
        for(j--; j >=0 && s[j] == s[i] ; j--) {
          a[j]--;
          a[j+1] = 9;
        }
        for(i++ ; i < n ; i++) {
          a[ct++] = 9;
        }
        break;
      }
      a[ct++] = s[i] -'0';
      // printf("%c",s[i]);
    }
    for(int i = 0 ; i < n ; i++) {
      ans *=10;
      ans +=a[i];
    }
    long long nine =0;
    for(int i = 0 ; i < n-1 ; i++) {
      nine *=10;
      nine +=9;
    }
    if ( nine > ans ) ans = nine;
    printf("%lld\n",ans);
  }
}
