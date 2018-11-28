#include <iostream>
#include <vector>
#include <unordered_map>
#include <sstream>
#include <utility>
#include <algorithm>

using namespace std;

pair<int, int> findOccupiedStall(vector<char>& rowOfStalls, int pos) {
   pair<int, int> p = make_pair(0, 0);
   // lhs
   for (int i = pos - 1; i >= 0; --i)
   {
      if (rowOfStalls[i] == 'O') {
         p.first = pos - i - 1;
         //cout << "left: " << p.first << endl;
         break;
      }
   }
   // rhs
   for (int i = pos + 1; i < rowOfStalls.size(); ++i)
   {
      if (rowOfStalls[i] == 'O') {
         p.second = i - pos - 1;
         //cout << "right: " << p.first << endl;
         break;
      }
   }

   return p;
}

int main() {
   int T, N, K, c=1;
   string line;
   cin >> T;
   cin.ignore();

   while(getline(cin, line)) {
      stringstream ss(line);

      ss >> N >> K;

      // initialize stall state
      vector<char> rowOfStalls(N+2, '.');
      vector<pair<int, int>> dist(N+2, make_pair(0, 0));
      vector<int> minDist(N+2, 0);
      vector<int> maxDist(N+2, 0);

      rowOfStalls[0] = 'O';
      rowOfStalls[N+1] = 'O';

      cout << "Case #" << c << ": ";


      pair<int, int> result = make_pair(0, 0);


      // number of occupants
      for (int j = 0; j < K; j++) {

         int minMax = -1;
         int minMaxIndex = -1;
      
         bool useMaxMax = false;

         int maxMaxIndex = -1;
         int maxMax = -1;

         vector<int> maxPos;

         // first pass to calculate distances
         for (int i = 1; i < (N+1); ++i) {
            // if empty
            if (rowOfStalls[i] == '.') {
               dist[i] = findOccupiedStall(rowOfStalls, i);

               //cout << "<" << dist[i].first << ", " << dist[i].second << ">" << endl;
               minDist[i] = min(dist[i].first, dist[i].second);
               maxDist[i] = max(dist[i].first, dist[i].second);
               //cout << "min: "<< minDist[i] << endl;
               //cout << "max: "<< maxDist[i] << "\n" << endl;

               if (minMax < minDist[i]) {
                  minMax = minDist[i];
                  minMaxIndex = i;
                  useMaxMax = false;
                  result.second = minMax;
                  maxPos.clear();
                  maxPos.push_back(i);

               } else if (minMax == minDist[i]) {
                  useMaxMax = true;
                  maxPos.push_back(i);
               }           
            }
         }

         for (auto i : maxPos) {
            //cout << "positions " << i << endl;
            if (maxMax < maxDist[i]) {
               maxMax = maxDist[i];
               maxMaxIndex = i;
               result.first = maxMax;
            } 
         }

         // to use max max?
         if (!useMaxMax) {
            //cout << "using stall " << minMaxIndex << endl;
            rowOfStalls[minMaxIndex] = 'O';
         } else {
            //cout << "using stall " << maxMaxIndex << endl;
            rowOfStalls[maxMaxIndex] = 'O';
         }
      }

      cout << result.first << " " << result.second << endl;

      c++;
   }

   return 0;
}