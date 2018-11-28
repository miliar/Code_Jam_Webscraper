#include <fstream>
#include <vector>
#include <iostream>
#include <iomanip>
#define dist first.first
#define e first.second
#define s second
#define ld long double
using namespace std;

int main()
{
  ifstream in("C-small-attempt0.in");
  ofstream out("output.txt");

  int T;
  in>>T;
  for(int t=0; t<T; t++)
  {
    int N, Q;
    in>>N>>Q;
    vector<pair<pair<ld, int>, int>> P[N];
    for(int i=0, a, b; i<N; i++)
    {
      in>>a>>b;
      P[i].push_back({{0,a}, b});
    }
    int d[N];

    for(int i=0; i<N; i++)
     for(int j=0, a; j<N; j++)
     {
       in>>a;
       if(a != -1)
        d[i] = a;
     }
    int a, b; in>>a>>b;

    for(int i=0; i<N-1; i++)
    {
      ld mn = -1;
      for(int j=1; j<P[i].size(); j++)
      {
       if(P[i][j].e >= d[i])
       {
         ld dst = P[i][j].dist + ((ld)d[i] / (ld)P[i][j].s);
         P[i+1].push_back({{dst, P[i][j].e-d[i]}, P[i][j].s});
       }
        if(mn == -1 || P[i][j].dist < mn) mn = P[i][j].dist;
      }

      if(mn == -1) mn = 0;
      if(P[i][0].e >= d[i])
      {
        ld dst = mn + ((ld)d[i] / (ld)P[i][0].s);
        P[i+1].push_back({{dst, P[i][0].e-d[i]}, P[i][0].s});
      }
    }
    ld mn = -1;
    for(int i=1; i<P[N-1].size(); i++)
     if(mn == -1 || P[N-1][i].dist < mn)
      mn = P[N-1][i].dist;
    out<<"Case #"<<(t+1)<<": "<<std::fixed<<std::setprecision(9)<<mn<<"\n";
    /*for(int i=0; i<N-1; i++)
    {
      for(int j=0; j<P[i].size(); i++)
       if(P[i][j].e >= d[i])
       {
         ld dst = P[i][j].dist + ((ld)d[i] / (ld)P[i][j].s);
         P[i+1].push_back({{dst, P[i][j].e - d[i]}, P[i][j].s});
       }
    }

    ld mn = -1;
    for(int i=0; i<P[N-1].size(); i++)
     if(mn == -1 || P[N-1][i].dist < mn)
      mn = P[N-1][i].dist;
    out<<"Case #"<<(t+1)<<": "<<std::fixed<<std::setprecision(6)<<mn<<"\n";*/
  }

  in.close();
  out.close();
  return 0;
}
