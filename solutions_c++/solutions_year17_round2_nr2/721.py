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

//a
//void main()
//{
//  //ifstream is("GoogleCodeJam/A-small-attempt0.in");
//  ifstream is("GoogleCodeJam/A-large.in");
//  //ifstream is("GoogleCodeJam/input.txt");
//  ofstream os("GoogleCodeJam/output.txt");
//  os << setprecision(15);
//
//  int t;
//  is>>t;
//
//  for (int ti=0;ti<t;++ti)
//  {
//    IN_INT2(d,n);
//    double t_max = 0;
//    FOR (i,0,n)
//    {
//      IN_INT2(k,s);
//      double l = d-k;
//      double t = l/s;
//      t_max=max(t,t_max);
//    }
//
//    double res = d/t_max;
//
//    //out
//    os << "Case #"<<ti+1<<": ";
//    os << res;
//    os << "\n";
//  }
//}

//////////////////////////////////////////////////////////////////////////
//static const double infinity_d = std::numeric_limits<double>::infinity();
//void main()
//{
//  //ifstream is("GoogleCodeJam/C-small-attempt0.in");
//  ifstream is("GoogleCodeJam/C-large.in");
//  //ifstream is("GoogleCodeJam/input.txt");
//  ofstream os("GoogleCodeJam/output.txt");
//  os << setprecision(15);
//
//  int t;
//  is>>t;
//
//  double d[100][100];
//
//  for (int ti=0;ti<t;++ti)
//  {
//    IN_INT2(n,q);
//    
//    vector<pair<int,int>> hs(n);
//    FOR (i,0,n)
//      is>>hs[i].first>>hs[i].second;
//
//    FOR (i,0,n)
//      FOR (j,0,n)
//        is>>d[i][j];
//
//    for (int k=0; k<n; ++k)
//      for (int i=0; i<n; ++i)
//        for (int j=0; j<n; ++j)
//          if (d[i][k]>=0&&d[k][j]>=0)
//            d[i][j] = d[i][j]>=0?min (d[i][j], d[i][k] + d[k][j]):d[i][k] + d[k][j];
//
//
//    //out
//    os << "Case #"<<ti+1<<": ";
//
//    FOR (i,0,q)
//    {
//      IN_INT2(s,f);
//      --s,--f;
//
//      vector<int> used(n,0);
//      vector<double> time(n,infinity_d);
//      multimap<double,int> front;
//      front.insert(make_pair(0,s));
//      //used[s]=1;
//      while (!used[f])
//      {
//        double t = front.begin()->first;
//        int i = front.begin()->second;
//        front.erase(front.begin());
//
//        if (!used[i])
//        {
//          time[i]=t;
//          used[i]=1;
//          FOR (j,0,n)
//            if (!used[j]&&d[i][j]>=0&&hs[i].first>=d[i][j])
//            {
//              double tj = t + d[i][j]/hs[i].second;
//              if (tj<time[j])
//              {
//                time[j]=tj;
//                front.insert(make_pair(tj,j));
//              }
//            }
//        }
//      }
//      os << time[f]<<" ";
//
//    }
//
//    os << "\n";
//  }
//}

//////////////////////////////////////////////////////////////////////////

void main()
{
  ifstream is("GoogleCodeJam/B-small-attempt1.in");
  //ifstream is("GoogleCodeJam/B-large.in");
  //ifstream is("GoogleCodeJam/input.txt");
  ofstream os("GoogleCodeJam/output.txt");
  os << setprecision(15);

  int t;
  is>>t;

  for (int ti=0;ti<t;++ti)
  {
    int n,R, O, Y, G, B, V;
    is>>n>> R>> O>> Y>> G>> B>> V;

    //red and yellow hairs appears orange.
    //yellow and blue hairs appears green.
    //red and blue hairs appears violet.

    bool ok =true;
    string res(n,'a');

    if (R&&R==G&&n>R+G)
      ok=false;
    if (Y&&Y==V&&n>Y+V)
      ok=false;
    if (B&&B==O&&n>B+O)
      ok=false;

    if (ok)
    FOR (i,0,n)
    {
      char prev = i>0?res[i-1]:0;
      char curr = 0;
      char sopr;
      int zero=0;
      int* cmax=&zero;
      int* soprn=&zero;
      if (R&&prev!='R'&&R-G>=*cmax-*soprn)
      {
        curr = 'R';
        cmax = &R;
        sopr = 'G';
        soprn = &G;
      }
      if (Y&&prev!='Y'&&(!curr||Y-V>*cmax-*soprn||(Y-V==*cmax-*soprn&&'Y'==res[0])))
      {
        curr = 'Y';
        cmax = &Y;
        sopr = 'V';
        soprn = &V;
      }
      if (B&&prev!='B'&&(!curr||B-O>*cmax-*soprn||(B-O==*cmax-*soprn&&'B'==res[0])))
      {
        curr = 'B';
        cmax = &B;
        sopr = 'O';
        soprn = &O;
      }

      if (!curr)
      {
        ok=false;
        break;
      }
      else
      {
        res[i]=curr;
        --*cmax;
        //*cmax-=*soprn;
        while (*soprn>0)
        {
          res[++i]=sopr;
          --*soprn;
          if (*cmax)
          {
            res[++i]=curr;
            --*cmax;
          }
          else if (*soprn)
          {
            ok=false;
            break;
          }
          else if (i!=n-1)
          {
            ok=false;
            break;
          }
        }
        if (!ok)
          break;
        //if (*cmax<0)
        //{
        //  ok=false;
        //  break;
        //}
      }
    }

    if (res[0]==res[n-1])
      ok=false;

    //out
    os << "Case #"<<ti+1<<": ";
    os << (ok?res:"IMPOSSIBLE");
    os << "\n";
  }
}

////test ans
//void main()
//{
//  ifstream is("GoogleCodeJam/B-small-attempt0.in");
//  //ifstream is("GoogleCodeJam/B-large.in");
//  //ifstream is("GoogleCodeJam/input.txt");
//  ifstream is1("GoogleCodeJam/output.txt");
//
//  int t;
//  is>>t;
//
//  for (int ti=0;ti<t;++ti)
//  {
//    int n,R, O, Y, G, B, V;
//    is>>n>> R>> O>> Y>> G>> B>> V;
//
//    string ans;
//    is1>>ans>>ans>>ans;
//
//    if (ans=="IMPOSSIBLE")
//    {
//      int m=max(R,max(Y,B));
//      int s2 = R+Y+B-m;
//      if (m<=s2)
//        cout<<"ERROR\n";
//
//      continue;
//    }
//
//    bool ok = true;
//    if (ans.size()!=n)
//      ok=false;
//    else
//    FOR (i,0,n)
//    {
//      int prev=ans[i==0?n-1:i-1];
//      int next=ans[(i+1)%n];
//      if (ans[i]==prev)
//        ok=false;
//      if (ans[i]==next)
//        ok=false;
//
//      if (ans[i]=='R')
//        --R;
//      if (ans[i]=='Y')
//        --Y;
//      if (ans[i]=='B')
//        --B;
//    }
//
//    if (R+ O+ Y+ G+ B+ V)
//      ok=false;
//
//    if (!ok)
//      cout<<"ERROR\n";
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
//  int t;
//  is>>t;
//
//  for (int ti=0;ti<t;++ti)
//  {
//    //solve
//
//    //out
//    os << "Case #"<<ti+1<<": ";
//    //os << res;
//    os << "\n";
//  }
//}


