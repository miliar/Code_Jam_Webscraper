#include<iostream>
#include<algorithm>
#include<vector>
#include<string>
#include<queue>
using namespace std;
#define REP(i,n) for(int i=0;i<(int)n;++i)
typedef long long int ll;


void solve() {
  int n;string s;
  cin>>s>>n;
  int flips=0;
  queue<int> q;
  for(int i=0;i<s.size();++i) {
    int unhappy=s[i]=='-';  // unhappy means 1
    int flipped=(q.size()%2);
    unhappy ^= flipped;
    if(unhappy) {
        flips++;
        q.push(i+n);
    }
    while(!q.empty() && q.front()<=i+1 ) q.pop();
  }
  if(q.empty()) cout<<flips<<endl;
  else cout<<"IMPOSSIBLE"<<endl;
}
int main() {
  int t;cin>>t;REP(i,t) {
    cout<<"Case #"<<(i+1)<<": ";
    solve();
  }

}
