//#include<iostream>
#include<cstdio>
#include<algorithm>
#include<vector>
#include<set>
#include<map>
#include<functional>
#include<string>
#include<cstring>
#include<cstdlib>
#include<queue>
#include<utility>
#include<fstream>
#include<sstream>
#include<cmath>
#include<stack>
#include<iterator>
#include<unordered_map>
#include<unordered_set>
#include<assert.h>

using namespace std;

typedef vector<int> VI;
typedef vector<VI> VVI;

ifstream cin("/Users/naginahas/Downloads/D-Large.in");
ofstream cout("/Users/naginahas/Downloads/Dqqqqq.txt");

// This code performs maximum bipartite matching.
//
// Running time: O(|E| |V|) -- often much faster in practice
//
//   INPUT: w[i][j] = edge between row node i and column node j
//   OUTPUT: mr[i] = assignment for row node i, -1 if unassigned
//           mc[j] = assignment for column node j, -1 if unassigned
//           function returns number of matches made
//ifstream cin("/Users/naginahas/Downloads/D-small-attempt0.in");
//ofstream cout("/Users/naginahas/Downloads/Dzzzzz.txt");
bool FindMatch(int i, const VVI &w, VI &mr, VI &mc, VI &seen) {
    for (int j = 0; j < w[i].size(); j++) {
        if (w[i][j] && !seen[j]) {
            seen[j] = true;
            if (mc[j] < 0 || FindMatch(mc[j], w, mr, mc, seen)) {
                mr[i] = j;
                mc[j] = i;
                return true;
            }
        }
    }
    return false;
}

int BipartiteMatching(const VVI &w, VI &mr, VI &mc) {
    mr = VI(w.size(), -1);
    mc = VI(w[0].size(), -1);
    
    int ct = 0;
    for (int i = 0; i < w.size(); i++) {
        VI seen(w[0].size());
        if (FindMatch(i, w, mr, mc, seen)) ct++;
    }
    return ct;
}

int main(int argc, const char * argv[]) {
    
    int T;
    cin >> T;
    for(int t=0;t<T;t++){
        int N, M;
        cin >> N >> M;
        vector <vector <int> > grid;
        vector <vector <int> > gridplus;
        vector <vector <int> > gridcross;
        
        grid.assign(N,vector <int> (N,0) );
        gridplus.assign(N,vector <int> (N,0) );
        gridcross.assign(N,vector <int> (N,0) );

        for(int k=0;k<M;k++){
            int i,j;
            char c;
            cin >> c >> i >> j ;
            i--;j--;
            grid[i][j] = c;
            if(c=='+') gridplus[i][j] =1;
            if(c=='x') gridcross[i][j] =1;
            if(c=='o') gridplus[i][j] = gridcross[i][j] = 1;
            
        }
        //first solve problem for x's
        vector <vector <int> > bpm;
        bpm.assign(N,vector <int> (N,0) );
        vector <int> availcols(N,1);
        vector <int> availrows(N,1);
        
        for(int i=0;i<N;i++){
            for(int j=0;j<N;j++){
                if(grid[i][j] == 'o' || grid[i][j] == 'x'){
                    availrows[i] = 0;
                    availcols[j] = 0;
                }
            }
        }
        for(int i=0;i<N;i++){
            for(int j=0;j<N;j++){
                if(availrows[i]==1 && availcols[j]==1)
                    bpm[i][j] = 1;
            }
        }
        vector <int> mr, mc;
        BipartiteMatching(bpm, mr,mc);
        for(int i=0;i<mr.size();i++){
            if(mr[i]!=-1)
                gridcross[i][mr[i]] = 1;
        }
        bpm.assign(2*N-1,vector <int> (2*N-1,0) );
        vector <int> availdif(2*N-1,1);
        vector <int> availsum(2*N-1,1);
        for(int i=0;i<N;i++){
            for(int j=0;j<N;j++){
                if(grid[i][j] == 'o' || grid[i][j] == '+'){
                    availdif[i-j+N-1] = 0;
                    availsum[j+i] = 0;
                }

            }
        }
        for(int i=0;i<2*N-1;i++){
            for(int j=0;j<2*N-1;j++){
                if(availdif[i] !=0 && availsum[j]!=0){
                    //i is the dif, what to do
                    
                    int dif = i-N+1;
                    if((dif+2000)%2!=j%2) continue;
                    int row = (dif+j)/2;
                    int col = (j-row);
                    if( row>=0 &&  row < N && col>=0 && col <N)
                        bpm[i][j] = 1;
                }
                
            }
        }
        BipartiteMatching(bpm, mr,mc);
        for(int i=0;i<mr.size();i++){
            if(mr[i]!=-1){
                int row = (i-N+1+mr[i])/2;
                int col = mr[i] - row;
                gridplus[row][col] = 1;
            }
        }
        /*
         For each test case, first output one line containing Case #x: y z,
         where x is the test case number (starting from 1), y is the number of 
         style points earned in your arrangement, and z is the total number 
         of models you have added and/or substituted in. */
        int z = 0;
        int y = 0;
        for(int i=0;i<N;i++){
            for(int j=0;j<N;j++){
                y+= (gridplus[i][j] + gridcross[i][j]);
                int q =0;
                if(grid[i][j] =='o') q = 2;
                else if (grid[i][j]!=0) q =1;
                if(gridplus[i][j] + gridcross[i][j]!=q) z++;
            }
        }
        cout << "Case #" << t+1 << ": " << y << " " << z << endl;
        for(int i=0;i<N;i++){
            for(int j=0;j<N;j++){
               
                int q =0;
                if(grid[i][j] =='o') q = 2;
                else if (grid[i][j]!=0) q =1;
                if(gridplus[i][j] + gridcross[i][j]!=q){
                    
                    if(gridplus[i][j] + gridcross[i][j] == 2){
                        cout << "o " ;
                    }
                    else if(gridplus[i][j]==1) cout << "+ " ;
                    else cout << "x " ;
                    cout << i+1 << " " << j+1 << endl;;
                }
            }
        }
        
        
        
    }
    return 0;
}
