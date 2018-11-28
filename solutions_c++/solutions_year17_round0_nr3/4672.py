#include <vector>
#include <string>
#include <iostream>
#include <algorithm>
#include <map>

using namespace std;

typedef unsigned long long mlong;
typedef pair<mlong, mlong> mpair;

bool pred( mpair &m1, mpair &m2 )
{
   if (m1.first < m2.first)
      return true;

   return false;
}

void cinsert( vector<mpair> &v, mlong val )
{
   for (int i = 0; i != v.size(); i++)
   {
      if (v[i].first == val)
      {
         v[i].second++;
         return;
      }
   }

   v.push_back(mpair(val, 1));
   sort(v.begin(), v.end(), pred);
}

void cpop( vector<mpair> &v, mlong &val )
{
   mpair t = v.back();

   v.back().second--;
   val = t.first;

   if (v.back().second == 0)
      v.pop_back();
}

void solve( mlong n, mlong k, mpair &ans )
{
   mlong t = n, t1, t2;
   std::vector<mpair> tt;

   if (t == 1)
   {
      t1 = 0;
      t2 = 0;
   }
   else
   {
      if (t % 2 == 0)
      {
         t1 = t / 2 - 1;
         t2 = t / 2;
      }
      else
      {
         t1 = t / 2;
         t2 = t / 2;
      }
   }

   ans.first = t2;
   ans.second = t1;

   cinsert(tt, t1);
   cinsert(tt, t2);

   k--;

   while (k > 0)
   {
      mlong c = 0;

      cpop(tt, c);

      if (c == 1)
      {
         t1 = 0;
         t2 = 0;
      }
      else
      {
         if (c % 2 == 0)
         {
            t1 = c / 2 - 1;
            t2 = c / 2;
         }
         else
         {
            t1 = c / 2;
            t2 = c / 2;
         }
      }

      ans.first = t2;
      ans.second = t1;

      cinsert(tt, t1);
      cinsert(tt, t2);

      k--;
   }

 
  
   
}

int main( int argc, char *argv[] )
{  
   int t = 0;
   vector<mlong> n;
   vector<mlong> k;   
   
   mpair ans;

   solve(1000, 1000, ans);
   solve(999999, 999998, ans);

   cin >> t;

   n.resize(t);
   k.resize(t);

   for (int i = 0; i < t; i++)
   {
      cin >> n[i];
      cin >> k[i];
   }

   for (int i = 0; i < t; i++)
   {
      mpair ans;

      solve(n[i], k[i], ans);
      cout << "Case #" << i + 1 << ": " << ans.first << " " << ans.second << endl;
   }

   return 0;
}