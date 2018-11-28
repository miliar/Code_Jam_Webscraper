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
#include <unordered_map>

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

int main()
{
    freopen("out.txt","w",stdout);
    freopen("C-large.in","r",stdin);
    //freopen("in.txt","r",stdin);
    int t, test = 0;
    cin>>t;
    while(t--){
        cout<<"Case #"<<++test<<": ";
        LL n, k;
        cin>>n>>k;
        unordered_map<LL, LL> h;
        h[n] = 1;
        LL k1 = k>>1;
        LL n1 = n, n2 = n;
        LL cnt = (LL)1;
        k--;
        while(k1){
            //cout<<k<<' '<<k1<<' '<<n1<<' '<<n2<<' '<<h[n1]<<' '<<h[n2]<<endl;
            k1 >>= 1;
            cnt <<= 1;
            if(k1 > 0) k -= cnt;
            unordered_map<LL, LL> h1;
            LL n3 = (n1-1)>>1, n4 = n1-1-n3;
            h1[n3] += h[n1]; h1[n4] += h[n1];
            if(n1 != n2){
                LL n5 = (n2-1)>>1, n6 = n2-1-n5;
                h1[n5] += h[n2]; h1[n6] += h[n2];
            }
            auto it = h1.begin();
            n1 = (*it).first;
            if(h1.size() > 1) n2 = (*(++it)).first;
            else n2 = n1;
            if(n1 > n2) swap(n1, n2);
            h[n1] = h1[n1]; h[n2] = h1[n2];
        }
        if(k <= h[n2]){
            LL n3 = (n2-1)>>1, n4 = n2-1-n3;
            cout<<max(n3, n4)<<' '<<min(n3, n4)<<endl;
        }
        else{
            LL n3 = (n1-1)>>1, n4 = n1-1-n3;
            cout<<max(n3, n4)<<' '<<min(n3, n4)<<endl;
        }
    }
    return(0);
}

