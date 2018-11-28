#include<bits/stdc++.h>
using namespace std;
typedef long long LL;

#define CIN_ONLY if(1)
struct cww{cww(){
    CIN_ONLY{
        ios::sync_with_stdio(false);cin.tie(0);
    }
}}star;
#define fin "\n"
#define FOR(i,bg,ed) for(int i=(bg);i<(ed);i++)
#define REP(i,n) FOR(i,0,n)
#define ALL(v) (v).begin(),(v).end()
#define fi first
#define se second
#define pb push_back
#define DEBUG if(0)
#define REC(ret, ...) std::function<ret (__VA_ARGS__)>
template <typename T>inline bool chmin(T &l,T r)
{bool a=l>r;if(a)l=r;return a;}
template <typename T>inline bool chmax(T &l,T r)
{bool a=l<r;if(a)l=r;return a;}
template <typename T>
istream& operator>>(istream &is,vector<T> &v){
    for(auto &it:v)is>>it;
    return is;
}
int latte(int h,int a,int H,int A,int fullH){
    REP(i,300){
        if(a>=H)return i+1;
        int dm=0;
        if(A>=h){
            h=fullH;
        }
        else
            dm=a;
        H-=dm;
        h-=A;
        if(h<=0){
            return 112345678;
        }
    }
    return 112345678;
}
void solve(){
    int h,a,H,A,B,D;
    cin>>h>>a>>H>>A>>B>>D;
    int nh=h;
    int na=a;
    int nH=H;
    int nA=A;
    int res=112345678;
    int nturn=0;
    REP(i,101){
        int nnh=nh;
        int nna=na;
        int nnH=nH;
        int nnA=nA;
        int nnturn=nturn;
        
        REP(j,101){
            chmin(res,nnturn+latte(nnh,nna,nnH,nnA,h));
            while(nnh-nnA<=0){
                if(h<=nnA+nnA){
                    j=101;break;
                }
                else{
                    nnh=h-nnA;
                    nnturn++;
                }
                if(nnh<=0){
                    j=101;break;
                }
            }
            nna+=B;
            nnturn++;
            nnh=max(0,nnh-nnA);
        }
        int xtA=max(0,nA-D);
        while(nh-xtA<=0){
            if(h<=nnA+max(nnA-D,0)){
                i=101;break;
            }
            else{
                nh=h-nA;
                nturn++;
            }
            if(nh<=0){
                i=101;break;
            }
        }
        nA=xtA;
        nturn++;
        nh=max(0,nh-nA);
    }
    if(res==112345678)cout<<"IMPOSSIBLE"<<endl;
    else cout<<res<<endl;
}
int main(){
    int T;
    cin>>T;
    FOR(i,1,T+1){
        cout<<"Case #"<<i<<": ";
        solve();
    }
    return 0;
}
