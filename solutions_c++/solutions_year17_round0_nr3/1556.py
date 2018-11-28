#include<bits/stdc++.h>
using namespace std;
void rd(int &x){
  int k, m=0;
  x=0;
  for(;;){
    k = getchar_unlocked();
    if(k=='-'){
      m=1;
      break;
    }
    if('0'<=k&&k<='9'){
      x=k-'0';
      break;
    }
  }
  for(;;){
    k = getchar_unlocked();
    if(k<'0'||k>'9'){
      break;
    }
    x=x*10+k-'0';
  }
  if(m){
    x=-x;
  }
}
void rd(long long &x){
  int k, m=0;
  x=0;
  for(;;){
    k = getchar_unlocked();
    if(k=='-'){
      m=1;
      break;
    }
    if('0'<=k&&k<='9'){
      x=k-'0';
      break;
    }
  }
  for(;;){
    k = getchar_unlocked();
    if(k<'0'||k>'9'){
      break;
    }
    x=x*10+k-'0';
  }
  if(m){
    x=-x;
  }
}
void wt_L(long long x){
  char f[20];
  int m=0, s=0;
  if(x<0){
    m=1;
    x=-x;
  }
  while(x){
    f[s++]=x%10;
    x/=10;
  }
  if(!s){
    f[s++]=0;
  }
  if(m){
    putchar_unlocked('-');
  }
  while(s--){
    putchar_unlocked(f[s]+'0');
  }
}
int main(){
  int TEST, test=0;
  rd(TEST);
  while(TEST--){
    long long K, N, now, sz;
    priority_queue< pair<long long,long long> > q;
    printf("Case #%d: ", ++test);
    fprintf(stderr, "r=%d\n", TEST);
    rd(N);
    rd(K);
    K--;
    q.push( make_pair(N, 1LL) );
    for(;;){
      now = q.top().first;
      sz = 0;
      while(q.size() && q.top().first == now){
        sz += q.top().second;
        q.pop();
      }
      if(K < sz){
        break;
      }
      K -= sz;
      q.push( make_pair( now/2, sz) );
      q.push( make_pair( (now-1)/2, sz) );
    }
    wt_L(now/2);
    putchar_unlocked(' ');
    wt_L((now-1)/2);
    putchar_unlocked('\n');
  }
  return 0;
}
// cLay varsion 20170408-3 [beta]

// --- original code ---
// {
//   int test = 0, TEST;
//   rd(TEST);
//   while(TEST--){
//     printf("Case #%d: ", ++test);
//     fprintf(stderr, "r=%d\n", TEST);
// 
//     ll N, K;
//     ll now, sz;
//     priority_queue< pair<ll,ll> > q;
//     
//     rd(N, K);
//     K--;
//     
//     q.push( make_pair(N, 1LL) );
//     for(;;){
//       now = q.top().first;
//       sz = 0;
//       while(q.size() && q.top().first == now){
//         sz += q.top().second;
//         q.pop();
//       }
//       if(K < sz) break;
// 
//       K -= sz;
//       q.push( make_pair( now/2, sz) );
//       q.push( make_pair( (now-1)/2, sz) );
//     }
// 
//     wt(now/2, (now-1)/2);
//   }
// }
