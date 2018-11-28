#include<iostream>
#include<queue>
#include<tuple>
#include<vector>

using namespace std;
#define repeat(i,n) for(int i=0;i<(n);i++)

int main(){

  int T;
  cin>> T;
  vector<tuple<int, int, int>> ans;
  repeat(i, T){
    int N, K;
    cin>> N>> K;
    priority_queue<tuple<int, int, int, int>> Q; // <min, max, -left, right>
    Q.push(make_tuple((N-1+1)/2-(N%2==0), (N-1+1)/2, -1, N));
    K--;
    while(K--){
      int foo, bar, l, r;
      tie(foo, bar, l, r)=Q.top(); Q.pop();
      // printf("%d %d %d %d\n", foo, bar, l, r);
      l=-l;
      if(l==r) continue;
      int m=(r+l)/2;
      // [l, m-1], [m+1, r]
      int len=(m-1)-l+1;
      int ma=len/2;
      int mi=ma-(len%2==0);
      Q.push(make_tuple(mi, ma, -l, m-1));
      len=r-(m+1)+1;
      ma=len/2;
      mi=ma-(len%2==0);
      Q.push(make_tuple(mi, ma, -(m+1), r));
    }
    int mi, ma, foo, bar;
    tie(mi, ma, foo, bar)=Q.top();
    ans.push_back(make_tuple(i+1, ma, mi));
  }

   repeat(i, ans.size()){
      int t, ma, mi;
      tie(t, ma, mi)=ans[i];
      printf("Case #%d: %d %d\n", t, ma, mi);
   }

  return 0;
}
