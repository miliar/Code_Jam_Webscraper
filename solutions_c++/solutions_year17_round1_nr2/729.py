#include<bits/stdc++.h>
using namespace std;

typedef vector<int> vi;
typedef long long int LL;
typedef pair<int,int> pi;
typedef unsigned long long int ull;



pi calc(int a,int b){
    double top = floor(b/0.9/a);
    double btm = ceil(b/1.1/a);
    return(make_pair(top,btm));
}

int TC,N,P,amo[60],a;
vector<pi> f[60];
bool jud;
pi ph;

pi jj(pi a,pi b){
    return(make_pair(min(a.first,b.first), max(a.second,b.second)));
}

int main(){
    std::ios::sync_with_stdio(false);
    freopen("B-large.in","r",stdin);
    freopen("out.txt","w",stdout);
    cin >> TC;
    for (int outi=0;outi<TC;outi++){
        cout << "Case #" << outi+1 << ": ";
        cin >> N >> P;
        for (int i = 0;i<N;i++) cin >> amo[i];
        for (int i = 0;i<N;i++){
            f[i].clear();
            for (int j = 1;j<=P;j++){
                cin >> a;
                ph = calc(amo[i],a);
                if (ph.second<=ph.first) f[i].push_back(ph);
            }
            sort(f[i].begin(),f[i].end());
            reverse(f[i].begin(),f[i].end());
        }
        jud = true;
        int ans = 0;
        while (jud){
            pi res = make_pair(10000000,0);
            pi minh = make_pair(10000000,10000000);
            int minp = -1;
            for (int i=0;i<N;i++){
                if (f[i].size()>0){
                    ph = f[i].back();
                    if (ph<minh) {minh=ph;minp=i;}
                    res = jj(res,ph);
                }
                else jud = false;
            }
            if (!jud) jud = false;
            else if (res.first>=res.second){
                ans++;
                for (int i=0;i<N;i++) f[i].pop_back();
            }
            else f[minp].pop_back();
        }
        cout << ans << "\n";

    }
}
