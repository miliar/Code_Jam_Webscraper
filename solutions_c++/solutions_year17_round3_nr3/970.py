#include <vector>
#include <iostream>
#include <map>
#include <set>
#include <algorithm>
#include <stack>
#include <queue>
#include <string>
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <cstdio>
#include <list>
#include <bitset>
#include <climits>

using namespace std;

typedef long long LL;
typedef unsigned long long ULL;
typedef vector<int> vI;
typedef vector<double> vD;
typedef vector<pair<int, int> > vpI;
typedef vector<string> vS;
typedef pair<int, int> pI;
typedef pair<double, double> pD;
typedef map<int, int> mI;
typedef map<string, int> mSI;
typedef map<int, pair<int, int> > mIP;
typedef map<pair<int, int>, int> mPI;
typedef set<int> sI;
typedef set<pI> sPI;
typedef set<string> sS;
typedef priority_queue<int> Qmax;
typedef priority_queue<int, vector<int>, greater<int> >Qmin;

#define TWO(k)  (1<<(k))
#define LTWO(k) (((LL)(1)<<(k)))
#define MP make_pair
#define PB push_back
#define FI first
#define SE second
#define For(i,a,b) for(int (i)=(a);(i)<=(b);(i)++)
#define Ford(i,a,b) for(int (i)=(a);(i)>=(b);(i)--)
#define For0(n) for(int (i)=0;(i)<(n);(i)++)
#define For1(n) for(int (i)=1;(i)<=(n);(i)++)
#define Zero(i) memset((i),0,sizeof((i)))
#define Fu1(i) memset((i),0xff,sizeof((i)))
#define Bit(s,i) (( (s) &(1<<(i)))>0)
#define NP next_permutation

const double PI = acos(-1.0);
//const double EPS = 1e-9;
//const int ioo = (~0)-(1<<31);
//const LL loo = (~(LL)0)-((LL)1<<63);
//const int MOD = 1000000007;
//const LL MODL = 1000000007;;

void Out(int a){
  if(a>9)
      Out(a/10);
  putchar(a%10+'0');
}

typedef struct node{
    LL r;
    LL h;
    int id;
}node;

bool cmp(const node &x, const node &y){
    if(x.r * x.h == y.r*y.h){
        return x.r > y.r;
    }
    return x.r*x.h > y.r*y.h;
}

bool cmp1(const node &x, const node &y){
    if(x.r == y.r){
        return x.h > y.h;
    }
    return x.r > y.r;
}


int main(){
    freopen("out.txt","w",stdout);
    freopen("A-large.in","r",stdin);
    //freopen("in.txt","r",stdin);
    int t, test = 0;
    cin>>t;
    while(t--){
        cout<<"Case #"<<++test<<": ";
        int n, k;
        node a[1005];
        node b[1005];
        cin>>n>>k;
        for(int i = 0; i < n; i++){
            cin>>a[i].r>>a[i].h; a[i].id = i;
            b[i] = a[i];
        }
        double ans = 0.0;
        for(int i = 0; i < n; i++){
            vector<node> tmp;
            for(int j = 0; j < n; j++){
                if(a[j].id != i && a[j].r <= a[i].r){
                    tmp.PB(a[j]);
                }
            }
            if(tmp.size() < k-1) continue;
            sort(tmp.begin(), tmp.end(), cmp);
            double t = 2*PI*a[i].r*a[i].h + PI*a[i].r*a[i].r;
            for(int j = 0; j < k-1; j++){
                t += 2*PI*tmp[j].r*tmp[j].h;
            }
            ans = max(ans, t);
        }
        printf("%.8f\n", ans);
    }
    return(0);
}

