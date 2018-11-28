#include<stdio.h>
#include<map>

void solve(){
  long long int N, K; scanf("%lld %lld", &N, &K);
  std::map<long long int, long long int> cnt;
  cnt[N] = 1;
  while(K!=0){
    std::map<long long int, long long int>::iterator it = cnt.end(); it--;
    long long int l = it->first;
    long long int c = it->second;
    cnt.erase(it);
    if(K>c){
      cnt[l/2] += c;
      cnt[(l-1)/2] += c;
      K -= c;
    }else{
      cnt.clear();
      printf("%lld %lld\n", l/2, (l-1)/2);
      K = 0;
    }
  }
}

int main(int agrc, char *argv[]){
  int T; scanf("%d", &T);
  for(int tc=1; tc<=T; tc++){
    printf("Case #%d: ", tc);
    solve();
  }
  return 0;
}
