#include <cstdio>
#include <iostream>
#include <map>
using namespace std;

pair<long long, long long> BathroomStalls(const long long n, long long k){
  pair<long long, long long> answer;
  map<long long, long long> q;
  q[-n] = 1;
  while(k > 0){
    map<long long, long long>::iterator it = q.begin();
    long long len = -(it->first);
    long long counter = it->second, half = len>>1;
    if(k <= counter){
      answer = make_pair(half, half - (len%2 == 0));
      break;
    }
    q.erase(q.begin());
    q[-(half-(len%2 == 0))] += counter;
    q[-half]                += counter;
    k -= counter;
  }
  return answer;
}

int main() {
  long long n, k;
  int cases;
  while(cin >> cases){
    for(int i = 1; i <= cases; i++){
      cin >> n >> k;
      pair<long long, long long> ans = BathroomStalls(n, k);
      printf("Case #%d: %lld %lld\n", i, ans.first, ans.second);
    }
  }
  return 0;
}
