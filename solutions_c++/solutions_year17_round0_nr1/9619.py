#include<stdio.h>
#include<iostream>
#include<string.h>
#include<string>
#include<ctype.h>
#include<math.h>
#include<set>
#include<map>
#include<vector>
#include<queue>
#include<bitset>
#include<algorithm>
#include<time.h>
using namespace std;
#define MS(x,y) memset(x,y,sizeof(x))
#define MC(x,y) memcpy(x,y,sizeof(x))
#define MP(x,y) make_pair(x,y)
#define ls o<<1
#define rs o<<1|1
typedef long long LL;
typedef unsigned long long UL;
typedef unsigned int UI;
template <class T1, class T2>inline void gmax(T1 &a, T2 b) { if (b>a)a = b; }
template <class T1, class T2>inline void gmin(T1 &a, T2 b) { if (b<a)a = b; }
const int N = 1010, M = 0, Z = 1e9 + 7, ms63 = 0x3f3f3f3f;
int casenum, casei;
void fre()
{
  freopen("input.in", "r", stdin);
  freopen("output.out", "w", stdout);
}
char s[2000];

int min_blank_pos(char s[], int n, int start){

  int rst = n-1;

  for (int i = start; i < n; i++)
    if (s[i] == '-'){ 
      rst = i;
      break;
    }
    
  if((rst == n-1) && (s[n-1] == '+') ) 
    rst = -1;

  //  printf("rst = %d\n", rst);

  return rst;
}

void flip(char s[], int span, int pos){
  //  printf("%s pos:%d Before flip\n", s, pos);
  for(int i = pos; i < pos + span; i++)
    {
      if(s[i] == '-') {
	s[i] = '+';
      }
      else
	s[i] = '-';
    }  
  //  printf("%s pos:%d After flip\n", s, pos);
}

int diff_in_tail(char s[], int n, int pos){
  int flag = 0;
  for(int i = pos; i < n-1; i++)
    if(s[i] != s[i+1])
      return 1;
  return 0;
}

int main()
{
  //  fre();
  scanf("%d", &casenum);
  for (casei = 1; casei <= casenum; ++casei)
    {
      int span;
      scanf("%s %d", s, &span);
      int n = strlen(s);      
      int count = 0;
      int pos = min_blank_pos(s, n, 0);

      // printf("Test #%d %s n: %d pos: %d\n", casei,s, n, pos);

      //continue to remove "-" sections
      while((pos >= 0) && (n - pos > span)){
	//	printf("Debug %s span:%d pos:%d\n", s, span, pos);
	flip(s, span, pos);

	//	printf("%s pos: %d count: %d\n", s, pos, count);
	count++;
	pos = min_blank_pos(s, n, pos);
      }

      if(pos < 0){//all '+'
	printf("Case #%d: %d\n", casei, count);
	continue;
      }

      int diff = diff_in_tail(s, n, pos);
      //  printf("diff: %s %d pos: %d\n", s, diff, pos);

      if(n-pos < span){
	//	if(diff == 1)//impossible
	  printf("Case #%d: IMPOSSIBLE\n", casei);
      }
      if(n - pos == span){
	if(diff == 1)//impossible
	  printf("Case #%d: IMPOSSIBLE\n", casei);
	else{
	  if(s[n-1] == '+'){
	    printf("Case #%d: %d\n", casei, count);
	  }
	  else//s[n] == '-'
	    printf("Case #%d: %d\n", casei, count+1);
	}
      }
    }
}
