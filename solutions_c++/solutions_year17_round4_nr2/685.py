#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <algorithm>
#include <cmath>
#include <queue>
#include <set>
#include <map>

using namespace std;

#define ll long long
#define pii pair<int,int>

int N,T;
int C,M;

int cnt[1005];
int serving[1005][1005];

ifstream fin("B.in");
ofstream fout("B.out");

int main() {
  fin >> T;
  for (int tt = 1; tt <= T; tt++) {
    cout << "Working on Case #" << tt << "\n";
    fin >> N >> C >> M;
    for (int i = 0; i < N; i++) {
      for (int j = 0; j < C; j++) serving[i][j] = 0;
    }
    for (int i = 0; i < C; i++) cnt[i] = 0;
    for (int i = 0; i < M; i++) {
      int a,b;
      fin >> a >> b;
      serving[a-1][b-1]++;
      cnt[b-1]++;
    }
    int rides = 0;
    for (int i = 0; i < C; i++) rides = max(rides,cnt[i]);
    int sum = 0;
    for (int i = 0; i < N; i++) {
      for (int j = 0; j < C; j++) sum += serving[i][j];
      rides = max(rides,(sum+i)/(i+1));
    }
    int ans = 0;
    for (int i = 0; i < N; i++) {
      int tot = 0;
      for (int j = 0; j < C; j++) tot += serving[i][j];
      if (tot > rides) ans += tot - rides;
    }
    fout << "Case #" << tt << ": " << rides << " " << ans << "\n";
  }
  return 0;
}