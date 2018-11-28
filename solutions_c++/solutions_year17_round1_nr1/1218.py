#include<bits/stdc++.h>
using namespace std;


void fill(vector<string>& grid,  int r1, int r2, int c1, int c2,char what){
   // cout << "Called fill " << r1 << " " << r2 << " " << c1 << " " << c2 << " " << what << endl;
    for(int i=r1;i<=r2;i++)
       for(int j=c1;j<=c2;j++)
          grid[i][j] = what;
}

int main(){

    int T;
    cin >> T;

    for(int t=0;t<T;t++){
        int R,C;
        cin >> R >> C;

        vector<string> grid(R);

        for(int i=0;i<R;i++)
            cin >> grid[i];
        
        vector<pair<int,int> > names(26);
        vector<bool> done (26);

        // for(int i=0;i<R;i++){
        //    for(int j=0;j<C;j++){
        //        char c = grid[i][j];
        //        if (c != '?'){
        //            names[c - 'A'] = make_pair(i,j);
        //        }
        //    }
        // }


        int row_done = 0;
        int next_row = 0;
        while(next_row < R){
            bool processed_row = false;
            for(int j=0;j<C;j++){
                if(grid[next_row][j] != '?' && !done[grid[next_row][j] - 'A']){

                    int Col = 0;
                    char nn, ln;
                    for(int nextc=0; nextc<C; nextc++){
                        nn = grid[next_row][nextc];
                        if (nn != '?' && !done[nn - 'A']){
                            ln = nn;
                            done[nn - 'A'] = true;
                            fill(grid, row_done, next_row, Col, nextc, ln);
                            Col = nextc+1;
                        }
                    }

                    if(Col != C && grid[next_row][Col] == '?'){
                        // have some empty
                        fill(grid, row_done, next_row, Col, C-1, ln);
                    }


                    processed_row = true;
                    next_row++;
                    row_done = next_row;
                    break;
                }
            }

            if(!processed_row)
                next_row++;

        }

        if (row_done != R){
            // have some empty in last row
            int Col = 0;
            char x, xn;
            for(int j=0;j<C;j++){
                x = grid[row_done-1][j];
                if(x != '?'){
                    xn = x;
                    fill(grid, row_done, R-1, Col, j, x);
                    Col = j + 1;
                }
            }
             if(Col != C && grid[row_done][Col] == '?'){
                // have some empty
                  fill(grid, row_done, R-1, Col, C-1, xn);
             }


        }

        cout << "Case #" << t+1 << ": " << endl;
        for(int i=0;i<R;i++){
            for(int j=0;j<C;j++){
                cout << grid[i][j];
            }
            cout << endl;
        }

    }
    return 0;
}  