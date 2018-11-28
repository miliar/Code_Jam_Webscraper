//
//  main.cpp
//  CodeJam
//
//  Created by Vasja Pavlov on 4/8/17.
//  Copyright © 2017 Vasja Pavlov. All rights reserved.
//

#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <cstring>

using namespace std;


//500 253
int rowX[101];
int colX[101];
int rowPlus[101];
int colPlus[101];
int rowO[101];
int colO[101];

int mainDiagonalX[201];
int otherDiagonalX[201];
int mainDiagonalPlus[201];
int otherDiagonalPlus[201];
int mainDiagonalO[201];
int otherDiagonalO[201];

char original[101][101];
char bestMat[101][101];
char mat[101][101];
int n;
int best;

int mainDiag(int r, int c) {
    return n+r-c;
}

int otherDiag(int r, int c) {
    return r+c;
}

bool valid(int r, int c) {
    // return true;
    if(rowX[r] + rowO[r] > 1) return false;
    if(colX[c] + colO[c] > 1) return false;
    int d = mainDiag(r, c);
    if(mainDiagonalO[d] + mainDiagonalPlus[d] > 1) return false;
    d = otherDiag(r, c);
    if(otherDiagonalO[d] + otherDiagonalPlus[d] > 1) return false;
    return true;
}

void add(int r, int c, char x) {
    
    int d = mainDiag(r, c);
    int d2 = otherDiag(r, c);
    
    if(x == 'x') {
        rowX[r]++;
        colX[c]++;
        mainDiagonalX[d]++;
        otherDiagonalX[d2]++;
        
    }
    if(x == '+') {
        rowPlus[r]++;
        colPlus[c]++;
        mainDiagonalPlus[d]++;
        otherDiagonalPlus[d2]++;
    }
    if(x == 'o') {
        rowO[r]++;
        colO[c]++;
        mainDiagonalO[d]++;
        otherDiagonalO[d2]++;
        
    }
}

void printBest() {
    for(int i = 1; i <= n; i++) {
        for(int j = 1; j <= n; j ++){
            cout << bestMat[i][j];
        }
        cout << endl;
    }
    cout << endl;
}


void remove(int r, int c, char x) {
    int d = mainDiag(r, c);
    int d2 = otherDiag(r, c);
    
    if(x == 'x') {
        rowX[r]--;
        colX[c]--;
        mainDiagonalX[d]--;
        otherDiagonalX[d2]--;
        
    }
    if(x == '+') {
        rowPlus[r]--;
        colPlus[c]--;
        mainDiagonalPlus[d]--;
        otherDiagonalPlus[d2]--;
    }
    if(x == 'o') {
        rowO[r]++;
        colO[c]++;
        mainDiagonalO[d]++;
        otherDiagonalO[d2]++;
        
    }
}

void set(int r, int c, char x) {
    char prev = mat[r][c];
    
    if(prev == '.') {
        mat[r][c] = x;
        add(r, c, x);
        if(!valid(r, c)) {
            mat[r][c] = prev;
            remove(r,c, x);
        }
        return;
    }
    
    if((prev == 'x' || prev == '+') && x == 'o') {
        mat[r][c] = x;
        add(r,c,x);
        remove(r,c,prev);
        if(!valid(r,c)) {
            mat[r][c] = prev;
            remove(r,c,x);
            add(r,c,prev);
        }
    }
    
}



void printMat() {
    for(int i = 1; i <= n; i++)
    {
        for(int j = 1; j <= n;j ++) {
            cout <<mat[i][j];
        }
        cout << endl;
    }
    cout << endl;
}
void precompute() {
    
    
    set(n,1,'o');
    
    for(int i = n-1; i > 1; i--) {
        set(i,1,'+');
    }
    
    //  printMat();
    set(1,n,'x');
    
    
    
    for(int i = 2; i <= n; i++) {
        set(i,n,'+');
    }
    
    int i = n-1;
    int j = 2;
    while(i > 1) {
        set(i,j,'x');
        i--;
        j++;
    }
}

