#include <bits/stdc++.h>
#define  ren(i,j,n) for(li i=(j);i<(n);i++)
#define  rep(i,n) ren(i,0,(n))
#define  all(a) begin(a),end(a)
using namespace std;
typedef long int li;
typedef unsigned long long ull;
typedef vector<int> vi;
typedef vector<li> vli;
typedef vector<string> vs;

int main()
{
    int t;
    cin>>t;
    rep(i,t){
        li n,k,m;
        cin>>n>>k;
        bool a[n+2];
        rep(i,n+2) a[i]=0;
        a[0]=a[n+1]=1;
        rep(i,k){
            m=0;
            int seq=0,p;
            for(int i=1;i<=n+1;i++){
                if(a[i]==0) seq++;
                else {
                    if(m<seq)m=seq,p=i-m/2-1;
                    seq=0;                
                }
            }
            a[p]=1;
        }
        cout<<"Case #"<<i+1<<": "<<m/2<<" "<<m-(m/2+1)<<"\n";
    }
    return 0;
}
