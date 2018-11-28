#include <string>
#include <iostream>
#include <vector>
#include <queue>
using namespace std;

int solve(vector<bool> &vec, int max_flip){
  queue<int> q;
  int moves{};
  size_t size_vec = vec.size();
  for (auto j = 0; j < size_vec; j++){
    if (!q.empty() && q.front() <=  j - max_flip)
      q.pop();
    if ((vec[j] ^ (q.size() % 2 == 0)) == 1){
      if (j > size_vec - max_flip)
        return -1;
      else{
        moves++;
        q.push(j);
      }
    }
  }
  return moves;
}




int main(){
  string seq;
  int n_seq, N;
  cin >> n_seq;
  int index_case = 1;
  while(n_seq--){
    cin >> seq >> N;
    size_t size_seq = seq.size();
    vector<bool> bits(seq.size());
    size_t i;
    for (i = 0; i < size_seq; i++){
      bits[i] = seq[i] == '-' ? 0 : 1;
    }
    //int ans = bits[0] ^ 1;
    //cout << ans << endl;
    
    

    int ans = solve(bits, N);
    if (ans == -1)
      printf("Case #%d: IMPOSSIBLE\n", index_case++);
    else
      printf("Case #%d: %d\n", index_case++, ans);
    
    
  }
  return 0;
}