void gen(int r, int c, int score) {
    
    //  cout << r << " " << c << endl;
    if(r == n+1) {
        //        if(score == 10) {
        //            for(int i = 1; i <= n; i++) {
        //                for(int j = 1; j <= n; j++) {
        //                    cout << mat[i][j];
        //                }
        //                cout << endl;
        //            }
        //            cout << endl;
        //        }
        
        if(score > best) {
            best = score;
            for(int i = 1; i <= n; i++)
                for(int j = 1; j <= n; j++) {
                    bestMat[i][j] = mat[i][j];
                }
        }
       // if(score == best && score == 13) printMat();
        
        return;
    }
    
    int nexti = r;
    int nextj = c;
    nextj++;
    if(nextj == n+1) {
        nextj = 1;
        nexti++;
    }
    
    int d,d2;
    d = mainDiag(r, c);
    d2 = otherDiag(r, c);
    char prev = mat[r][c];
    if(mat[r][c] == '.') {
        gen(nexti, nextj, score);
        
        
        
        rowX[r]++;
        colX[c]++;
        mainDiagonalX[d]++;
        otherDiagonalX[d2]++;
        mat[r][c] = 'x';
        if(valid(r,c)) gen(nexti, nextj, score + 1);
        rowX[r]--;
        colX[c]--;
        mainDiagonalX[d]--;
        otherDiagonalX[d2]--;
        
        rowPlus[r]++;
        colPlus[c]++;
        mainDiagonalPlus[d]++;
        otherDiagonalPlus[d2]++;
        mat[r][c] = '+';
        if(valid(r,c)) gen(nexti, nextj, score + 1);
        rowPlus[r]--;
        colPlus[c]--;
        mainDiagonalPlus[d]--;
        otherDiagonalPlus[d2]--;
        
        rowO[r]++;
        colO[c]++;
        mainDiagonalO[d]++;
        otherDiagonalO[d2]++;
        mat[r][c] = 'o';
        if(valid(r,c)) gen(nexti, nextj, score + 2);
        rowO[r]--;
        colO[c]--;
        mainDiagonalO[d]--;
        otherDiagonalO[d2]--;
    }
    else if(mat[r][c] == 'o') {
        gen(nexti, nextj, score);
    } else if(mat[r][c] == 'x' || mat[r][c] == '+'){ //x or +
        gen(nexti,nextj,score);
        rowO[r]++;
        colO[c]++;
        mainDiagonalO[d]++;
        otherDiagonalO[d2]++;
        if(prev == 'x') {
            rowX[r]--;
            colX[c]--;
            mainDiagonalX[d]--;
            otherDiagonalX[d2]--;
            
        }
        if(prev=='+') {
            rowPlus[r]--;
            colPlus[c]--;
            mainDiagonalPlus[d]--;
            otherDiagonalPlus[d2]--;
        }
        mat[r][c] = 'o';
        if(valid(r,c))
            gen(nexti,nextj,score+1);
        rowO[r]--;
        colO[c]--;
        mainDiagonalO[d]--;
        otherDiagonalO[d2]--;
        if(prev == 'x') {
            rowX[r]++;
            colX[c]++;
            mainDiagonalX[d]++;
            otherDiagonalX[d2]++;
            
        }
        if(prev=='+') {
            rowPlus[r]++;
            colPlus[c]++;
            mainDiagonalPlus[d]++;
            otherDiagonalPlus[d2]++;
        }
        
    }
    
    mat[r][c] = prev;
}

