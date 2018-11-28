

#include <iostream>
#include <queue>
#include <stdint.h>
using namespace std; 

int main() 
  { 
  ios::sync_with_stdio(false);
  cin.tie(NULL);

  int T;

  uint64_t N, K, a,b;
  cin >> T;
  for(int o=0; o<T; o++){
  cout << "Case #" << o+1<<": ";
      cin >> N >> K;
      priority_queue< uint64_t > q;
      q.push(N);
      for(int i=0; i<K; i++){
          a=q.top()-1;
          b=a/2; a=a-b;
          q.push(a); q.push(b);
         // cout << q.top()<< ' ';
          q.pop();
         // cout << q.top()<< ' ';
         
      }
      cout << a << ' ' << b<<'\n';
  } 

return 0; 
} 
 