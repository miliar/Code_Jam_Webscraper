#include <algorithm>
#include <iostream>
#include <vector>
#include <cmath>
#include <iomanip>
using namespace std;

#define rep(i, from, to) for (int i = from; i < to; i++)

typedef long long ll;
typedef vector<ll> vi;
typedef pair<ll,ll> ii;
typedef vector<ii> vii;
typedef long double lld;

ll T, Ac, Aj, a, b, m, curchunk, totchunk0, totchunk1, chunk, cur;
vii dist;
vi type, ind, mellan0, mellan1;

bool mySort(int i, int j) { return dist[i].first < dist[j].first; }

int main(){
  cin >> T;
  rep(t, 1, T+1){
    cout << "Case #" << t << ": ";
    cin >> Ac >> Aj;
    m = 250;
    dist.clear(); type.clear(); ind.clear(); mellan0.clear(); mellan1.clear();
    rep(i, 0, Ac) {
      cin >> a >> b;
      dist.push_back(make_pair(a, b));
      type.push_back(0); ind.push_back(i);
    }
    rep(i, 0, Aj) {
      cin >> a >> b;
      dist.push_back(make_pair(a, b));
      type.push_back(1); ind.push_back(Ac+i);
    }
    sort(ind.begin(), ind.end(), mySort);
    curchunk = dist[ind[0]].second-dist[ind[0]].first;
    chunk = 0; totchunk0 = 0; totchunk1 = 0;
    rep(i, 1, Ac+Aj){
      if (type[ind[i]] != type[ind[i-1]]) {
        chunk++;
        if (type[ind[i-1]] == 0) totchunk0 += curchunk;
        else totchunk1 += curchunk;
        curchunk = dist[ind[i]].second-dist[ind[i]].first;
      }
      else {
        curchunk += dist[ind[i]].second-dist[ind[i-1]].second;
        if (type[ind[i]] == 0) mellan0.push_back(dist[ind[i]].first-dist[ind[i-1]].second);
        else mellan1.push_back(dist[ind[i]].first-dist[ind[i-1]].second);
      }
    }
    if (type[ind[Ac+Aj-1]] == 0) totchunk0 += curchunk;
    else totchunk1 += curchunk;
    if (type[ind[0]] == type[ind[Ac+Aj-1]] && type[ind[0]] == 0){
      mellan0.push_back(24*60-dist[ind[Ac+Aj-1]].second+dist[ind[0]].first);
      totchunk0 += 24*60-dist[ind[Ac+Aj-1]].second+dist[ind[0]].first;
    }
    else if (type[ind[0]] == type[ind[Ac+Aj-1]] && type[ind[0]] == 1){
      mellan1.push_back(24*60-dist[ind[Ac+Aj-1]].second+dist[ind[0]].first);
      totchunk1 += 24*60-dist[ind[Ac+Aj-1]].second+dist[ind[0]].first;
    }
    else chunk++;

    //cout << chunk << " " << totchunk0 << " " << totchunk1 << endl;

    sort(mellan0.begin(), mellan0.end());
    sort(mellan1.begin(), mellan1.end());

    /*
    rep(i, 0, mellan0.size()) cout << mellan0[i] << " ";
    cout << endl;
    rep(i, 0, mellan1.size()) cout << mellan1[i] << " ";
    cout << endl;
    */

    if (totchunk0 <= 720 && totchunk1 <= 720) cout << chunk << endl;
    else {
      if (totchunk0 > 720){
        cur = mellan0.size()-1;
        while (totchunk0 > 720 && cur >= 0) { totchunk0 -= mellan0[cur]; cur--; chunk += 2; }
        cout << chunk << endl;
      } else {
        cur = mellan1.size()-1;
        while (totchunk1 > 720 && cur >= 0) { totchunk1 -= mellan1[cur]; cur--; chunk += 2; }
        cout << chunk << endl;
      }
    }
  }
}