int solveSmall(int caseNum) {
    vector<char> added;
    vector<int> posi, posj;
    
    int x = 0,p = 0,o = 0;
    
    for(int j = 1; j <= n; j++) {
        if(mat[1][j] == 'x') x++;
        if(mat[1][j] == '+') p++;
        if(mat[1][j] == 'o') o++;
    }
    if(x == 0 && o == 0) {
        mat[1][1] = 'o';
        for(int j = 2; j<=n;j++) mat[1][j] = '+';
        for(int i = 2, j = 2; i <= n; i++,j++) {
            mat[i][j] = 'x';
        }
        for(int j = 1; j < n; j++) {
            mat[n][j] = '+';
        }
        mat[n][1] = '.';
    }
    
    int row = 1,col = 0;
    if(o == 1 || x== 1) { //case xxxxoxxxxx
        if(x == 1) {
            for(int j = 1; j <= n; j++) {
                if(mat[1][j] == 'x') mat[1][j] = 'o';
            }
        }
        for(int j = 1; j <= n;j++) mat[n][j] = '+';
        for(int j = 1; j <= n; j++) {
            if(mat[1][j] == 'o') col = j;
            if(mat[1][j] == '.') mat[1][j] = '+';
        }
        
        if(col > n - col) {
            for(int i = row+1, j = col-1; i <= n && j >= 1; i++, j--) {
                mat[i][j] = 'x';
            }
            for(int i = col + 1, j = col+1; i <= n && j<=n; i++, j++) {
                mat[i][j] = 'x';
            }
        } else {
            
            for(int i = row+1, j = col+1; i <= n && j <= n; i++, j++) {
                mat[i][j] = 'x';
            }
            
            for(int i = n-col + 2, j = col-1; i <= n && j>= 1; i++, j--) {
                mat[i][j] = 'x';
            }
        }
        
        if(n > 1 && mat[1][1] == mat[n][n]) mat[n][n] = '.';
        if(n > 1 && mat[1][n] == mat[n][1]) mat[n][1] = '.';
        
    }
    
    row = 1;
    if(false && x == 1) {
        for(int j = 1; j<= n; j++) {
            if(mat[1][j] == '.') mat[1][j] = '+';
            if(mat[1][j] == 'x') col = j;
        }
        
        
        
        bool placedO = false;
        bool busy[101] = {0};
        busy[col] = true;
        if(col == 1) {
            mat[n][n] = 'o';
            busy[n] = true;
            placedO = true;
        } else
            if(col == n) {
                mat[n][1] = 'o';
                busy[1] = true;
                placedO = true;
            }
        //        for(int j = 2; j <= n; j++) {
        //            if(!busy[j]) {
        //                busy[j] = true;
        //                mat[n][j] = 'x';
        //                break;
        //            }
        //        }
        
        for(int i = 2; i <= n; i++) {
            for(int j = 1; j <= n; j++) {
                if(!busy[j]) {
                    busy[j] = true;
                    mat[i][j] = 'x';
                    break;
                }
            }
        }
        
        for(int j = 1; j < n; j++) {
            if(mat[n][j] != 'o') mat[n][j] = '+';
        }
        
        for(int j = 1; j <= n; j++) if(mat[n][j] == 'x' && !placedO) {mat[n][j] = 'o'; placedO = true;}
        
        if(mat[1][1] == mat[n][n]) mat[n][n] = '.';
        if(mat[1][n] == mat[n][1]) mat[n][1] = '.';
    }
    
    int res = 0;
    
    for(int i = 1; i <= n; i++)
        for(int j = 1; j <= n; j++) {
            if(mat[i][j] == 'o') res+=2;
            if(mat[i][j] == '+') res++;
            if(mat[i][j] == 'x') res++;
        }
//    if(n < 50)
   // printMat();
    return res;
    
    
}



int bruteForce() {
    int r = 0;
    for(int i = 1; i <= n; i++) {
        for(int j = 1; j <= n; j ++)
        {
            char c = mat[i][j];
            if(c == 'x' || c == '+') r++;
            if(c == 'o') r+=2;
            bestMat[i][j] = mat[i][j];
            
        }
    }
    
    best = r;
    gen(1,1,r);
    printBest();
    return best;
}


