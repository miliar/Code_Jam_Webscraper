#include <cstdio>
#include <algorithm>
#include <string>
#include <vector>
int N;
bool check1(int C1, int C2, char c1, char c2){
    if(C1 != 0 && C1 == C2){
        if(N != C1+C2) printf("IMPOSSIBLE");
        else for(int i = 0; i< C1; i++) printf("%c%c",c1,c2);
        printf("\n");
        return true;
    }
    return false;
}
int main(){
    int T;
    scanf("%d",&T);
    for(int tc = 1; tc<=T;tc++){
        int R,O,Y,G,B,V;
        scanf("%d%d%d%d%d%d%d",&N,&R,&O,&Y,&G,&B,&V);
        printf("Case #%d: ", tc);
        if(O > B || G > R || V > Y) {
            printf("IMPOSSIBLE\n");
            continue;
        }
        if(N == O+B && B==O+1) {printf("IMPOSSIBLE\n"); continue;}
        if(N == V+Y && Y==V+1) {printf("IMPOSSIBLE\n"); continue;}
        if(N == G+R && R==G+1) {printf("IMPOSSIBLE\n"); continue;}

        if(check1(O,B,'O','B')) continue;
        if(check1(V,Y,'V','Y')) continue;
        if(check1(G,R,'G','R')) continue;

        B-=O;
        Y-=V;
        R-=G;

        std::pair<int,char> sorted[] = {{B,'B'},{Y,'Y'},{R,'R'}};
        std::sort(sorted,sorted+3);
        if(sorted[2].first > sorted[0].first+sorted[1].first){
            printf("IMPOSSIBLE\n"); continue;
        }
        std::string tmp;
        tmp.push_back(sorted[2].second);

        std::vector<std::string> ans(sorted[2].first);
        for(int i = 0; i < sorted[2].first; i++) ans[i].push_back(sorted[2].second);

        for(int i = 0; i < sorted[1].first;i++){
            ans[i%ans.size()].push_back(sorted[1].second);
        }
        for(int i = 0; i < sorted[0].first;i++){
            ans[(i+sorted[1].first)%ans.size()].push_back(sorted[0].second);
        }
        for(auto& s : ans){
            for(auto c:s){
                if(c == 'B' && O != 0){
                    for(int i = 0; i< O;i++) printf("BO");
                    O=0;
                }
                if(c == 'Y' && V != 0){
                    for(int i = 0; i< V;i++) printf("YV");
                    V=0;
                }
                if(c == 'R' && G != 0){
                    for(int i = 0; i< G;i++) printf("RG");
                    G=0;
                }
                printf("%c",c);
            }
        }
        printf("\n");
    }
}
