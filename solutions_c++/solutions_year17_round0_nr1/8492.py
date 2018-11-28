#include <vector>
#include <queue>
#include <set>
#include <map>
#include <unordered_set>
#include <unordered_map>
#include <deque>

#include <cassert>
#include <cmath>
#include <cstring>
#include <cstdio>
#include <cstdlib>

#include <algorithm>
#include <functional>
#include <string>
#include <tuple>
#include <utility>

#include <iostream>
#include <sstream>

using namespace std;

#define forn(i,n) for(int i=0;i<(int)(n); i++)
#define forsn(i,s,n) for(int i=(s);i<(int)(n); i++)
#define esta(x,v) (find((v).begin(),(v).end(),(x)) !=  (v).end())
#define index(x,v) (find((v).begin(),(v).end(),(x)) - (v).begin())
#define debug(x) cout << #x << " = "  << x << endl

typedef long long tint;
typedef unsigned long long utint;
typedef vector<tint> vi;

void imprimirVector (vi &v){
	if (!v.empty()){
		int p = v.size();
		cout << "[";
		forn(i,p-1)
			cout << v[i] << ",";
		cout << v[p-1] << "]" << endl;
	}else
		cout << "[]" << endl;
}

tint MAXN = 10;

vi getNeighbors(tint state, tint N, tint K) {
  vi ret;
  tint mask = (1<<K) - 1;
  forn(j,N-K+1) {
    tint v = state ^ (mask<<j);
    ret.push_back(v);
  }
  return ret;
}

vector<vi> generateGraf(tint N, tint K) {
  tint nstates = 1<<N;
  vector<vi> graf(nstates, vi());
  forn(i,nstates) {
    // get neighbors
    vi neis = getNeighbors(i, N, K);
    graf[i] = neis;
  }
  return graf;
}

tint getStart(string start) {
  tint n = start.size();
  tint s = 0;
  forn(i,n) {
    if (start[i] == '-') s += (1<<i);
  }
  return s;
}

int main(){
	tint T; cin >> T;
  forn(CASE,T) {
    string start; cin >> start;
    tint N = start.size();
    tint K; cin >> K;
    
    vector<vi> graf = generateGraf(N, K);
    
    // bfs
    tint nstart = getStart(start);
    queue<tint> Q;
    vi dist(1<<N, -1);
    Q.push(nstart);
    dist[nstart] = 0;
    while(!Q.empty()) {
      tint v = Q.front(); Q.pop();
      for(auto &n : graf[v]) {
        if (dist[n] == -1) {
          dist[n] = dist[v] + 1;
          Q.push(n);
        }
      }
    }
    
    cout << "Case #" << CASE+1 << ": ";
    if (dist[0] == -1) {
      cout << "IMPOSSIBLE\n";
    } else {
      cout << dist[0] << "\n";
    }
  }
	return 0;
}