void doValidation() {
    for(int i = 1; i <= n; i++)
        for(int j = 1; j<= n; j++) {
            set(i, j, mat[i][j]);
        }
    
    for(int i = 1; i <= n; i++)
        for(int j = 1; j<= n; j++) {
            if(!valid(i,j)) {cout << "ERROR" << endl;
                while(1);}
        }

}

int main(int argc, const char * argv[]) {
    
    ifstream cin ("input.txt");
    ofstream cout ("output.txt");
    
    int t, caseNum = 1;
    char c;
    int ii,jj;
    
    cin >> t;
    
    int m;
    while(t--) {
        //   printf("test %d\n", t);
        memset(rowX,0,sizeof(rowX));
        memset(rowPlus,0,sizeof(rowPlus));
        memset(rowO,0,sizeof(rowO));
        memset(colX,0,sizeof(colX));
        memset(colPlus,0,sizeof(colPlus));
        memset(colO,0,sizeof(colO));
        
        memset(mainDiagonalX,0,sizeof(mainDiagonalX));
        memset(mainDiagonalPlus,0,sizeof(mainDiagonalPlus));
        memset(mainDiagonalO,0,sizeof(mainDiagonalO));
        memset(otherDiagonalX,0,sizeof(otherDiagonalX));
        memset(otherDiagonalPlus,0,sizeof(otherDiagonalPlus));
        memset(otherDiagonalO,0,sizeof(otherDiagonalO));
        
        cin >> n >> m;
        
        for(int i = 1; i <= n; i++) {
            for(int j = 1; j <= n; j++) {
                mat[i][j] = '.';
            }
        }
        
        
        for(int i = 0; i < m; i++) {
            cin >> c >> ii >> jj;
            set(ii,jj,c);
        }
        
        
        int r = 0;
        for(int i = 1; i <= n; i++)
            for(int j = 1; j <= n; j ++)
            {
                original[i][j] = mat[i][j];
            }
        
        
        
        //            int r1 = bruteForce();
//        int r2 = solveSmall(caseNum);
        
        
        //            if(r1 != r2) {
        //                cout << "Case #" << caseNum << ":\n";
        //                cout << "bruteForce() " << r1 << endl;
        //                cout << "solveSmall()" << r2 << endl;
        //                cout << endl << endl;
        //            }
        
        
        //        if( n > 3) {
        //            solveSmall(caseNum);
        //
        //            for(int i = 1; i <= n; i++) {
        //                for(int j = 1; j <= n; j++)
        //                bestMat[i][j] = mat[i][j];
        //            }
        //        } else {
        //
        //        }
        
        //        best = 0;
        
        if(n < 4) {
            
            r = bruteForce();
        } else {
            r = solveSmall(caseNum);
            for(int i = 1; i <= n; i++) {
                for(int j = 1; j <= n; j++)
                    bestMat[i][j] = mat[i][j];
            }
        }
        
        
     //   doValidation();
        
        cout << "Case #"<<caseNum << ": " << r << " ";
        vector<char> added;
        vector<int> posi, posj;
        
        for(int i = 1; i <= n; i++) {
            for(int j = 1; j <= n; j ++) {
                if(bestMat[i][j] != original[i][j]) {
                    added.push_back(bestMat[i][j]);
                    posi.push_back(i);
                    posj.push_back(j);
                }
            }
        }
        cout << added.size() << endl;
        for(int i = 0; i < added.size(); i++) {
            cout << added[i] << " " << posi[i] << " " << posj[i] << endl;
        }
        
        //        for(int i = 1; i <= n; i++) {
        //            for(int j = 1; j <= n; j++) {
        //                cout << bestMat[i][j];
        //            }
        //            cout << endl;
        //        }
        //        cout << "------------------\n";
        
        
        
        caseNum++;
    }
    return 0;
}
