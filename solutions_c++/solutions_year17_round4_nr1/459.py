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
#include <iomanip>

using namespace std;
typedef long long     ll;
typedef unsigned int  UInt;
#define ALL(a)             (a).begin(), (a).end()
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
template<class T> int        get_bit(T v, int bit_index) { return (v >> bit_index) & 1; } //return {0,1}

//////////////////////////////////////////////////////////////////////////

//a - solve large !!!!!!!!!
void main()
{
  //ifstream is("GoogleCodeJam/A-small-attempt1.in");
  ifstream is("GoogleCodeJam/A-large.in");
  //ifstream is("GoogleCodeJam/input.txt");
  ofstream os("GoogleCodeJam/output.txt");
  os << setprecision(15);

  IN_INT (tests_num);
  for (int ti=0;ti<tests_num;++ti)
  {
    //solve
    IN_INT2 (n,p);
    vector<int> a(n);
    map<int,int> m;
    FOR (i,0,n)
    {
      is>>a[i];
      a[i]=a[i]%p;
      m[a[i]]++;
    }

    int res=m[0];
    FOR (i,1,p)
    {
      if (i+i==p)
      {
        res+=m[i]/2;
        m[i]%=2;
      }
      else
      {
        int j = p-i;
        int mm=min(m[i],m[j]);
        res+=mm;
        m[i]-=mm;
        m[j]-=mm;
      }
    }

    int l=0;
    FOR (i,2,3)
    {
      while (m[i])
      {
        if (!l)
          ++res;
        l+=i;
        l%=p;
        --m[i];
      }
    }

    FOR_REV (i,1,p)
    {
      while (m[i])
      {
        if (!l)
          ++res;
        l+=i;
        l%=p;
        --m[i];
      }
    }

    //out
    os << "Case #"<<ti+1<<": ";
    os << res;
    os << "\n";
  }
}

//////////////////////////////////////////////////////////////////////////

////
//void main()
//{
//  //ifstream is("GoogleCodeJam/B-small-attempt0.in");
//  ifstream is("GoogleCodeJam/B-large.in");
//  //ifstream is("GoogleCodeJam/input.txt");
//  ofstream os("GoogleCodeJam/output.txt");
//  os << setprecision(15);
//
//  IN_INT (tests_num);
//  for (int ti=0;ti<tests_num;++ti)
//  {
//    //solve
//    IN_INT3 (n,c,m);
//    map<int,map<int,int>> ptob; //place-> customer -> num_in_place
//    vector<int> a(n);
//    map<int,int> cust_to_tick;
//    map<int,int> pton;
//    FOR (i,0,m)
//    {
//      IN_INT2(p,b);
//      ptob[p][b]++;
//      cust_to_tick[b]++;
//      pton[p]++;
//      //is>>a[i];
//    }
//
//    int runs0=0;
//    FOR_EACH (it,cust_to_tick)
//      runs0=max(runs0,it->second);
//
//    FOR (runs,runs0,m+1)
//    {
//      bool ok =true;
//      int prom=0;
//      int places_free=0;
//      FOR (pos,1,n+1)
//      {
//        //int pos = it->first;
//        int num = pton[pos];
//
//        if (runs+places_free<num)
//        {
//          ok=false;
//          break;
//        }
//
//        prom+=max(0,num-runs);
//        places_free-=num-runs;
//      }
//
//      //out
//      if (ok)
//      {
//        os << "Case #"<<ti+1<<": ";
//        os << runs<<" "<<prom;
//        os << "\n";
//        break;
//      }
//
//    }
//  }
//}



//////////////////////////////////////////////////////////////////////////

//void main()
//{
//  //ifstream is("GoogleCodeJam/A-small-attempt0.in");
//  //ifstream is("GoogleCodeJam/A-large.in");
//  ifstream is("GoogleCodeJam/input.txt");
//  ofstream os("GoogleCodeJam/output.txt");
//  os << setprecision(15);
//
//  IN_INT (tests_num);
//  for (int ti=0;ti<tests_num;++ti)
//  {
//    //solve
//    IN_INT2 (n,p);
//    vector<int> a(n);
//    FOR (i,0,n)
//      is>>a[i];
//
//    //out
//    os << "Case #"<<ti+1<<": ";
//    //os << res;
//    os << "\n";
//  }
//}


