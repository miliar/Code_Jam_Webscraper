#include <iostream>
#include <iterator>
#include <vector>
#include <set>
#include <algorithm>
#include <numeric>
#include <string>
#include <iomanip>

using namespace std;
typedef vector<int> IntV;

template<typename InputIt, typename Size, typename OutputIt>
OutputIt my_copy_n(InputIt &first /*dirty hack reference - we're adjusting input iterator*/, Size count, OutputIt result)
{
   while (count-- > 0)
   {
      *result++ = *first++;
   }
   return result;
}

template<typename AllLsType>
struct Printer
{
   size_t current;
   const AllLsType &allLs;

   explicit Printer(const AllLsType &i_allLs)
      : current(0U),
        allLs(i_allLs)
   {

   }

   void operator()(const int& i)
   {
      cout << (current ? "\n" : "") << allLs[i - 1];
      ++current;
   }
};

template<typename AllLsType>
Printer<AllLsType> make_printer(const AllLsType& l)
{
   return Printer<AllLsType>(l);
}

template<typename T, size_t N>
vector<T> assignArray(T (&a)[N])
{
   return vector<T>(&a[0], &a[0]+sizeof(a)/sizeof(a[0]));
}

int main(int, char*[])
{   
   ios_base::sync_with_stdio(false);
   cin.tie(NULL);
   
   // B
   /*string x;
   cin >> x;

   string y;
   cin >> y;

   string z(y);

   for (int i = 0; i < x.size(); ++i)
   {
	   if (x[i] < y[i])
	   {
		   cout << -1;
		   return 0;
	   }
   }

   cout << z; */

   // A
   /*string s;
   cin >> s;

   int vkCnt = 0;
   int vvCnt = 0;

   for (int i = 0; (i + 1) < s.size(); ++i)
   {
	   if ((s[i] == 'V') && (s[i + 1] == 'K'))
	   {
		   s[i] = s[i + 1] = 'X';

		   ++vkCnt;
		   ++i;
	   }
   }

   for (int i = 0; (i + 1) < s.size(); ++i)
   {
	   if (((s[i] == 'V') && (s[i + 1] == 'V'))
		   || ((s[i] == 'K') && (s[i + 1] == 'K')))
	   {
		   ++vvCnt;
		   break;
	   }
   }

   cout << (vkCnt + (vvCnt ? 1 : 0));
   */

   int T = 0;

   cin >> T;

   const int c_T = T;

   while (--T >= 0)
   {
      double D = 0.0;
      int N = 0;
      
      cin >> D;
      cin >> N;

      double K, S;

      double y = numeric_limits<double>::max();

      while (--N >= 0)
      {
         cin >> K >> S;

         y = min(y, D * S / ((D - K) ? D - K : 1.0));
      }

      cout << "Case #" << c_T - T << ": " << std::fixed << std::setprecision(8) << y << (T ? "\n" : "");
   }

   return 0;
}