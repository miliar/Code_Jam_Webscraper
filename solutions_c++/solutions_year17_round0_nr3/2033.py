#pragma comment(linker, "/STACK:1024000000,1024000000")
#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <cmath>
#include <vector>
#include <set>
#include <map>
#include <string>
using namespace std;
#define LL long long
#define mp make_pair
#define fr first
#define sc second
#define pb push_back
#define lc (x<<1)
#define rc ((x<<1)|1)
const int M=205;
const LL two=2ll;
LL q[M],qn[M];
int main(){
   // freopen("in.txt","r",stdin);freopen("out.txt","w",stdout);
    int T,T0=0;cin>>T;
    while (T--){
        LL n,k,m=0;cin>>n>>k;
        int h,t;q[h=t=1]=n;qn[1]=1;
        while (1){
            m+=qn[h];
            if (m>=k) break;
            LL a=q[h]/two,b=q[h]-a-1;
            if (a!=q[t]) q[++t]=a,qn[t]=0;
            qn[t]+=qn[h];
            if (b!=q[t]) q[++t]=b,qn[t]=0;
            qn[t]+=qn[h];
            h++;
        }
        cout<<"Case #"<<++T0<<": ";
        cout<<q[h]/two<<" "<<q[h]-q[h]/two-1<<endl;
    }
  //  system("pause");
    return 0;
}
