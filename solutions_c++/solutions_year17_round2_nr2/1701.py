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

void print_stalls(vector<char> & conv, vector<size_t> & stalls)
{
   for (size_t i = 0; i < stalls.size(); ++i)
   {
      //cerr << conv[stalls[i]];
   }
   //cerr << endl;
}

void second_problem()
{
   ull t;
   cin >> t;
   for (size_t cnt = 0; cnt < t; ++cnt)
   {
      ull n, r, o, y, g, b, v;
      cin >> n >> r >> o >> y >> g >> b >> v;
      if (r < g or b < o or y < v)
      {
         //cerr << "here-1" << endl;
         output("IMPOSSIBLE");
         continue;
      }
      vull color(6);
      vector<char> conv(6);
      color[0] = r; conv[0] = 'R';
      color[1] = y; conv[1] = 'Y';
      color[2] = b; conv[2] = 'B';
      color[3] = g; conv[3] = 'G';
      color[4] = v; conv[4] = 'V';
      color[5] = o; conv[5] = 'O';
      
      vector<size_t> a(n, 6);
      bool skip = false;
      if (r == 0 and y == 0 and b == 0)
      {
         //cerr << "here0" << endl;
         output("IMPOSSIBLE");
         continue;
      }
      size_t first = 0;
      for (; color[first] == 0; ++first);
      a[0] = first;
      color[first]--;
      for (size_t i = 1; i < n - 1; ++i)
      {
         //cerr << "loop " << i << endl;
         //print_stalls(conv, a);
         size_t prev = a[i-1];
         if (prev < 3)
         {
            if (color[prev + 3] > 0)
            {
               a[i] = prev + 3;
               color[prev + 3]--;
               continue;
            }
            else {
               switch (prev)
               {
                  case 0:
                     if (color[1] > color[2])
                     {
                        a[i] = 1;
                        color[1]--;
                     }
                     else if (color[2] > 0)
                     {
                        a[i] = 2;
                        color[2]--;
                     }
                     else
                     {
                        //print_stalls(conv, a);
                        //cerr << "here1 + " << i << endl;
                        output("IMPOSSIBLE");
                        skip = true;
                     }
                     break;
                  case 1:
                     if (color[0] > color[2])
                     {
                        a[i] = 0;
                        color[0]--;
                     }
                     else if (color[2] > 0)
                     {
                        a[i] = 2;
                        color[2]--;
                     }
                     else
                     {
                        //print_stalls(conv, a);
                        //cerr << "here2 + " << i << endl;
                        //cerr << color[0] << ", " << color[1] << ", " << color[2] << endl;
                        output("IMPOSSIBLE");
                        skip = true;
                     }
                     break;
                  case 2:
                     if (color[1] > color[0])
                     {
                        a[i] = 1;
                        color[1]--;
                     }
                     else if (color[0] > 0)
                     {
                        a[i] = 0;
                        color[0]--;
                     }
                     else
                     {
                        //print_stalls(conv, a);
                        //cerr << "here3 + " << i << endl;
                        output("IMPOSSIBLE");
                        skip = true;
                     }
                     break;
               }
            }
         }
         if (skip)
         {
            break;
         }
         if (prev > 2)
         {
            if (color[prev - 3] > 0)
            {
               a[i] = prev - 3;
               color[prev - 3]--;
               continue;
            }
            else {
               //print_stalls(conv, a);
               //cerr << "here4 + " << i << endl;
               output("IMPOSSIBLE");
               skip = true;
               break;
            }
         }
      }



      size_t last = 0;
      for (; color[last] == 0; ++last);
      a[n-1] = last;
      if (not skip)
      {
         if (a[0] == last or a[n - 2] == last)
         {
            ////print_stalls(conv, a);
            ////cerr << "here5" << endl;
            output("IMPOSSIBLE");
            skip = true;
         } else if (last > 2 and (a[0] != last - 3 or a[n - 2] != last - 3))
         {
            ////print_stalls(conv, a);
            ////cerr << "here6" << endl;
            output("IMPOSSIBLE");
            skip = true;
         }
         else if (last < 3 and
                 (
                         (a[0] > 2 and a[0] != last + 3)
                  or
                         (a[n - 2] > 2 and a[n - 2] != last + 3)
                 )
                 )
         {
            ////print_stalls(conv, a);
            ////cerr << "here7" << endl;
            output("IMPOSSIBLE");
            skip = true;
         }
      }



      if (not skip)
      {
         cout << "Case #" << case_count++ << ": ";
         for (size_t i = 0; i < n; ++i)
         {
            cout << conv[a[i]];
         }
         cout << endl;
      }
   }
}

int main()
{
   std::ios::sync_with_stdio(false);
   cin.tie(0);
   second_problem();
   return 0;
}