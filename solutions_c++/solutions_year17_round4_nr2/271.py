#include<bits/stdc++.h>
using namespace std;

typedef vector<int> vi;
typedef long long int LL;
typedef pair<int,int> pi;
typedef unsigned long long int ull;
#define mp make_pair

int TC,N,P,a,b,c,n,m;
int sn[2000],pn[2000];

int main(){
    std::ios::sync_with_stdio(false);
    freopen("B-large.in","r",stdin);
    freopen("out.txt","w",stdout);
    cin >> TC;
    for (int outi=0;outi<TC;outi++){
        cout << "Case #" << outi+1 << ": ";
        cin >> n >> c >> m;
        memset(pn,0,sizeof pn);
        memset(sn,0,sizeof sn);
        int ans1 = 0;
        for (int i=0;i<m;i++){
            cin >> a >> b;
            pn[b]++;ans1 = max(ans1,pn[b]);
            sn[a]++;
        }
        int sum = 0;
        for (int i=1;i<=n;i++){
            sum += sn[i];
            ans1 = max(ans1, int(ceil(sum*1.0/i)));
        }
        int ans2 = 0;
        for (int i=1;i<=n;i++){
            ans2 += max(0, sn[i]-ans1);
        }
        cout << ans1 << " " << ans2 << "\n";
    }
}
