#include <iostream>
#include <vector>
#include <string>
using namespace std;

void fill(char val, vector<string> &S, int r, int c, int r0, int c0){
    for(int i=r0;i<=r;++i){
        for(int j=c0;j<=c;++j){
            S[i][j] = val;
        }
    }
}

void solve(vector<string> &S){
    int n = S.size();
    int m = S[0].size();
    int next_row = 0;
    for(int i=0;i<n;++i){
        int next_col = 0;
        char last_val = '?';
        for(int j=0;j<m;++j){
            if(S[i][j]=='?'){
                continue;
            }
            last_val = S[i][j];
            fill(last_val, S, i, j, next_row, next_col);
            next_col = j+1;
        }
        if(last_val!='?'){
            fill(last_val, S, i, m-1, next_row, next_col);
            next_row = i+1;
        }
    }
    
    for(int j=0;j<m;++j){
        char val = S[next_row-1][j];
        for(int i=next_row; i<n; ++i){
            S[i][j] = val;
        }
    }
    
}


int main(){

    int T;
    cin>>T;
    for(int t=1;t<=T;++t){
        vector<string> S;
        int R, C;
        cin>>R>>C;
        for(int i=0;i<R;++i){
            string s;
            cin>>s;
            S.push_back(s);
        }
        
        solve(S);
        
        cout<<"Case #"<<t<<":"<<endl;
        for(int i=0;i<R;++i){
            cout<<S[i]<<endl;
        }
        
    }
    return 0;
}

