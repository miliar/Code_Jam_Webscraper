#include <iostream>
#include <fstream>
#include <vector>
#include <list>
#include <map>
#include <cassert>
#include <stack>
#include <string>
#include <cstdio>
#include <climits>
#include <algorithm>
#include <set>
#include <cmath>

using namespace std;

#define REP(i, a, b) for (int i = a; i < b; i++)
#define REPE(i, a, b) for (int i = a; i <= b; i++)
#define REPD(i, a, b) for (int i = a; i >= b; i--)
#define ll long long
#define vl vector<long long>
#define vll vector<vector<long long>>
#define vi vector<int>
#define vii vector<vector<int>>

#define DEBUG 0

#if DEBUG == 0
#define cout outfile
#define cerr outfile
#endif
// void flip(string &s,int eloc,int k)

int main(void)
{
   std::ios_base::sync_with_stdio(false);
   cin.tie(NULL);
   ifstream infile("infile");
   ofstream outfile("outfile.txt");
   long long testcases = 1;
   infile >> testcases;
   // cout<<111111111111111120-10<<endl;
   REPE(testcase, 1, testcases)
   {

      string s;
      ll n;
      infile >> n;
      s = to_string(n);
      int slen = s.length();
		bool f = is_sorted(s.begin(),s.end());
      if (n < 10 || f)
      {
	 cout << "Case #" << testcase << ": " << n << endl;
      }
      else
      {

#if DEBUG == 10 || DEBUG == 1
	 cout << "*********TESTCASE" << testcase << "**********" << endl;
	 cout << "s  \t" << s << endl;
#endif

	 int i = distance(s.begin(), is_sorted_until(s.begin(), s.end())) - 1, k = i - 1;
	 bool flag = false;
	 while (k > 0 && s[k] == s[i])
	 {
	    k--;
	    flag = true;
	 }
	 if (i == 1 && s[1] == s[0])
	 {
	    flag = true;
	    k = 0;
	 };

	 string temp = "";
	 int e = (!flag) ? i : (k >= 0) ? k : 0;
	 REPE(q, 0, e)
	 temp += s[q];
//  cout<<i<<" "<<k<<" "<<e<<" flag "<<flag<<endl;

#if DEBUG == 1
	 cout << "i " << i << "\t k " << k << endl;
#endif

	 // cerr<<temp<<endl;
	 ll t = stoll(temp) - (ll)1;
	 temp = to_string(t);
	 ll j = temp.length() - 1;

#if DEBUG == 1
	 cout << "temp " << temp << endl;
#endif
	 i = e;
	 while (j >= 0)
	 {
	    s[i] = temp[j];
	    j--;
	    i--;
	    //  e--;
	 };
#if DEBUG == 1
	 cout << s << endl;
#endif
	 while (i >= 0)
	 {
	    s[i] = '0';
	    i--;
	 };
	 REP(q, e + 1, slen)
	 s[q] = '9';

	 cout << "Case #" << testcase << ": " << stoll(s) << endl;
      };
   };

   // #if DEBUG == 1
   // #endif
   return 0;
};