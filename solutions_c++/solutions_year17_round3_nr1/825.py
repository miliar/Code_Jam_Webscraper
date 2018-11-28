#include <bits/stdc++.h>
using namespace std;

typedef pair<int,int> ii;
typedef pair<int,int> dd;

#define sc(x) scanf("%d",&x)
#define scs(x) scanf("%s",x)
#define fr(i,a,b) for(int i = a; i < b; i++)
#define fre(i,a,b) for(int i = a; i <= b; i++)
#define clr(a,v) memset(a,v,sizeof a)
#define F first
#define S second

#define N 1123
int t,n,k,r,h;
double ans;

const double pi = acos(-1);

struct pan{
  int r;
  int h;
  double totalArea,topArea, sideArea;
  pan(){}
  pan(int r, int h):r(r),h(h){
    topArea = double(r)*r*pi;
    sideArea = 2.0*pi*r*h;
    totalArea = topArea + sideArea;
  }
};


pan A[N];

bool comp(pan a, pan b){
  if (a.r > b.r) return 1;
  if (a.r < b.r) return 0;
  return (a.h > b.h);
}

double memo[N][N];
int step[N][N];
int z;

double go(int pos, int left){
  if (pos >= n || left == 0) return 0;

  if (step[pos][left] == z) return memo[pos][left];

  double ret = 0;

  ret = A[pos].sideArea + go(pos+1,left-1);
  if (left == k) ret += A[pos].topArea;
  ret = max(ret,go(pos+1,left));

  step[pos][left] = z;
  return memo[pos][left] = ret;
}


int main(){
    sc(t);
    fre(ca,1,t){
      z++;
      printf("Case #%d: ",ca);
      sc(n), sc(k);
      fr(i,0,n){
        sc(r), sc(h);
        A[i] = pan(r,h);
      }
      sort(A,A+n, comp);
      ans = go(0,k);
      //ans = A[0].topArea;
      //fr(i,0,k) ans += A[i].sideArea;

      //fr(i,0,n) printf("%d %d\n",A[i].r, A[i].h);
      printf("%.6lf\n",ans);

    }
    return 0;
}
