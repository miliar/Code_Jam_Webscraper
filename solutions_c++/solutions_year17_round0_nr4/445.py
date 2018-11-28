#include<bits/stdc++.h>
using namespace std;



int solver(int n, vector<vector<bool> >& board) {
    vector<bool> freecols(n,true);
    vector<bool> freerows(n,true);
    for(int i=0;i<n;i++) for(int j=0;j<n;j++) if(board[i][j]) freerows[i]=freecols[j]=false;
    queue<int> cols;
    for(int i=0;i<n;i++) if(freecols[i]) cols.push(i);
    int up = 0;
    for(int i=0;i<n;i++) {
        if(!freerows[i]) continue;
        int c = cols.front();
        cols.pop();
        board[i][c] = true;
        up++;
    }
    return up;    
}

int pairCount(unordered_set<int>& A, unordered_set<int>& B, vector<vector<bool>>& board, vector<pair<int,int> >& p, bool set) {
    unordered_set<int> _A;
    unordered_set<int> _B;
    int count = 0;
    for(auto point : p) {
        int r,c;
        tie(r,c) = point;
        if(A.count(r+c) || B.count(r-c) || _A.count(r+c) || _B.count(r-c)) continue;
        _A.insert(r+c);
        _B.insert(r-c);
        count++;
        if(set) {
            A.insert(r+c);
            B.insert(r-c);
            board[r][c] = true;
        }
    }
    return count;
}

int solveb(int n, vector<vector<bool>>& board) {
    int up = 0;
    unordered_set<int> A,B;
    for(int i=0;i<n;i++) {
        for(int j=0;j<n;j++) {
            if(!board[i][j]) continue;
            A.insert(i+j);
            B.insert(i-j);
        }
    }
    
    for(int i=0;i<n;i++) {
        vector<vector<pair<int,int> >> points = {{ {i,0}, {n-1-i,n-1}}, { {0,i},{n-1,n-1-i}}};
        up += max(pairCount(A,B,board,points[0],false),pairCount(A,B,board,points[1],false));
        if(pairCount(A,B,board,points[0],false) > pairCount(A,B,board,points[1],false)) pairCount(A,B,board,points[0],true);
        else pairCount(A,B,board,points[1],true);
    }
    return up;

}


void f() {
    int n,m;
    cin>>n>>m;
    vector<vector<bool> > bishops(n, vector<bool>(n, false));
    vector<vector<bool> > rooks(n, vector<bool>(n, false));
    vector<vector<char> > all(n, vector<char>(n, '.'));
    vector<vector<char> > res(n, vector<char>(n, '.'));
    int points = 0;
    int upg = 0;
    for(int i=0;i<m;i++) {
        char c;
        int x,y;
        cin>>c>>x>>y;
        x--;y--;
        if(c=='o' || c=='+') {
            points++;
            bishops[x][y] = true;
        }
        if(c=='o' || c=='x') {
            points++;
            rooks[x][y] = true;
        }
        all[x][y] = c;

    }
    points += solveb(n,bishops);
    points += solver(n,rooks);

    for(int i=0;i<n;i++) for(int j=0;j<n;j++) {
        if(bishops[i][j] && rooks[i][j]) res[i][j]='o';
        else if(bishops[i][j]) res[i][j] = '+';
        else if(rooks[i][j]) res[i][j] = 'x';
    }
    for(int i=0;i<n;i++) for(int j=0;j<n;j++) if(all[i][j] != res[i][j]) upg++;
    cout<<points<<" "<<upg<<endl;

    for(int i=0;i<n;i++) for(int j=0;j<n;j++) if(res[i][j] != all[i][j]) cout<<res[i][j]<<" "<<(i+1)<<" "<<(j+1)<<endl;

 //  for(int i=0;i<n;i++) { for(int j=0;j<n;j++) {cout<<res[i][j];}cout<<endl;}
}

int main() {
    int t;
    cin>>t;
    for(int i=1;i<=t;i++) {
        cout<<"Case #"<<i<<": ";
        f();
    }
}
