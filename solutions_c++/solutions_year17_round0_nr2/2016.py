#include <iostream>
#include <vector>
#include <string>
using namespace std;

#define rep(i, from, to) for(int i = from; i < to; i++)

int main(){
 int T, last, curr; cin >> T;
 string N;
 rep(t, 0, T){
   cout << "Case #" << t+1 << ": ";
   last = 0;
   cin >> N;
   curr = 1;
   while (curr < N.size() && N[curr] >= N[curr-1]) { if(N[curr] != N[curr-1]) last = curr; curr++; }
   if (curr == N.size()) { cout << N << endl; continue; }
   rep(i, 0, N.size()){
     if (i == last && N[i] != '1') cout << char(N[i]-1);
     else if (i == last && N[i] == '1') continue;
     else if (i < last) cout << N[i];
     else cout << 9;
   }
   cout << endl;
 }
}
