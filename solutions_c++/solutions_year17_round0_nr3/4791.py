#include <bits/stdc++.h>
using namespace std;
typedef long long lli;
lli tr[3*1000005];
bool done[3*1000005];
int aa, bb;
void first(int nd, int b, int e){
    if(b>e) return;
    tr[nd]=e-b+1;
    //cout<<b<<' '<<e<<' '<<tr[nd]<<endl;
    int lft=nd*2, rght=nd*2+1, m=(b+e)/2;
    first(lft, b, m-1); first(rght, m+1, e);
}
void tree(int nd, int b, int e){
    int lft=nd*2, rght=nd*2+1, m=(b+e)/2;
    //cout<<b<<' '<<e<<endl;
    if(!done[nd]){
        int x=(e-b)/2; int y=e-b-x;
        done[nd]=true;
        if(e-b==1) x=0, y=1;
        else if(e-b==0) x=0, y=0;
        tr[lft]=x; tr[rght]=y;
        tr[nd]=max(tr[lft], tr[rght]);
        aa=x; bb=y;
        //cout<<"a b: "<<b<<' '<<e<<' '<<x<<' '<<y<<endl;
        return;
    }
    if(tr[lft]>=tr[rght]) tree(lft, b, m-1);
    else tree(rght, m+1, e);
    tr[nd]=max(tr[lft], tr[rght]);
}
int main()
{
    //freopen("input.txt", "r", stdin);
    //freopen("output.txt", "w", stdout);
    int t, cs=0;
    cin>>t;
    while(t--){
        lli n, k;
        cin>>n>>k;
        first(1, 1, n);
        aa=0, bb=0;
        memset(done, 0, sizeof done);
        for(int i=0; i<k; i++){
            tree(1, 1, n);
        }
        printf("Case #%d: %d %d\n", ++cs, bb, aa);
    }
}
