#include<iostream>
#include<algorithm>
#include<vector>
#include<string>
#include<queue>

using namespace std;
#define REP(i,n) for(int i=0;i<(int)n;++i)
typedef long long int ll;


void solve() {
  long long int n,k;
  cin>>n>>k;

  queue<pair<ll ,ll > > q;
  q.push(make_pair(n,1));  
  while(k) {
    ll mark=q.front().first;
    ll count=0;
    while(!q.empty() && mark==q.front().first) {count+=q.front().second;q.pop();}
    if(k<=count) {
      ll c1=(mark-1)/2;
      ll c2=mark/2;
      cout<<c2<<" "<<c1<<endl;
      return;
    } else {
      k-=count;
      if(mark%2) {
        q.push(make_pair(mark/2, count*2));
      } else {
        q.push(make_pair(mark/2,count));
        q.push(make_pair(mark/2-1,count));
      }

    }
  }
}
int main() {
  int t;cin>>t;REP(i,t) {
    cout<<"Case #"<<(i+1)<<": ";
    solve();
  }

}
