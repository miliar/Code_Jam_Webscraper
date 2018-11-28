//the 2-sat implementationn taken from https://github.com/kartikkukreja/blog-codes/blob/master/src/2SAT%20in%20linear%20time.cpp

using namespace std;
#include <stdio.h>
#include <algorithm>
#include <map>
#include <vector>
#include <string.h>
#define SIZE 12000

typedef vector<int> vi;

// Assuming vertices are labeled 1...V
vi G[SIZE], Grev[SIZE];
bool explored[SIZE];
int leader[SIZE], finish[SIZE], order[SIZE], t = 0, parent = 0;
map <int, bool> truthAssignment;

// running DFS on the reverse graph
void dfs_reverse(int i) {
    explored[i] = true;
    for(vi::iterator it = Grev[i].begin(); it != Grev[i].end(); it++)
        if(!explored[*it])
            dfs_reverse(*it);
    t++;
    finish[i] = t;
}

// running DFS on the actual graph
void dfs(int i) {
    explored[i] = true;
    leader[i] = parent;
    for(vi::iterator it = G[i].begin(); it != G[i].end(); it++)
        if(!explored[*it])
            dfs(*it);
}

// check if u & v are in the same connected component
bool stronglyConnected(int u, int v)    {
    return leader[u] == leader[v];
}


char configs[55][55];
int R, C;
map<int, int> mEmpty;
map<int, int> mBeam;
int nEmpty;
int nBeam;
vector<int> beamHits;
vector<int> clauses[2550];
int isMustVH[2550];

bool DfsBeam(int y, int x, int dir){
	if(y < 0) return true;
	if(y >= R) return true;
	if(x < 0) return true;
	if(x >= C) return true;
	if(configs[y][x] == '#') return true;
	if(configs[y][x] == '|') return false;
	if(configs[y][x] == '-') return false;
	
	if(configs[y][x] == '.'){
		int cnum = y * C + x;
		beamHits.push_back(mEmpty[cnum]);
		if(dir == 0) return DfsBeam(y, x+1, dir);
		if(dir == 1) return DfsBeam(y+1, x, dir);
		if(dir == 2) return DfsBeam(y, x-1, dir);
		if(dir == 3) return DfsBeam(y-1, x, dir);
	}
	if(configs[y][x] == '\\'){
		if(dir == 0) return DfsBeam(y+1, x, 1);
		if(dir == 1) return DfsBeam(y, x+1, 0);
		if(dir == 2) return DfsBeam(y-1, x, 3);
		if(dir == 3) return DfsBeam(y, x-1, 2);
	}
	if(configs[y][x] == '/'){
		if(dir == 0) return DfsBeam(y-1, x, 3);
		if(dir == 1) return DfsBeam(y, x-1, 2);
		if(dir == 2) return DfsBeam(y+1, x, 1);
		if(dir == 3) return DfsBeam(y, x+1, 0);
	}
	return false;
}

