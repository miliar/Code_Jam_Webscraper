#include <iostream>
#include <fstream>
#include <queue>
#include <vector>
#include <map>

#define ll long long

using namespace std;

const char* fi = "C-large.in";
const char* fo = "C-large.out";

pair<ll, ll> cj_makePair(ll n) {
  return n % 2 == 0 ? make_pair(n / 2, n / 2 - 1) : make_pair(n / 2, n / 2);
}

pair<ll, ll> solve(ll n, ll k) {
  map<ll, ll> quality_map;

  pair<ll, ll> result;
  quality_map[n] = 1;
  
  while (true) {
    map<ll, ll>::reverse_iterator top = quality_map.rbegin();
    
    result = cj_makePair(top->first);
    
    ll q = top->second;
    if (q >= k) {
      return result;
    } else {
      k -= q;
    }

    quality_map[result.first] += q;
    quality_map[result.second] += q;
    
    quality_map.erase(top->first);
  }
  
  return result;
}

int main(int argc, const char * argv[]) {
  ifstream fin;
  fin.open(fi);
  
  ofstream fout;
  fout.open(fo);
  
  int nTest;
  fin >> nTest;
  
  for (int i = 1; i <= nTest; i++) {
    ll n, k;
    fin >> n >> k;

    pair<ll, ll> result = solve(n, k);
    
    fout << "Case #" << i << ": ";
    fout << result.first << " " << result.second << endl;
  }
  
  fin.close();
  fout.close();
  return 0;
}
