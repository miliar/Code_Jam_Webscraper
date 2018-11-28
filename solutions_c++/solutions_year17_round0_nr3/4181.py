#include <iostream>
#include <stack>
#include <string>
#include <vector>
#include <algorithm>
#include <set>
#include <queue>
using namespace std;

void clear( std::priority_queue<long long int> &q )
{
   std::priority_queue<long long int> empty;
   std::swap( q, empty );
}

int main()
{
  int n;
  long long int N, K, tmp, l, r;
  priority_queue<long long int> Q;
  cin >> n;
  for(int i = 0; i < n; i++){
    cin >> N >> K;
    l = r = 0;
    clear(Q);
    Q.push(N);
    for(int j = 0; j < K; j++){
      if(Q.top() % 2 == 0){
        tmp = Q.top();
        l = (tmp / 2) - 1;
        r = tmp / 2;
        Q.pop();
        if(r) Q.push(r);
        if(l) Q.push(l);
      }else{
        tmp = Q.top();
        l = r = (tmp - 1) / 2;
        Q.pop();
        if(r) Q.push(r);
        if(l) Q.push(l);
      }
    }
    cout << "Case #" << i + 1 << ": " << r << " " << l << endl;
  }
  return 0;

}