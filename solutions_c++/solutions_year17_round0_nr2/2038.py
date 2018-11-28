#include <cstdio>
#include <cstring>

#define OK            0
#define FAILED_NOUP  -1
#define FAILED_UP     1

char st[100];
int n;

int check(char *s, int n, bool& isup, int& up_location, int& failed_location)
{
  char o = '0'-1;
  isup = false;
  
  for(int i=0; i<n; i++)
    if(s[i] < o) {
      failed_location = i;
      if(isup) {
        return FAILED_UP;
      } else {
        return FAILED_NOUP;
      }
    } else {
      if((i>0) && (s[i] > o)) {
        isup = true;
        up_location = i;
      }
      o = s[i];
    }
  return OK;
}

void solve(int t)
{
  bool isup;
  int up_location, failed_location;

  scanf("%s",st);
  n = strlen(st);
  int res = check(st,n,isup,up_location,failed_location);

  printf("Case #%d: ",t);
  
  if(res == OK) {
    printf("%s",st);
  } else if(res == FAILED_NOUP) {
    if(st[0] == '1') {
      for(int i=0; i<n-1; i++) {
        printf("9");
      }
    } else {
      printf("%c",st[0]-1);
      for(int i=0; i<n-1; i++) {
        printf("9");
      }
    }
  } else {
    for(int i=0; i<up_location; i++)
      printf("%c",st[i]);
    printf("%c",st[up_location]-1);
    for(int i=up_location+1; i<n; i++)
      printf("9");
  }
  printf("\n");
}
  
main()
{
  int t;
  scanf("%d",&t);
  for(int tt=0; tt<t; tt++) {
    solve(tt+1);
  }
}
