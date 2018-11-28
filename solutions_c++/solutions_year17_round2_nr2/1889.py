#include <iostream>
#include <cmath>
#include <ctime>
#include <cstdlib>
#include <cstring>
#include <cstdio>
#include <vector>
#include <cmath>
#include <algorithm>
#include <map>
#include <queue>
#include <set>
#include <limits>
#include <sstream>
#include <fstream>

using namespace std;
#define ll long long
#define x first
#define y second
#define pii pair<int, int>
#define pdd pair<double, double>
#define L(s) (int)(s).size()
#define vi vector<int>
#define all(s) (s).begin(), (s).end()
#define pb push_back
#define mp make_pair
#define inf 1000000000
#define pi 3.14159265358979323426264

#define sqr(x) ((x) * (x))
#define REP(i, n) for (int (i) = 0; (i) < (n); (i)++)
#define REPD(i, n) for (int (i) = (n) - 1; (i) >= 0; (i)--)
#define FOR(i, a, b) for (int (i) = (a); (i) < (b); (i)++)
#define FORD(i,a, b) for (int (i) = (a); (i) >= (b); (i)--)
#define FORI(it, cont) for (auto (it) = (cont).begin(); (it) != (cont).end(); (it)++)
#define eps std::numeric_limits<double>::epsilon()

bool possible(int n,int r,int ry,int y,int yb,int b,int rb)
{
   if (r > y + b + yb || y > r + b + rb || b > r + y + ry)
   {
      return false;
   }
   if (y < rb || b < ry || r < yb)
   {
      return false;
   }
   if ((y == rb && y + rb < n && y > 0) || (b == ry && b + ry < n && b > 0) || (r == yb && r + yb < n && r > 0))
   {
      return false;
   }
   return true;
}

string getRB(int& y,int& rbs)
{
   string rb;
   if (rbs > 0)
   {
      if (y > rbs) {rb.pb('Y'); y--;}
      while (rbs)
      {
         rb.pb('V');
         rb.pb('Y');
         rbs--;
         y--;
      }
   }
   return rb;
}

string getYB(int& r,int& ybs)
{
   string yb;
   if (ybs > 0)
   {
      if (r > ybs) {yb.pb('R'); r--;}
      while (ybs)
      {
         yb.pb('G');
         yb.pb('R');
         ybs--;
         r--;
      }
   }
   return yb;
}

string getRY(int& b,int& rys)
{
   string ry;
   if (rys > 0)
   {
      if (b > rys) {ry.pb('B'); b--;}
      while (rys)
      {
         ry.pb('O');
         ry.pb('B');
         rys--;
         b--;
      }
   }
   return ry;
}

string getSTR(int n,int r,int ry,int y,int yb,int b,int rb)
{
   string res;
   bool mod = false;

   /****************** MORE YYYYYYYYYYYY **************/
   if (y - rb >= r - yb && y - rb >= b - ry)
   {
      res = getRB(y, rb);
      mod = b > r;
       
      int last = 0; // 0 == y; 1 == r; 2== b;
      
      if (res.empty())
      {
         last = mod ? 1 : 2; 
      }
      while (r + y + b)
      {
          
         if (yb && last == 0)
         {
            res += getYB(r, yb);
            last = 1;
            continue;
         }
         if (ry && last == 0)
         {
            res += getRY(b, ry);
            last = 2;
            continue;
         }
         if (b && last == 0 && mod)
         {
            res += 'B';
            b--;
            last = 2;
            mod = b > r;
            continue;
         }
         if (r && last == 0 && !mod)
         {
            res += 'R';
            r--;
            last = 1;
            mod = b > r;
            continue;
         }
         if (y && last != 0)
         {
            res += 'Y';
            y--;
            last = 0;
            mod = b > r;
            continue;
         }
         if (r && last == 2)
         {
            res += 'R';
            r--;
            last = 1;
            continue;
         }
         if (b && last == 1)
         {
            res += 'B';
            b--;
            last = 2;
            continue;
         }
      }
   }
   else   if (y - rb <= r - yb && r - yb >= b - ry)
   {
      /****************** MORE RRRRRRRRRRRRRRRRRRRRRR **************/
      res = getYB(r, yb);
      mod = b > y;
      int last = 0; // 0 = r; 1 = y; 2 = b;

      if (res.empty())
      {
         last = mod ? 1 : 2; 
      }
      while (r + y + b)
      {
          
         if (rb && last == 0)
         {
            res += getRB(y, rb);
            last = 1;
            continue;
         }
         if (ry && last == 0)
         {
            res += getRY(b, ry);
            last = 2;
            continue;
         }
         if (b && last == 0 && mod)
         {
            res += 'B';
            b--;
            last = 2;
            mod = b > y;
            continue;
         }
         if (y && last == 0 && !mod)
         {
            res += 'Y';
            y--;
            last = 1;
            mod = b > y;
            continue;
         }
         if (r && last != 0)
         {
            res += 'R';
            r--;
            last = 0;

            mod = b > y;
            continue;
         }
         if (y && last == 2)
         {
            res += 'Y';
            y--;
            last = 1;
            continue;
         }
         if (b && last == 1)
         {
            res += 'B';
            b--;
            last = 2;
            continue;
         }
      }
   }
   else
   {
      /****************** MORE BBBBBBBBBBBBBBBBBBB **************/
      res = getRY(b, ry);
      int last = 0; // 0 = b; 1 = y; 2 = r;
      mod = y < r;
      if (res.empty())
      {
         last = mod ? 1 : 2; 
      }
      while (r + y + b)
      {
          
         if (rb && last == 0)
         {
            res += getRB(y, rb);
            last = 1;
            continue;
         }
         if (yb && last == 0)
         {
            res += getYB(r, yb);
            last = 2;
            continue;
         }
         if (r && last == 0 && mod)
         {
            res += 'R';
            r--;
            last = 2;
            mod = y < r;
            continue;
         }
         if (y && last == 0 && !mod)
         {
            res += 'Y';
            y--;
            last = 1;
            mod = y < r;
            continue;
         }
         if (b && last != 0)
         {
            res += 'B';
            b--;
            last = 0;
            mod = y < r;
            continue;
         }
         if (y && last == 2)
         {
            res += 'Y';
            y--;
            last = 1;
            continue;
         }
         if (r && last == 1)
         {
            res += 'R';
            r--;
            last = 2;
            continue;
         }
      }
   }
   return res;

}

int main()
{
   freopen("A.in", "r", stdin);
   freopen("B_out.txt", "w", stdout);
   int t;
   int n,r,ry,y,yb,b,rb;
   cin >> t;
   string res;
   REP(test, t)
   {
      res.clear();
      cin >> n >> r >> ry >> y >> yb>> b >> rb;
      if (!possible(n,r,ry,y,yb,b,rb))
      {
         cout << "Case #" << test + 1 << ": IMPOSSIBLE" << endl;
      }
      else
      {
         res = getSTR(n,r,ry,y,yb,b,rb);
         cout << "Case #" << test + 1 << ": " << res << endl;
      }
   }

   return 0;
}

