//
//  main.cpp
//  Codejam2017
//
//  Created by Lavi on 2017-04-08.
//  Copyright © 2017 Lavi. All rights reserved.
//

#include <iostream>
#include <string>
#include <vector>
using namespace std;


int fd(int x, int y, int N){
    return y-x+N-1;
}

int bd(int x, int y){
    return x+y;
}

int main() {
    int T;
    cin >> T;
    for (int t=1;t<=T;t++){
        int N, M;
        cin >> N >> M;
        vector< vector<int> > grid(N, vector<int>(N, 0)) , origgrid(N, vector<int>(N, 0));
        vector<bool> row(N, true), col(N,true);
        vector<bool> fordiag(2*N, true), backdiag(2*N,true);
        
        int points = 0;
        int models_added = 0;
        
        for (int m=0;m<M;m++){
            char s;
            int C, R;
            cin >> s >> R >> C;
            int x = C-1;
            int y = R-1;
            if (s=='x' || s=='o'){
                origgrid[x][y]+=1;
                row[y]=false;
                col[x]=false;
                points++;
            }
            if (s=='+' || s=='o'){
                origgrid[x][y]+=2;
                fordiag[fd(x, y, N)]=false;
                backdiag[bd(x,y)]=false;
                points++;
            }
            grid[x][y]=origgrid[x][y];
        }
        
        
        for (int x=0;x<N;x++){
            for (int y=0;y<N;y++){
                if (row[y] && col[x]){
                    if (grid[x][y]==origgrid[x][y]) models_added++;
                    grid[x][y]+=1;
                    row[y]=false;
                    col[x]=false;
                    points++;
                }
            }
        }
        
        for (int side=0;side<4;side++){
            for (int leng=0;leng<N;leng++){
                int x = side%2==0?(side<2?0:N-1):leng;
                int y = side%2==1?(side<2?0:N-1):leng;
                if (fordiag[fd(x, y, N)] && backdiag[bd(x, y)]){
                    if (grid[x][y]==origgrid[x][y]) models_added++;
                    grid[x][y]+=2;
                    fordiag[fd(x, y, N)] = false;
                    backdiag[bd(x, y)] = false;
                    points++;
                }
            }
        }
        
        /*for (int x=0;x<=N-1;x+=N-1){
            for (int y=0;y<N;y++){
                if (fordiag[fd(x, y, N)] && backdiag[bd(x, y)]){
                    if (grid[x][y]==0) models_added++;
                    grid[x][y]+=2;
                    fordiag[fd(x, y, N)] = false;
                    backdiag[bd(x, y)] = false;
                    points++;
                }
            }
        }*/
        cout << "Case #"<< t << ": " << points << " " << models_added << "\n";
        
        
        for (int x=0;x<N;x++){
            for (int y=0;y<N;y++){
                if (grid[x][y] != origgrid[x][y]){
                    switch (grid[x][y]){
                        case 1:
                            cout << "x";
                            break;
                        case 2:
                            cout << "+";
                            break;
                        case 3:
                            cout << "o";
                            break;
                    }
                    
                    cout << " " << y+1 << " " << x+1 << endl;
                    
                }
            }
        }
        
    }
}
