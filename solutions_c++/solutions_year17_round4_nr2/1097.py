#include<bits/stdc++.h>
using namespace std;
#define REP(_x,_y) for(int (_x)=0;(_x)<(_y);(_x)++)
#define FOR(_x,_y,_z) for(int (_x)=(_y);(_x)<=(_z);(_x)++)
#define FORD(_x,_y,_z) for(int (_x)=(_y);(_x)>=(_z);(_x)--)
#define RESET(_x,_y) memset((_x),(_y),sizeof(_x))
#define SZ(_x) ((int)(_x).size())
#define LEN(_x) strlen(_x)
#define ALL(_x) (_x).begin(),(_x).end()
#define LL long long
#define ULL unsigned LL
#define PII pair<int,int>
#define VI vector<int>
#define VII vector< PII >
#define VVI vector< VI >
#define MP make_pair
#define PB push_back
#define F first
#define S second
const int INF=1e9;
const int MOD=1e9+7;
int t,tc=1,n,c,m,p[1000],b[1000];
multiset<int> ms[2];
bool find_match(int i,VVI &w,VI &mr,VI &mc,VI &seen){
    for(int j=0;j<(int)w[i].size();j++){
        if(w[i][j]&&!seen[j]){
            seen[j]=1;
            if(mc[j]<0||find_match(mc[j],w,mr,mc,seen)){
                mr[i]=j;
                mc[j]=i;
                return 1;
            }
        }
    }
    return 0;
}
int bipartite_matching(VVI &w,VI &mr,VI &mc){
    mr=VI((int)w.size(),-1);
    if((int)w.size()>0)mc=VI((int)w[0].size(),-1);
    int res=0;
    for(int i=0;i<(int)w.size();i++){
        VI seen=VI((int)w[0].size(),0);
        if(find_match(i,w,mr,mc,seen))res++;
    }
    return res;
}
VI le,ri;
int main(){
    freopen("b_small.in","r",stdin);
    freopen("b_small.out","w",stdout);
    scanf("%d",&t);
    while(t--){
        scanf("%d %d %d",&n,&c,&m);
        REP(i,m)scanf("%d %d",&p[i],&b[i]);
        if(c==2){
            le.clear();
            ri.clear();
            REP(i,m){
                if(b[i]==1)le.PB(p[i]);
                else ri.PB(p[i]);
            }
            VVI w=VVI(SZ(le),VI());
            REP(i,SZ(le))w[i]=VI(SZ(ri),0);
            REP(i,SZ(le)){
                REP(j,SZ(ri)){
                    if(le[i]!=ri[j])w[i][j]=1;
                }
            }
            VI mr,mc;
            int matched=bipartite_matching(w,mr,mc);
            VI unmatched_le,unmatched_ri;
            REP(i,SZ(mr)){
                if(mr[i]==-1)unmatched_le.PB(le[i]);
            }
            REP(i,SZ(mc)){
                if(mc[i]==-1)unmatched_ri.PB(ri[i]);
            }
            w=VVI(SZ(unmatched_le),VI());
            REP(i,SZ(unmatched_le))w[i]=VI(SZ(unmatched_ri),0);
            REP(i,SZ(unmatched_le)){
                REP(j,SZ(unmatched_ri)){
                    assert(unmatched_le[i]==unmatched_ri[j]);
                    if(unmatched_le[i]>1||unmatched_ri[j]>1)w[i][j]=1;
                }
            }
            int unmatched_matched=bipartite_matching(w,mr,mc);
            int x=0,y=0;
            REP(i,SZ(mr)){
                if(mr[i]==-1)x++;
            }
            REP(i,SZ(mc)){
                if(mc[i]==-1)y++;
            }
//            assert(matched+unmatched_matched+x+y>=max(SZ(le),SZ(ri)));
            int haha=matched+unmatched_matched+x+y;
            haha=max(haha,max(SZ(le),SZ(ri)));
            printf("Case #%d: %d %d\n",tc++,haha,unmatched_matched);
        }
    }
    return 0;
}
