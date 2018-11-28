#include <iostream>
#include <algorithm>
#include <vector>
#include <cstdlib>
using namespace std;

bool cmp(pair<long long, long long> a, pair<long long, long long> b) {
  if(a.first == b.first)
    return a.second > b.second;
  return a.first < b.first;
}

bool is_slow[1010];

int main() {
  int n_case;

  cin >> n_case;
  for (int i_case = 1; i_case <= n_case; ++i_case) {
    long long dest, nHorse;
    vector<pair<long long, long long> > horse;
    cin >> dest >> nHorse;
    for(int i=0; i<nHorse; i++) {
      long long start, speed;
      cin >> start >> speed;
      horse.push_back(make_pair(start, speed));
    }

    // initialize
    double ans;
    for(int i=0; i<1010; i++)
      is_slow[i] = false;

    // process
    sort(horse.begin(), horse.end(), cmp);
    // for(auto x: horse) {
    //   cout << x.first << " " << x.second << "\n";
    // }
    for(int i=0; i<nHorse; i++)
      for(int j=i+1; j<nHorse; j++)
        if( (dest-horse[i].first)*horse[j].second <= (dest-horse[j].first)*horse[i].second ) {
          is_slow[i] = true;
          break;
        }
    
    double maxTime=0;
    for(int i=0; i<nHorse; i++)
      if(!is_slow[i])
        maxTime = max(maxTime, (double)(dest-horse[i].first)/horse[i].second);
    ans = dest/maxTime;


    // display result
    printf("Case #%d: %lf\n",i_case,ans);
  }
  return 0;
}