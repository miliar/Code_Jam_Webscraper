#include <iostream>
#include <utility>
#include <cstdint>
#include <algorithm>
#include <map>
#include <iterator>
#include <iomanip>
typedef std::pair<int, char> ic;

int n;
int cnt[6];
std::string color;
char ANS[1024];

bool solve()
{
   ic counts[6];
   for (int i=0; i<6; i++)
   {
       counts[i] = ic(cnt[i], color[i]);
   }
   std::sort(counts, counts+6, std::greater<ic>());
   
   for (int i=0; i<6; i++)
   {
       cnt[i] = counts[i].first;
       color[i] = counts[i].second;
   }
   int maxn = n / 2;
   if (cnt[0] > maxn) return false;
   int spaces = cnt[0];
   if (cnt[1]-cnt[2] > spaces) return false;
   
   int c0 = cnt[0];
   int edge = 2 * (c0 - 1);
   for (int i=0; i<=edge; i++)
   {
       if (i%2 == 0 && cnt[0] > 0)
       {
           ANS[i] = color[0];
           cnt[0]--;
       }
       else
       {
           if (cnt[1] > cnt[2])
           {
               cnt[1]--;
               ANS[i] = color[1];
           }
           else
           {
               cnt[2]--;
               ANS[i] = color[2];
           }
       }
   }
   int parity = cnt[1] > cnt[2] ? 0 : 1;
   for (int i=edge+1; i<n; i++)
   {
       ANS[i] = color[1 + parity];
       parity ^= 1;
   }
   
   ANS[n] = 0;
   return true;
}

int main()
{
    int t;
    std::cin >> t;
    for (int i=1; i<=t; i++)
    {
        std::cin >> n;
        color = "ROYGBV";
        for (int j=0; j<6; j++)
        {
            std::cin >> cnt[j];
        }
        std::cout << "Case #" << i << ": ";
        if (solve())
        {
            ANS[n] = 0;
            std::cout << ANS;
        }
        else
        {
            std::cout << "IMPOSSIBLE";
        }
        std::cout << "\n";
        
    }
}
