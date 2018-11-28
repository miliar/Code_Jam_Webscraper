#include <assert.h>
#include <vector>
#include <list>
#include <map>
#include <math.h>
#include <set>
#include <string>
#include <sstream>
#include <iostream>
#include <fstream>
#include <algorithm>

using namespace std;
typedef long long     ll;
typedef unsigned int  UInt;
#define ALL(a)             (a).begin(), (a).end()
//#define FOR(i,a,b)         for(int i = a;   i <  (int)(b); ++i)
//#define FOR_REV(i,a,b)     for(int i = b-1; i >= (int)(a); --i)
#define FOR(i,a,b)           for(int i = a,   end = (int)(b) ; i < end; ++i)
#define FOR_REV(i,a,b)       for(int i = b-1, rend = (int)(a); i >= rend; --i)
#define FOR_EACH(it,a)       for(remove_reference<decltype(a)>::type::iterator it = (a).begin(); it != (a).end(); ++it)
#define FOR_EACH_CONST(it,a) for(remove_reference<decltype(a)>::type::const_iterator it = (a).begin(); it != (a).end(); ++it)
#define FOR_EACH_REV(it,a)   for(remove_reference<decltype(a)>::type::reverse_iterator it = (a).rbegin(); it != (a).rend(); ++it)
#define IN_INT(a)            int a;       is >> a;
#define IN_INT2(a,b)         int a,b;     is >> a >> b;
#define IN_INT3(a,b,c)       int a,b,c;   is >> a >> b >> c;
#define IN_INT4(a,b,c,d)     int a,b,c,d; is >> a >> b >> c >> d;
template<class T> inline T   sqr(T v)  { return v * v; }
template<class T> inline int sign(T v) { return v == 0 ? 0 : (v > 0 ? 1 : -1); }
template<class T> int get_bit(T v, int bit_index) { return (v >> bit_index) & 1; } //return {0,1}

//////////////////////////////////////////////////////////////////////////

void main()
{
  //ifstream is("GoogleCodeJam/A-small-attempt0.in");
  ifstream is("GoogleCodeJam/A-large.in");
  //ifstream is("GoogleCodeJam/input.txt");
  ofstream os("GoogleCodeJam/output.txt");

  int t;
  is>>t;

  for (int ti=0;ti<t;++ti)
  {
    //solve
    string ss;
    is>>ss;
    vector<bool> s;
    FOR (i,0,ss.size())
    {
      char c=ss[i];;
      //is>>c;
      if (c=='+'||c=='-')
        s.push_back(c=='+');
      else
        break;
    }
    //int k = atoi(ss.c_str()+i);
    IN_INT(k);
    int res=0;
    FOR (i,0,s.size())
    {
      if (!s[i])
      {
        if (i+k<=s.size())
        {
          ++res;
          FOR (j,i,i+k)
            s[j]=!s[j];
        }
        else
        {
          res=-1;
          break;
        }
      }
    }

    //out
    os << "Case #"<<ti+1<<": ";
    if (res>=0)
      os << res;
    else
      os<<"IMPOSSIBLE";
    os<<"\n";
  }
}




//////////////////////////////////////////////////////////////////////////

//void main()
//{
//  //ifstream is("GoogleCodeJam/A-small-attempt0.in");
//  //ifstream is("GoogleCodeJam/A-large.in");
//  ifstream is("GoogleCodeJam/input.txt");
//  ofstream os("GoogleCodeJam/output.txt");
//
//  int t;
//  is>>t;
//
//  for (int ti=0;ti<t;++ti)
//  {
//    //solve
//
//    os << "Case #"<<ti+1<<": ";
//    //out
//    os<<"\n";
//  }
//}


