#include <vector>
#include <iostream>

using namespace std;

vector<vector<char>> src, out;
int n;

int countScore(){
    int count = 0;
    for(auto &v : out){
        for(auto c : v){
            if(c == '+' || c == 'x')
                ++count;
            else if(c == 'o')
                count += 2;
        }
    }
    return count;
}

int countChanged(){
    int count = 0;
    for(int i=0; i<n; ++i){
        for(int j=0; j<n; ++j){
            if(src[i][j] != out[i][j]){
                ++count;
            }
        }
    }
    return count;
}

void printChanged(){
    for(int i=0; i<n; ++i){
        for(int j=0; j<n; ++j){
            if(src[i][j] != out[i][j]){
                cout << out[i][j] << " " << (i+1) << " " << (j+1) << endl;
            }
        }
    }
}

void comp(int tc){
    int m;
    cin >> n >> m;
    src.assign(n, vector<char>(n, '.'));
    out.assign(n, vector<char>(n, '.'));
    
    int oj = -1;
    
    for(int i=0; i<m; ++i){
        int r, c;
        char cell;
        cin >> cell >> r >> c;
        src[--r][--c] = cell;
        if(cell != '+'){
            oj = c;
        }
    }
    
    if(n == 1){
        out[0][0] = 'o';
    } else{
        bool mirror = false;
        if(oj == -1)
            oj = n-1;
        else if(oj == 0){
            oj = n-1;
            mirror = true;
        }
        
        out[0].assign(n, '+');
        out[0][oj] = 'o';
        out[n-1].assign(n, '+');
        out[n-1][0] = 'x';
        out[n-1][n-1] = '.';
        
        for(int i=n-2, j=1; i>0; --i, ++j){
            if(j == oj)
                ++j;
            out[i][j] = 'x';
        }
        
        if(mirror){
            for(auto &v : out){
                reverse(v.begin(), v.end());
            }
        }
    }
    
    cout << "Case #" << tc << ": " << countScore() << " " << countChanged() << endl;
    printChanged();
}

int main(){
    int T;
    cin >> T;
    for(int tc=1; tc<=T; ++tc){
        comp(tc);
    }
}
