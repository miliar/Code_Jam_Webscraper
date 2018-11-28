#include<iostream>
#include<cstdio>
#include<algorithm>
#include<vector>
#include<cstring>
#include<string>
#include<set>
#include<queue>
#include<cstdlib>
#include<cmath>
#include<functional>

class pan{
public:
  double r;
  double h;
  pan(){
    this->r=0.0f;
    this->h=0.0f;
  }
  pan(double R, double H){
    this->r=R;
    this->h = H;
  }
};

typedef struct cmax{
  double val;
  int last;
}cmax;

bool comp(pan a, pan b){
  return (a.r < b.r ? true : (a.r == b.r && a.h < b.h ? true : false));
}

    cmax surf[1001][1001];
using namespace std;
int main(){
  int T, t;
  scanf("%d", &T);
  t =  T;
  double pi = atan(1) * 4.0f;
  while(T--){
    double r, h;
    int N, K;
    scanf("%d %d", &N, &K);
    vector<pan> cake = vector<pan>(N);
    vector<double> disc = vector<double>(N);
    vector<double> side = vector<double>(N);
    for(int i=0; i<=1000; i++){
      for(int j=0; j<=1000; j++){
        surf[i][j].val = 0.0f;
        surf[i][j].last = -1;
      }
    }
    for(int i=0; i<N; i++){
      scanf("%lf %lf", &r, &h);
      cake[i] = pan(r, h);
    }
    sort(cake.begin(), cake.end(), comp);
    for(int i=0; i<N; i++){
      disc[i] = pi * (cake[i].r * cake[i].r);
      side[i] = 2 * pi * (cake[i].r * cake[i].h);
    }
    surf[0][1].val = disc[0] + side[0];
    surf[0][1].last = 0;
    for(int i=1; i<N; i++){
      for(int j=1; j<=(i+1 > K ? K : i+1); j++){
        double pre, add, rep;
        int prei=-1, addi=-1, repi=-1;
        pre = surf[i-1][j].val;
        prei = surf[i-1][j].last;
        add = surf[i-1][j-1].val - disc[surf[i-1][j-1].last] + disc[i] + side[i];
        addi = i;
        rep = surf[i-1][j].val - disc[surf[i-1][j].last] - side[surf[i-1][j].last] + disc[i] + side[i];
        repi = i;
        double pres, presi;
        if(pre < add){
          pres = add;
          presi = addi;
        }
        else{
          pres = pre;
          presi = prei;
        }
        if(pres < rep){
          pres = rep;
          presi = repi;
        }
        surf[i][j].val = pres;
        surf[i][j].last = presi;
      }
    }
    printf("Case #%d: %.9f\n", t - T, surf[N-1][K].val);

  }
  return 0;
}
