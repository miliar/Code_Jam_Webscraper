#include<cstdio>
#include<vector>
#include<algorithm>
#include<cstring>
#include<set>
using namespace std;
struct packbound{
    int ni, pi, lb, ub;
    bool boundstart;
};
struct packboundcmp{
    bool operator()(packbound a, packbound b){
        if(a.ni == b.ni){
            return a.pi < b.pi;
        }
        else return a.ni < b.ni;
    }
};
int basenum[50];
int packlb[50][50], packub[50][50];
int packcnt[50];
vector<packbound> bounds;
set<packbound, packboundcmp> currpacks[50];
bool packboundcmpfirst(packbound a, packbound b){
    int aci = a.boundstart ? a.lb : a.ub;
    int bci = b.boundstart ? b.lb : b.ub;
    if(aci == bci){
        if(a.boundstart == b.boundstart){
            return a.ub < b.ub;
        }
        else return (!a.boundstart) && b.boundstart;
    }
    else return aci < bci;
}
int main(){
    int numcases; scanf("%d", &numcases);
    for(int ccase = 0; ccase < numcases; ccase++){
        int N, P; scanf("%d%d", &N, &P);
        for(int i = 0; i < N; i++){
            scanf("%d", &basenum[i]);
        }
        bounds.clear();
        for(int i = 0; i < N; i++){
            for(int i2 = 0; i2 < P; i2++){
                int cpacknum; scanf("%d", &cpacknum);
                int cpacklbcmp = cpacknum - cpacknum / 11;
                int cpacklb = cpacklbcmp / basenum[i];
                if(cpacklbcmp % basenum[i] != 0) cpacklb++;
                packlb[i][i2] = cpacklb;
                int cpackubcmp = cpacknum + cpacknum / 9;
                int cpackub = cpackubcmp / basenum[i];
                cpackub++;
                packub[i][i2] = cpackub;
                if(cpackub > cpacklb){
                    bounds.push_back(packbound{
                        i, i2, cpacklb, cpackub, true
                    });
                    bounds.push_back(packbound{
                        i, i2, cpacklb, cpackub, false
                    });
                }
            }
        }
        sort(bounds.begin(), bounds.end(), packboundcmpfirst);
        memset(packcnt, 0, sizeof(packcnt));
        for(int i = 0; i < N; i++)
            currpacks[i] = set<packbound, packboundcmp>();
        int rescnt = 0;
        for(size_t i = 0; i < bounds.size(); i++){
            if(bounds[i].boundstart)
                currpacks[bounds[i].ni].insert(bounds[i]);
            else
                currpacks[bounds[i].ni].erase(bounds[i]);
            bool cancombine = true;
            for(int i2 = 0; i2 < N; i2++){
                if(currpacks[i2].empty()){
                    cancombine = false;
                    break;
                }
            }
            if(cancombine){
                rescnt++;
                for(int i2 = 0; i2 < N; i2++){
                    currpacks[i2].erase(currpacks[i2].begin());
                }
            }
        }
        printf("Case #%d: %d\n", ccase + 1, rescnt);
    }
    return 0;
}
