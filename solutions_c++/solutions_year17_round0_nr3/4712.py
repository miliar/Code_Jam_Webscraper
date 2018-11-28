#include <cstdio>
#include <vector>
#include <algorithm>
#include <queue>

using namespace std;

typedef pair<int, int> P;

P split_range(int n) {
  P res;
  
  if (n%2 == 1) {
    res = make_pair(n/2,n/2);
  } else {
    res = make_pair(n/2,n/2-1);
  }
  
  return res;
}

int main(){
  int T, n, k;
  priority_queue< P, vector<P>, less<P> > dist;
  P curr;
  
  scanf("%d",&T);
  for (int t=1; t<=T; t++) {
    scanf("%d",&n);
    scanf("%d",&k);
    
    while (!dist.empty()) {
      dist.pop();
    }
    
    if (n%2 == 1) {
      dist.push(split_range(n));
    } else {
      dist.push(split_range(n));
    }
    
    //curr = dist.top();
    //printf("%d %d\n", curr.first, curr.second);
    
    for (int i=1; i<k; i++) {
      /*curr = dist.top();
      printf("%d %d\n", curr.first, curr.second);*/
      curr = dist.top();
      dist.pop();
      if (curr.first != 0) {
        dist.push(split_range(curr.first));
      }
      if (curr.second != 0) {
        dist.push(split_range(curr.second));
      }
    }
    
    curr = dist.top();
    
    printf("Case #%d: %d %d\n",t,curr.first, curr.second);
    /*while (!dist.empty()) {
      curr = dist.top();
      dist.pop();
      printf("%d %d\n",curr.first, curr.second);
    }*/
  }
  
  return 0;
}