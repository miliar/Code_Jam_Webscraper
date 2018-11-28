/*
Observe that locations of x's and +'s have no influence on each other (apart from if they overlap)
Split original board into one for x's and one for +'s (o becomes x on xboard and + on +board)
Find maximal number of x's or +'s that can be put onto each respectively
Note that maximal number of xboard is always N because you put 1 x in each row
Calculate maximal number of +'s on + board using greedy algorithm (?)
Combine two boards to get final answer
Even if a + and x overlap, it's okay because that means it can be an o, and 1+1pt = 2pt anyway
So, final answer is N+(max # of +'s on +board)


To calculate optimal +board:
Greedy approach where you always choose to put a + where it covers the least squares on its diagonals
*/

#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>

using namespace std;

int xboard[101][101]; //0 if nothing, 1 if x
bool rused[101]; //stores if that row already contains a + from the input
bool cused[101]; //stores if that col already contains a + from the input

int pboard[101][101]; //0 if nothing, 1 if +
int sused[202]; //stores if r+c for diagonal was used
int dused[202]; //stores if r-c for diagonal was used (add N so no index out of bounds error)

char board[101][101]; //input board

void reset(int x){
    for(int i = 1; i <= 2*x+1; i++){
        sused[i] = false;
        dused[i] = false;
    }
    for(int i = 1; i <= x; i++){
        rused[i] = false;
        cused[i] = false;
        for(int j = 1; j <= x; j++){
            xboard[i][j] = 0;
            pboard[i][j] = 0;
            board[i][j] = '.';
        }
    }
}

//x's
void calcX(int N){
    int c = 1;
    for(int r = 1; r <= N; r++){
        if(!rused[r]){
            while(cused[c]){
                c++;
            }
            rused[r] = true;
            cused[c] = true;
            xboard[r][c] = 1;
        }
    }
}

//+'s
struct cell{
    int r;
    int c;
    int nd; //number of squares on diagonals
};

bool cmp(cell a, cell b){
    return a.nd < b.nd;
}

void calcP(int N){
    cell cells[N*N];
    for(int r = 1; r <= N; r++){
        for(int c = 1; c <= N; c++){
            cells[N*(r-1)+(c-1)].r = r;
            cells[N*(r-1)+(c-1)].c = c;
            cells[N*(r-1)+(c-1)].nd = min(r-1,c-1) + min(N-r, c-1) + min(r-1, N-c) + min(N-r, N-c);
        }
    }
    sort(cells, cells+N*N, cmp);

    int row, col;
    for(int i = 0; i < N*N; i++){
        row = cells[i].r;
        col = cells[i].c;
        if(!sused[row+col] && !dused[row-col+N]){
            sused[row+col] = true;
            dused[row-col+N] = true;
            pboard[row][col] = 1;
        }
    }
}

int main(){
    ifstream fin("D-large.in");
    ofstream fout("D-large.out");

    int T; fin >> T;
    for(int t = 1; t <= T; t++){
        fout << "Case #" << t << ": ";
        int N, M; fin >> N >> M;
        reset(N);
        char ic;
        int row, col;
        for(int m = 0; m < M; m++){
            fin >> ic >> row >> col;
            board[row][col] = ic;
            if(ic != 'x'){
                pboard[row][col] = 1;
                sused[row+col] = true;
                dused[row-col+N] = true;
            }
            if(ic != '+'){
                xboard[row][col] = 1;
                rused[row] = true;
                cused[col] = true;
            }
        }
        //calculate xboard
        calcX(N);
        //calculate pboard
        calcP(N);
        //get answer
        int style = 0, newmod = 0;
        bool print = false;
        for(int fr = 1; fr <= N; fr++){
            for(int fc = 1; fc <= N; fc++){
                if(xboard[fr][fc] == 1 && pboard[fr][fc] == 0){
                    style++;
                    if(board[fr][fc] == '.'){
                        newmod++;
                    }
                    if(print){cout << "x ";}
                }else if(xboard[fr][fc] == 0 && pboard[fr][fc] == 1){
                    style++;
                    if(board[fr][fc] == '.'){
                        newmod++;
                    }
                    if(print){cout << "+ ";}
                }else if(xboard[fr][fc] == 1 && pboard[fr][fc] == 1){
                    style+=2;
                    if(board[fr][fc] != 'o'){
                        newmod++;
                    }
                    if(print){cout << "o ";}
                }else{
                    if(print){cout << ". ";}
                }
            }
            if(print){cout << "\n";}
        }

        if(print){cout << "\n";}
        if(print){cout << style << " " << newmod << "\n";}
        //cout << style << " " << newmod << "\n";
        fout << style << " " << newmod << "\n";

        for(int fr = 1; fr <= N; fr++){
            for(int fc = 1; fc <= N; fc++){
                if(xboard[fr][fc] == 1 && pboard[fr][fc] == 0){
                    if(board[fr][fc] == '.'){
                        fout << "x " << fr << " " << fc << "\n";
                    }
                }else if(xboard[fr][fc] == 0 && pboard[fr][fc] == 1){
                    if(board[fr][fc] == '.'){
                        fout << "+ " << fr << " " << fc << "\n";
                    }
                }else if(xboard[fr][fc] == 1 && pboard[fr][fc] == 1){
                    if(board[fr][fc] != 'o'){
                        fout << "o " << fr << " " << fc << "\n";
                    }
                }
            }
        }
    }
    return 0;
}
