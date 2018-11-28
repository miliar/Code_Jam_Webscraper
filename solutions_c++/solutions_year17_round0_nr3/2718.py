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

////a
//void main()
//{
//  //ifstream is("GoogleCodeJam/A-small-attempt0.in");
//  ifstream is("GoogleCodeJam/A-large.in");
//  //ifstream is("GoogleCodeJam/input.txt");
//  ofstream os("GoogleCodeJam/output.txt");
//
//  int t;
//  is>>t;
//
//  for (int ti=0;ti<t;++ti)
//  {
//    //solve
//    string ss;
//    is>>ss;
//    vector<bool> s;
//    FOR (i,0,ss.size())
//    {
//      char c=ss[i];;
//      //is>>c;
//      if (c=='+'||c=='-')
//        s.push_back(c=='+');
//      else
//        break;
//    }
//    //int k = atoi(ss.c_str()+i);
//    IN_INT(k);
//    int res=0;
//    FOR (i,0,s.size())
//    {
//      if (!s[i])
//      {
//        if (i+k<=s.size())
//        {
//          ++res;
//          FOR (j,i,i+k)
//            s[j]=!s[j];
//        }
//        else
//        {
//          res=-1;
//          break;
//        }
//      }
//    }
//
//    //out
//    os << "Case #"<<ti+1<<": ";
//    if (res>=0)
//      os << res;
//    else
//      os<<"IMPOSSIBLE";
//    os<<"\n";
//  }
//}

//////////////////////////////////////////////////////////////////////////

////b
//void main()
//{
//  //ifstream is("GoogleCodeJam/B-small-attempt2.in");
//  ifstream is("GoogleCodeJam/B-large.in");
//  //ifstream is("GoogleCodeJam/input.txt");
//  ofstream os("GoogleCodeJam/output.txt");
//
//  int t;
//  is>>t;
//
//  for (int ti=0;ti<t;++ti)
//  {
//    //solve
//    string s;
//    is>>s;
//
//    //int res2;
//    //{
//    //  int n = atoi(s.c_str());
//    //  FOR_REV (r,0,n+1)
//    //  {
//    //    int i=r;
//    //    bool ok=true;
//    //    int prev=10;
//    //    while (i)
//    //    {
//    //      int j=i%10;
//    //      if (j>prev)
//    //      {
//    //        ok=false;
//    //        break;
//    //      }
//    //      prev=j;
//    //      i/=10;
//    //    }
//
//    //    if (ok)
//    //    {
//    //      res2=r;
//    //      break;
//    //    }
//    //  }
//    //}
//
//    FOR(i,0,s.size())
//    {
//      bool ok =true;
//      FOR (j,i+1,s.size())
//        if (s[j]!=s[i])
//        {
//          if (s[j]<s[i])
//            ok=false;
//          break;
//        }
//      if (!ok)
//      {
//        --s[i];
//        FOR (j,i+1,s.size())
//          s[j]='9';
//        break;
//      }
//    }
//
//    //int res1=atoi(s.c_str());
//    //assert(res1==res2);
//
//    os << "Case #"<<ti+1<<": ";
//    bool done=false;
//    FOR(i,0,s.size())
//    {
//      if (s[i]!='0'||done)
//      {
//        done=true;
//        os<<s[i];
//      }
//    }
//    os<<"\n";
//  }
//}
//

//////////////////////////////////////////////////////////////////////////

struct Intervals
{
  ll len_max; 
  vector<ll> num; //num[0] - with len_max
  ll sum_num;

  Intervals()
  {
    sum_num = 0;
  }
  Intervals(ll n)
  {
    len_max=n;
    num.push_back(1);
    sum_num = 1;
  }
};

void split_all(Intervals& ints)
{
  Intervals res;
  res.len_max = ints.len_max/2;
  res.sum_num=0;
  FOR (i, 0, ints.num.size())
  {
    ll num = ints.num[i];
    ll l = ints.len_max-i;
    if (l>1)
    {
      int l1 = res.len_max-l/2;
      res.num.resize(l1+1,0);
      res.num[l1]+=num;
      res.sum_num+=num;
    }
    if (l>2)
    {
      int l1 = res.len_max-(l-1)/2;
      res.num.resize(l1+1,0);
      res.num[l1]+=num;
      res.sum_num+=num;
    }
  }
  ints=res;
}

pair<ll,ll> findk(Intervals& ints, ll k)
{
  pair<ll,ll> res(0,0);

  FOR (i, 0, ints.num.size())
  {
    ll num = ints.num[i];
    ll l = ints.len_max-i;
    if (num>=k)
    {
      res.first = l/2;
      res.second = (l-1)/2;
      break;
    }
    else
      k-=num;
  }
  return res;
}

void main()
{
  //ifstream is("GoogleCodeJam/C-small-2-attempt0.in");
  ifstream is("GoogleCodeJam/C-large.in");
  //ifstream is("GoogleCodeJam/input.txt");
  ofstream os("GoogleCodeJam/output.txt");

  int t;
  is>>t;

  for (int ti=0;ti<t;++ti)
  {
    ll n,k;
    is>>n>>k;

    Intervals ints (n);
    while (ints.sum_num<k)
    {
      k-=ints.sum_num;
      split_all(ints);
    }
    pair<ll,ll> res = findk(ints,k);
    //out
    os << "Case #"<<ti+1<<": ";
    os << res.first <<" "<<res.second;
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
//    //out
//    os << "Case #"<<ti+1<<": ";
//    os << "\n";
//  }
//}


