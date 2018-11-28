#include <iostream>
#include <queue>
#include <fstream>

using namespace std;

const int MAXN = 1e3 + 10;

ifstream fin("c_small.in");
ofstream fout("c_small.out");

#define cin fin
#define cout fout

int t , n , k;
int max_res , min_res;

void solve(){
  priority_queue <int> q;
  q.push(n);
  for(int i = 0 ; i < k ; i++){
    int x = q.top() - 1;
    max_res = x - (x/2);
    min_res = x/2;
    q.pop();
    q.push(max_res);
    q.push(min_res);
  }
} 

void input(){
  cin >> t;
  for(int i = 1 ; i <= t ; i++){
    cin >> n >> k;
    solve();
    cout << "Case #" << i << ": " << max_res << " " << min_res << endl;
  }
}

int main(){
  input();
  return 0;
}
