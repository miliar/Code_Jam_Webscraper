#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <iostream>
#include <map>
using namespace std;
unsigned long long N, K;

char ans[1000];

map<unsigned long long, unsigned long long> stalls;

void solve(){
    unsigned long long cnt_allocated = 0;
    unsigned long long cur_stall, cnt_cur_stalls, ls, rs;

    stalls.clear();

    stalls[N] = 1;

    while(!stalls.empty()){
        cur_stall = stalls.rbegin()->first;

        cnt_cur_stalls = stalls.rbegin()->second;

        stalls.erase(stalls.rbegin()->first);

        cnt_allocated += cnt_cur_stalls;

        ls = (cur_stall-1)/2;
        rs = ((cur_stall-1)+1)/2;

        if(K <= cnt_allocated){
            sprintf(ans, "%llu %llu",rs, ls);
            return;
        }

        if(ls) stalls[ls] += cnt_cur_stalls;
        if(rs) stalls[rs] += cnt_cur_stalls;
    }

}

int
main ()
{
  int T;
   // freopen("input.txt", "r", stdin);
   // freopen("output.txt", "w", stdout);
  scanf ("%d", &T);

  for(int t=1; t<=T; t++)
    {
      scanf("%llu %llu", &N, &K);
      solve();
      printf ("Case #%d: %s\n",t, ans);
    }
  return 0;
}
