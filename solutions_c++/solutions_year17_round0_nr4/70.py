#include <iostream>
#include <string>
#include <map>
#include <vector>
#include <queue>
#include <stack>
#include <algorithm>

using namespace std;
typedef long long ll;

// (0,0) ....     (0, N)


// (N, 0)

// bipartite matching code borrowed from geeksforgeeks.com

// A DFS based recursive function that returns true if a
// matching for vertex u is possible
bool bpm(vector<vector<bool> > &bpGraph, int u, vector<bool> &seen, vector<int> &matchR, int M, int N)
{
    // Try every job one by one
    for (int v = 0; v < N; v++)
    {
        // If applicant u is interested in job v and v is
        // not visited
        if (bpGraph[u][v] && !seen[v])
        {
            seen[v] = true; // Mark v as visited
 
            // If job 'v' is not assigned to an applicant OR
            // previously assigned applicant for job v (which is matchR[v]) 
            // has an alternate job available. 
            // Since v is marked as visited in the above line, matchR[v] 
            // in the following recursive call will not get job 'v' again
            if (matchR[v] < 0 || bpm(bpGraph, matchR[v], seen, matchR, M, N))
            {
                matchR[v] = u;
                return true;
            }
        }
    }
    return false;
}
 
// Returns maximum number of matching from M to N
vector<int> maxBPM(vector<vector<bool> > &bpGraph, int M, int N)
{
    // An array to keep track of the applicants assigned to
    // jobs. The value of matchR[i] is the applicant number
    // assigned to job i, the value -1 indicates nobody is
    // assigned.
    vector<int> matchR(N, -1);
 
    int result = 0; // Count of jobs assigned to applicants
    for (int u = 0; u < M; u++)
    {
        // Mark all jobs as not seen for next applicant.
        vector<bool> seen(N, false);
 
        // Find if the applicant 'u' can get a job
        bpm(bpGraph, u, seen, matchR, M, N);
    }
    return matchR;
}

string things = ".x+o";

int main(){
    int T;
    cin >> T;
    for(int t=1;t<=T;t++){
        int N, M;
        cin >> N >> M;

        vector<int> brow(N, 0);
        vector<vector<int> > board(N, brow);
        
        vector<bool> row(2*N-1, 0);
        vector<vector<bool> > graph(2*N-1, row); // g[i][j] = 1 iff square where (r+c) ==i and(r-c+N-1)==j
        
        vector<bool> row2(N, true);
        vector<vector<bool> > graph2(N, row2);

        for(int r=0;r<N;r++){
            for(int c=0;c<N;c++){
                graph[r+c][r-c+(N-1)]=true;
                graph2[r][c] = true;
            }
        }

        for(int i=0;i<M;i++){
            char t;
            int r, c;
            cin >> t >> r >> c;
            r--; c--;

            

            if(t=='x' || t=='o'){
                // do something for xs
                board[r][c] += 1;
                for(int j=0;j<N;j++){
                    graph2[r][j] = false;
                    graph2[j][c] = false;
                }
            }
            if(t=='+' || t=='o'){
                // do something for +s 
                board[r][c] += 2;
                for(int j=0;j<2*N-1;j++){
                    graph[r+c][j] = false;
                    graph[j][r-c+(N-1)] = false;
                }
            }
        }
        
        vector<vector<int> > nboard(N, brow);
        for(int r=0;r<N;r++){
            for(int c=0;c<N;c++){
                nboard[r][c] = board[r][c];
            }
        }

        vector<int> diagMatch = maxBPM(graph, 2*N-1, 2*N-1);
        vector<int> plusMatch = maxBPM(graph2, N, N);

        for(int i=0;i<diagMatch.size();i++){
            if(diagMatch[i]>=0){
                int c = (diagMatch[i]-i+(N-1))/2;
                int r = (diagMatch[i]+i-(N-1))/2;
//                cout << "thinking + " << r << " " << c << endl;
                nboard[r][c] |= 2;   
            }
        }
        
        for(int i=0;i<plusMatch.size();i++){
            if(plusMatch[i]>=0){
                int c = i;
                int r = plusMatch[i];
//                cout << "thinking x " << r << " " << c << endl;
                nboard[r][c] |= 1;
            }
        }

        int ans = 0;
        int diffs = 0;
        /*for(int r=0;r<N;r++){
            for(int c=0;c<N;c++){
                cout << things[nboard[r][c]];
            }
            cout << endl;
        }*/
        for(int r=0;r<N;r++){
            for(int c=0;c<N;c++){
                if((nboard[r][c]&2) == 2){
                    ans ++;
                }
                if((nboard[r][c]&1) == 1){
                    ans ++;
                }
                if(nboard[r][c] != board[r][c]){
                    diffs ++;
                }
            }
        }
        cout << "Case #" << t << ": " << ans << " " << diffs << endl;

        for(int r=0;r<N;r++){
            for(int c=0;c<N;c++){
                if(nboard[r][c] != board[r][c]){
                    cout << things[nboard[r][c]] << " " << (r+1) << " " << (c+1) << endl;
                }
            }
        }
    }

    return 0;
}