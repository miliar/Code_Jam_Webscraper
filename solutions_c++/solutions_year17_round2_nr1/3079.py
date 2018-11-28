
#include <algorithm>
#include <vector>
#include <string>
#include <iostream>
#include <fstream>

using namespace std;

struct chunk {
   int D, N;

   vector<pair<int, int>> Ks;
};

long double solve( const chunk &ch )
{
   long double res = 24.5f;

   vector<long double> t;

   t.resize(ch.N);

   for (int i = 0; i < ch.N; i++)
   {
      t[i] = (ch.D - ch.Ks[i].first) * 1.0f / ch.Ks[i].second;
   }

   vector<long double>::iterator tmin = std::max_element(t.begin(), t.end());

   long double tmin_ = *tmin;

   return ch.D / tmin_;
}



int main( int argc, char *argv[] )
{
   int t = 0;

   vector<chunk> chunks;

   ifstream cin("test.in");
   
   cin >> t;

   chunks.resize(t);

   for (int i = 0; i < t; i++)
   {
      cin >> chunks[i].D;
      cin >> chunks[i].N;

      chunks[i].Ks.resize(chunks[i].N);

      for (int j = 0; j < chunks[i].N; j++)
      {
         cin >> chunks[i].Ks[j].first;
         cin >> chunks[i].Ks[j].second;
      }
   }

   for (int i = 0; i < t; i++)
   {
      long double solution = solve(chunks[i]);

      printf("Case #%i: %lf\n", i + 1, solution);
   }


   return 0;
}