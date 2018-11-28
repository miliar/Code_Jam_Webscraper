#include <cstdio>
#include <string>
using namespace std;
#define REP(i,n) for(int i=0;i<(n);++i)

const int MX = 30;
int _,h,w;
char s[MX][MX];


int main() {
  scanf("%d",&_);
  REP(t,_) {
    scanf("%d%d ",&h,&w);
    REP(i,h) gets(s[i]);

    int lst_row = -1, fst_row = -1;
    REP(i,h) {
      int num = 0; char fst = -1;
      REP(j,w) if (s[i][j] != '?') { fst = s[i][j]; break; }
      REP(j,w) if (s[i][j] != '?') ++num;
      if (num > 0) {
	char lst = fst;
	REP(j,w) {
	  if (s[i][j] != '?') lst = s[i][j];
	  else s[i][j] = lst;
	}
	lst_row = i;
	if (fst_row == -1) fst_row = i;
      } else if (lst_row != -1) {
	REP(j,w) s[i][j] = s[lst_row][j];
      }
    }
    REP(i,h) {
      if (s[i][0] == '?') {
	REP(j,w) s[i][j] = s[fst_row][j];
      }
    }

    printf("Case #%d:\n", t+1);
    REP(i,h) puts(s[i]);
  }
}
