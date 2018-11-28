#include <bits/stdc++.h>

#define ft first
#define sd second
#define mp make_pair

using namespace std;

int n, k;

struct prioritize{
  bool operator() (pair<int, int> a, pair<int, int> b){
    int menora = (a.sd - a.ft)/2;
    int maiora = (a.sd - a.ft+1)/2;

    int menorb = (b.sd - b.ft)/2;
    int maiorb = (b.sd - b.ft+1)/2;

    if(menora != menorb)
      return menora < menorb;
    if(maiora != maiorb)
      return maiora < maiorb;
    return a.ft > b.ft;
  }
};

main(){
  int ts;
  scanf("%d", &ts);

  for(int c=1;c<=ts;c++){
    printf("Case #%d: ", c);

    scanf("%d %d", &n, &k);

    priority_queue<pair<int, int>, vector<pair<int, int> >, prioritize> q;
    q.push(mp(0, n-1));

    int t = 1;
    while(!q.empty()){
      int l = q.top().ft;
      int r = q.top().sd;
      q.pop();

      if(l > r)
        continue;

      if(t == k){
        while(!q.empty())
          q.pop();
        printf("%d %d\n", (r-l+1)/2, (r-l)/2);
        break;
      }

      if((r - l) % 2 == 1){ // par
        q.push(mp((r+l)/2+1, r));
        q.push(mp(l, (r+l)/2-1));
      }
      else{
        q.push(mp(l, (r+l)/2-1));
        q.push(mp((r+l)/2+1, r));
      }

      t++;
    }
  }
}