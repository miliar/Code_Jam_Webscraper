#include<cstdio>
#include<cstring>
#include<vector>
#include<utility>
using namespace std;
struct AugPath {
    int A, B;   //size of left, right groups
    vector<vector<int> > G; //size A
    vector<bool> visited;   //size A
    vector<int> P;          //size B
    
    AugPath(int _A, int _B): A(_A), B(_B), G(_A), P(_B, -1) {}
    
    void AddEdge(int a, int b) {    //a from left, b from right
        G[a].push_back(b);
    }
    bool Aug(int x) {
        if (visited[x]) return 0;
        visited[x] = 1;
        /* Greedy heuristic */
        for (auto it:G[x]) {
            if (P[it] == -1) {
                P[it] = x;
                return 1;
            }
        }
        for (auto it:G[x]) {
            if (Aug(P[it])) {
                P[it] = x;
                return 1;
            }
        }
        return 0;
    }
    int MCBM() {
        int matchings = 0;
        for (int i = 0; i < A; ++i) {
            visited.resize(A, 0);
            matchings += Aug(i);
            visited.clear();
        }
        return matchings;
    }
    vector<pair<int, int> > GetMatchings() {
        vector<pair<int, int> > matchings;
        for (int i = 0; i < B; ++i) {
            if (P[i] != -1) matchings.emplace_back(P[i], i);
        }
        return matchings;
    }
};
AugPath augPath(0, 0);
bool gridplus[100][100], gridcross[100][100];
bool rowdisabled[100], coldisabled[100];
bool ldiagdisabled[200], rdiagdisabled[200];
bool dirty[100][100];
int main(){
    int numcases; scanf("%d", &numcases);
    for(int ccase = 0; ccase < numcases; ccase++){
        int N, M; scanf("%d%d", &N, &M);
        memset(gridplus, false, sizeof(gridplus));
        memset(gridcross, false, sizeof(gridcross));
        memset(rowdisabled, false, sizeof(rowdisabled));
        memset(coldisabled, false, sizeof(coldisabled));
        memset(ldiagdisabled, false, sizeof(ldiagdisabled));
        memset(rdiagdisabled, false, sizeof(rdiagdisabled));
        memset(dirty, false, sizeof(dirty));
        for(int i = 0; i < M; i++){
            char val[2]; int cx, cy; scanf("%s%d%d", val, &cx, &cy);
            cx--; cy--;
            if(val[0] == 'o'){
                gridplus[cy][cx] = true;
                gridcross[cy][cx] = true;
            }
            else if(val[0] == '+')
                gridcross[cy][cx] = true;
            else if(val[0] == 'x')
                gridplus[cy][cx] = true;
        }
        augPath = AugPath(3 * N - 1, 3 * N - 1);
        for(int i = 0; i < N; i++){
            for(int i2 = 0; i2 < N; i2++){
                int ldiagi = (i - i2) + N - 1;
                int rdiagi = i + i2;
                if(gridplus[i][i2]){
                    coldisabled[i2] = true;
                    rowdisabled[i] = true;
                }
                if(gridcross[i][i2]){
                    ldiagdisabled[ldiagi] = true;
                    rdiagdisabled[rdiagi] = true;
                }
            }
        }
        for(int i = 0; i < N; i++){
            for(int i2 = 0; i2 < N; i2++){
                int ldiagi = (i - i2) + N - 1;
                int rdiagi = i + i2;
                if(!coldisabled[i2] && !rowdisabled[i])
                    augPath.AddEdge(i, i2);
                if(!ldiagdisabled[ldiagi] && !rdiagdisabled[rdiagi])
                    augPath.AddEdge(ldiagi + N, rdiagi + N);
            }
        }
        int resVal = augPath.MCBM();
        vector<pair<int, int> > matchings = augPath.GetMatchings();
        for(size_t i = 0; i < matchings.size(); i++){
            if(matchings[i].first < N){
                gridplus[matchings[i].first][matchings[i].second] = true;
                dirty[matchings[i].first][matchings[i].second] = true;
            }
            else{
                int cdiff = matchings[i].first - N - (N - 1);
                int csum = matchings[i].second - N;
                int crow = (csum + cdiff) / 2; 
                int ccol = (csum - cdiff) / 2;
                gridcross[crow][ccol] = true;
                dirty[crow][ccol] = true;
            }
        }
        int dirtycnt = 0;
        int scorecnt = 0;
        for(int i = 0; i < N; i++){
            for(int i2 = 0; i2 < N; i2++){
                if(dirty[i][i2])
                    dirtycnt++;
                if(gridplus[i][i2])
                    scorecnt++;
                if(gridcross[i][i2])
                    scorecnt++;
            }
        }
        printf("Case #%d: %d %d\n", ccase + 1, scorecnt, dirtycnt);
        for(int i = 0; i < N; i++){
            for(int i2 = 0; i2 < N; i2++){
                if(dirty[i][i2]){
                    if(gridplus[i][i2] && gridcross[i][i2])
                        printf("o %d %d\n", i2 + 1, i + 1);
                    else if(gridplus[i][i2])
                        printf("x %d %d\n", i2 + 1, i + 1);
                    else if(gridcross[i][i2])
                        printf("+ %d %d\n", i2 + 1, i + 1);
                }
            }
        }
    }
    return 0;
}
