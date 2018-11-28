#include <vector>
#include <utility>
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
#define NegOne(i) memset((i),0xff,sizeof((i)))
#define Bit(s,i) (( (s) &(1<<(i)))>0)
#define NP next_permutation

//const double PI = acos(-1.0);
//const double EPS = 1e-9;
//const int ioo = (~0)-(1<<31);
//const LL loo = (~(LL)0)-((LL)1<<63);
//const int MOD = 1000000007;
//const LL MODL = 1000000007;;

int Scan()    
{
  int res=0,ch,flag=0;
  if((ch=getchar())=='-')
      flag=1;
  else if(ch>='0'&&ch<='9')
      res=ch-'0';
  while((ch=getchar())>='0'&&ch<='9')
      res=res*10+ch-'0';
  return flag?-res:res;
}

void Out(int a)  
{
  if(a>9)
      Out(a/10);
  putchar(a%10+'0');
}

typedef struct node{
    int cnt;
    int col;
}node;

bool operator < (const node &x, const node &y){
    return x.cnt < y.cnt;
}

const string tag = "ROYGBV";

int main()
{
    freopen("out.txt","w",stdout);
    freopen("B-small-attempt0.in","r",stdin);
    int t, test = 0;
    cin>>t;
    while(t--){
        cout<<"Case #"<<++test<<": ";
        int N; cin>>N;
        int a[6];
        for(int i = 0; i < 6; i++){
            cin>>a[i];
        }
        bool sol = false;
        for(int i = 0; i < 6; i++){
            if(a[i] == 0) continue;
            priority_queue<node> pq;
            int ans[1000] = {0};
            node tmp; tmp.col = i; tmp.cnt = a[i]-1;
            ans[0] = i;
            if(tmp.cnt) pq.push(tmp);
            for(int j = 0; j < 6; j++){
                if(j == i || a[j] == 0) continue;
                tmp.col = j; tmp.cnt = a[j];
                pq.push(tmp);
            }
            bool flag = true;
            for(int i = 1; i < N; i++){
                tmp = pq.top(); pq.pop();
                if(tmp.col == ans[i-1]){
                    if(pq.empty()){
                        flag = false;
                        break;
                    }
                    node tmp1 = pq.top(); pq.pop();
                    ans[i] = tmp1.col; tmp1.cnt--;
                    pq.push(tmp); if(tmp1.cnt) pq.push(tmp1);
                }
                else{
                    ans[i] = tmp.col; tmp.cnt--;
                    if(tmp.cnt) pq.push(tmp);
                }
            }
            if(ans[0] == ans[N-1]) flag = false;
            if(flag){
                for(int i = 0; i < N; i++) cout<<tag[ans[i]];
                cout<<endl;
                sol = true;
                break;
            }
        }
        if(!sol) cout<<"IMPOSSIBLE"<<endl;
    }
    return(0);
}

