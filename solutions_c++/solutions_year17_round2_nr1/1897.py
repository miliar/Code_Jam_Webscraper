#include <bits/stdc++.h>

using namespace std;

typedef unsigned long long ull;
typedef long long ll;
typedef size_t st;
typedef vector<ull> vull;
typedef vector<vull> vvull;
typedef vector<ll> vll;
typedef vector<vll> vvll;

size_t case_count = 1;

namespace patch
{
    template <typename T>
    string to_string(const T& n)
    {
       std::ostringstream stm ;
       stm << n ;
       return stm.str() ;
    }
}

void output(string str)
{
   cout << "Case #" << case_count << ": " << str << endl;
   ++case_count;
}

template <typename  T>
void output(T a)
{
   output(patch::to_string<T>(a));
}

void first_problem()
{
   ull t;
   cin >> t;
   for (size_t cnt = 0; cnt < t; ++cnt)
   {
      ull d, n;
      cin >> d;
      cin >> n;
      vector<double> k(n);
      vector<double> s(n);
      double best = numeric_limits<double>::max();
      for (size_t i = 0; i < n; ++i)
      {
         cin >> k[i] >> s[i];
         best = min(best, d*s[i]/ (d - k[i]));
      }
      cout.precision(17);
      cout << "Case #" << cnt+1 << ": " << fixed << best << endl;
   }
}

int main()
{
   std::ios::sync_with_stdio(false);
   cin.tie(0);
   first_problem();
   return 0;
}