int main() {
	int jcase;
	
	freopen("C-large.in", "r", stdin);
	freopen("C-large.out", "w", stdout);
	
	scanf("%d", &jcase);
	for(int icase=0; icase<jcase; icase++){
		scanf("%d %d", &R, &C);
		gets(configs[0]);
		for(int i=0; i<R; i++){
			gets(configs[i]);
		}
		
		nEmpty = 0;
		nBeam = 0;
		mEmpty.clear();
		mBeam.clear();
		
		for(int i=0; i<R; i++){
			for(int j=0; j<C; j++){
				if(configs[i][j] == '.'){
					int cnum = i*C + j;
					mEmpty[cnum] = nEmpty;
					clauses[nEmpty].clear();
					nEmpty++;
				}
				if(configs[i][j] == '-' || configs[i][j] == '|'){
					int cnum = i*C + j;
					mBeam[cnum] = nBeam;
					nBeam++;
				}
			}
		}
		
		bool isGoodCase = true;
		memset(isMustVH, 0, sizeof(isMustVH));
		for(int i=0; i<R; i++){
			for(int j=0; j<C; j++){
				if(configs[i][j] == '-' || configs[i][j] == '|'){
					beamHits.clear();
					int cnum = i*C + j;
					int beamNo = mBeam[cnum];
					
					bool isGoodCase2 = false;
					bool isGood = DfsBeam(i, j-1, 2);
					if(isGood){
						isGood = DfsBeam(i, j+1, 0);
						if(isGood){
							//add edges
							for(int k=0; k<beamHits.size(); k++){
								clauses[beamHits[k]].push_back(beamNo+1);
							}
							isGoodCase2 = true;
							isMustVH[beamNo] += 1;
						}
					}
					
					beamHits.clear();
					isGood = DfsBeam(i-1, j, 3);
					if(isGood){
						isGood = DfsBeam(i+1, j, 1);
						if(isGood){
							//add edges
							for(int k=0; k<beamHits.size(); k++){
								clauses[beamHits[k]].push_back(-beamNo-1);
							}
							isGoodCase2 = true;
							isMustVH[beamNo] += 2;
						}
					}
					
					if(!isGoodCase2) isGoodCase = false;
				}
			}
		}
		
		if(!isGoodCase){
			printf("Case #%d: IMPOSSIBLE\n", icase+1);
			continue;
		}
		
		// 2 sat
		int N = nBeam; //num of vars
		int M = nEmpty; //num of clause
		int i, u, v;
		
		for(int i=0; i<SIZE; i++){
			G[i].clear();
			Grev[i].clear();
		}
		memset(explored, false, sizeof(explored));
		memset(leader, 0, sizeof(leader));
		memset(finish, 0, sizeof(finish));
		memset(order, 0, sizeof(order));
		truthAssignment.clear();
		t = 0;
		parent = 0;

    for(i=0; i<M; i++)  {
        //scanf("%d %d", &u, &v); 
        int sz = clauses[i].size();
        if(sz == 0){
					isGoodCase = false;
					break;
        }
        if(sz == 1){
					u = v = clauses[i][0];
        }
        else if(sz == 2){
					u = clauses[i][0];
					v = clauses[i][1];
        }
        //printf("clause %d: %d %d\n", i, u, v);
        /*  Each clause is of the form u or v
						1 <= x <= N for an uncomplemented variable x
						-N <= x <= -1 for a complemented variable x
						-x is the complement of a variable x
				*/

    // Internally, complement of variable x is represented as N + x.
        if(u > 0)   {
            if(v > 0)   {
                G[N+u].push_back(v); G[N+v].push_back(u);
                Grev[v].push_back(N+u); Grev[u].push_back(N+v);
            } else  {
                G[N+u].push_back(N-v); G[-v].push_back(u);
                Grev[N-v].push_back(N+u); Grev[u].push_back(-v);
            }
        } else  {
            if(v > 0)   {
                G[-u].push_back(v); G[N+v].push_back(N-u);
                Grev[v].push_back(-u); Grev[N-u].push_back(N+v);
            } else  {
                G[-u].push_back(N-v); G[-v].push_back(N-u);
                Grev[N-v].push_back(-u); Grev[N-u].push_back(-v);
            }
        }
    }
    
    if(!isGoodCase){
			printf("Case #%d: IMPOSSIBLE\n", icase+1);
			continue;
		}
		

    // run dfs on the reverse graph to get reverse postorder
    memset(explored, false, (2*N + 1)*sizeof(bool));
    for(i=2*N; i>0; i--)  {
        if(!explored[i]){
            dfs_reverse(i);
				}
        order[finish[i]] = i;
    }

    // run dfs on the actual graph in reverse postorder
    memset(explored, false, (2*N + 1)*sizeof(bool));
    for(i=2*N; i>0; i--){
        if(!explored[order[i]]) {
            parent = order[i];
            dfs(order[i]);
        }
		}
    for(i=2*N; i>0; i--)   {
        u = order[i];
        if(u > N)   {
            if(stronglyConnected(u, u-N)) break;
            if(truthAssignment.find(leader[u]) == truthAssignment.end())    {
                truthAssignment[leader[u]] = true;
                truthAssignment[leader[u-N]] = false;
            }
        } else {
            if(stronglyConnected(u, N+u)) break;
            if(truthAssignment.find(leader[u]) == truthAssignment.end())    {
                truthAssignment[leader[u]] = true;
                truthAssignment[leader[N+u]] = false;
            }
        }
    }

    if(i > 0){
			printf("Case #%d: IMPOSSIBLE\n", icase+1);
			continue;
    }
    else{
			printf("Case #%d: POSSIBLE\n", icase+1);
			for(int i=0; i<R; i++){
				for(int j=0; j<C; j++){
					if(configs[i][j] != '|' && configs[i][j] != '-'){
						printf("%c", configs[i][j]);
					}
					else{
						int cnum = i*C + j;
						int beamNo = mBeam[cnum];
						if(isMustVH[beamNo] == 1) {
							printf("-");
						}
						else if(isMustVH[beamNo] == 2){
							printf("|");
						}
						else{
							bool isH = truthAssignment[leader[beamNo+1]];
							if(isH) printf("-");
							else printf("|");
 						}
					}
				}
				printf("\n");
			}
		}
		//fprintf(stderr, "case %d/%d\n", icase+1, jcase);
	}
	return 0;
}

