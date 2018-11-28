#include<bits/stdc++.h>
using namespace std;
const int MX = 100;
set < pair < int , int > > S[MX];
int need[MX];
struct item{
    int x , who , y , idx;
    item(){}
    item(int x , int who , int y , int idx):x(x) , who(who) , y(y) , idx(idx){}
};
int n , P;
bool operator < (const item&A , const item&B){
    return A.x < B.x;
}
void nk7(item Q){
    if(Q.who > 0)
        S[Q.who].insert({Q.y , Q.idx});
    else S[-Q.who].erase({Q.y , Q.idx});
}
bool exist(){
    bool ok = 1;
    for(int j = 1 ; j <= n ; j++) ok &= (!S[j].empty());
    if(!ok) return 0;
    for(int j = 1 ; j <= n ; j++) S[j].erase(S[j].begin());
    return 1;
}    int T , Tn = 0;

int main(){
    freopen("in.in","r",stdin);
    freopen("out.out","w",stdout);
    cin>>T;
    while(T--){
        for(int j = 1 ; j < MX ; j++) S[j].clear();

        scanf("%d %d",&n,&P);
        for(int j = 1 ; j <= n ; j++) scanf("%d",&need[j]);
        vector < item > sorted;
        for(int j = 1 ; j <= n ; j++){
            for(int i = 1 ; i <= P ; i++){
                int X; scanf("%d",&X);
                int st = 0  , en = X / need[j] , mid , atleast = en + 1;
                while(st <= en){
                    mid = (st + en)/2;
                    long long A = 1ll * mid * need[j];
                    long long B = X;
                    if(B * 100ll > 110ll * A)
                        st = mid + 1;
                    else {
                        atleast = mid;
                        en = mid-1;
                    }
                }
                st = X / need[j] + 1 , en = 2 * 1e6;
                int atmost = st - 1;
                while(st <= en){
                    mid = (st + en)/2;
                    long long A = 1ll * mid * need[j];
                    long long B = X;
                    if(B * 100ll < 90ll * A){
                        en = mid-1;
                    }
                    else {
                        atmost = mid;
                        st = mid + 1;
                    }
                }
                if(atleast <= atmost){
                    sorted.push_back(item(atleast , j , atmost , i));
                    sorted.push_back(item(atmost + 1 , -j , atmost , i));
                }
            }
        }
        sort(sorted.begin() , sorted.end());
        reverse(sorted.begin() , sorted.end());
        int ans = 0;
        while(!sorted.empty()){
            int cor = sorted.back().x;
            while(!sorted.empty() && sorted.back().x == cor){
                nk7(sorted.back());
                sorted.pop_back();
            }
            while(exist()) ans++;
        }
        printf("Case #%d: %d\n",++Tn,ans);
    }
}

