#include<iostream>
#include<cstdio>
#include<vector>
#include<algorithm>
#include<functional>
#include<queue>
#include<set>
#include<cstring>
#include<cstdlib>
#include<string>

using namespace std;
class piece{
public:
  int left;
  int right;
  int center;
  int m;
  int M;
  piece(){
    left=right=center=m=M=0;
  }
  piece(int left, int right){
    this->left = left;
    this->right = right;
    center = (left + right) / 2;
    m = (center-left);
    M = (right-center);
  }
};

bool comp(piece a, piece b){
  if(a.m < b.m) return true;
  else if(a.m == b.m && a.M < b.M) return true;
  else if(a.m == b.m && a.M == b.M && a.center > b.center) return true;
  else return false;
}

int main(){
  int t, T, K, N;
  scanf("%d", &T);
  t = T;
  while(T--){
    scanf("%d %d", &N, &K);
    priority_queue<piece, vector<piece>, std::function<bool(piece, piece)>> pq(comp);
    piece init = piece(0, N-1);
    pq.push(init);
    int i=1;
    piece curr = piece();
    piece left = piece();
    piece right = piece();
    while(i<K){
      curr = pq.top();
      pq.pop();
      if(curr.m > 0){
        left = piece(curr.left, curr.center-1);
        pq.push(left);
      }
      if(curr.M > 0){
        right = piece(curr.center+1, curr.right);
        pq.push(right);
      }
      i++;
    }
    curr = pq.top();
    printf("Case #%d: %d %d\n", t - T, curr.M, curr.m);
  }
  return 0;
}
