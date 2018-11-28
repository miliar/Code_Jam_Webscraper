#include<bits/stdc++.h>
using namespace std;
#define N 108
#define f first
#define s second
typedef pair<int,int> PII;
PII arr[N];
int n,k;
double PI = 3.14159265358979323846264338327950;
long long inf = 1e8;
long long memo[N][N][N];
long long dp(int pos, int pq, int ls){
      if(pos >= n){
            if(pq == k){
                  return 1LL*arr[ls].f*arr[ls].f;
            }
            return -1LL*inf*inf;
      }
      if(memo[pos][pq][ls] != -1LL)return memo[pos][pq][ls];
      long long a = 2LL*arr[pos].f*arr[pos].s;
      if(ls == 105){
            return memo[pos][pq][ls] = max( a + dp(pos+1, pq+1,pos), dp(pos+1,pq,ls));
      }else{
         a += abs(1LL*arr[ls].f*arr[ls].f - 1LL*arr[pos].f*arr[pos].f);
         return memo[pos][pq][ls] = max( a + dp(pos+1, pq+1, pos), dp(pos+1,pq,ls));
      }
}
int main(){
    int t,r,h;
    cin>>t;
    for (int T = 1; T <= t; ++T){
      cin>>n>>k;
      for (int j = 0; j < n; ++j){
      	cin>>r>>h;
            arr[j] = make_pair(r,h);
      }
      for (int i = 0; i < N; ++i){
            for (int j = 0; j < N; ++j){
                  for (int k = 0; k < N; ++k){
                        memo[i][j][k] = -1LL;
                  }
            }
      }
      sort(arr,arr+n);
      reverse(arr,arr+n);
      double tot = dp(0,0,105);
      printf("Case #%d: %0.9lf\n",T,PI*tot);
    }
}