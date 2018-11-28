#include<iostream>
#include<algorithm>
#include<cstdio>
#include<cstdlib>
#include<vector>
#include<string>
#include<sstream>
#include<cmath>
#include<numeric>
#include<queue>
#include<map>
using namespace std;

int main(){

  int t;
  cin >> t;
  for(int loop=0; loop<t; loop++){
    long long int n, k;
    cin >> n >> k;
    priority_queue< pair<long long int, long long int> , vector<pair<long long int, long long int> > > q;
    q.push( make_pair( n/2, (n-1)/2 ) );
    for(int i=0; i<k; i++){
      pair<long long int, long long int> p = q.top();
      // pair<long long int, long long int> p = q.front();
      q.pop();
      q.push( make_pair(p.first/2, (p.first-1)/2) );
      q.push( make_pair(p.second/2, (p.second-1)/2) );
      // cerr << i+1 << " " << p.first << " " << p.second << endl;
      if( i == k-1 ){
        cout << "Case #" << loop+1 << ": ";
        cout << p.first << " " << p.second << endl;
      }
    }

  }


  return 0;
}


// EOF
