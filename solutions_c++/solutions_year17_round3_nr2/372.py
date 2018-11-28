#include <bits/stdc++.h>

using namespace std;

int diff(int x, int y) {
   if(y >= x) return y - x;
   else return (1440 - x + y);
}

int main() {
   int T;
   cin >> T;
   for(int testcase = 1; testcase <= T; testcase++) {
      int C, J;
      cin >> C >> J;
      vector<pair<pair<int,int>,char>> tab(C + J);
      for(int i = 0; i < C; ++i) {
         int x, y;
         cin >> x >> y;
         tab[i] = {{x,y},'C'};
      }
      for(int i = C; i < C+J; ++i) {
         int x, y;
         cin >> x >> y;
         tab[i] = {{x,y},'J'};
      }
      sort(tab.begin(),tab.end());
      vector<pair<int,char>> interv;
      int timeC = 720, timeJ = 720;
      int score = 0;
      for(int i = 0; i < C+J; ++i) {
         int xA = tab[i].first.first,
             yA = tab[i].first.second;
         char pA = tab[i].second;
         int xB = tab[(i+1) % (C + J)].first.first,
             yB = tab[(i+1) % (C + J)].first.second;
         char pB = tab[(i+1) % (C + J)].second;
         if(pA == 'C') timeC -= yA - xA;
         else timeJ -= yA - xA;
         if(pA == pB) interv.push_back({diff(yA,xB),pA});
         else score++;
      }
      int N = interv.size();
      sort(interv.begin(),interv.end());
      for(int i = 0; i < N; ++i) {
         int x = interv[i].first;
         int p = interv[i].second;
         if(p == 'C') {
            if(x > timeC) {
               timeC = 0;
               timeJ -= x - timeC;
               score += 2;
            }
            else timeC -= x;
         }
         else {
            if(x > timeJ) {
               timeJ = 0;
               timeC -= x - timeJ;
               score += 2;
            }
            else timeJ -= x;
         }
      }
      cout << "Case #" << testcase << ": " << score << endl;
   }
}
