#include <cstring>
#include <cstdio>
#include <fstream>
#include <cstdlib>
#include <vector>
#include <iostream>
#include <string>
#include <queue>
#include <algorithm>
//#include <iostream>

using namespace std;


struct rect {
    int i1,j1,i2,j2;
    rect(){i1=j1=i2=j2 = -1; }
    rect(int _i1, int _j1, int _i2, int _j2) {
        i1 = _i1;
        j1 = _j1;
        i2 = _j2;
        j2 = _j2;
    }
};

rect v[26];

int main()
{
    
    ifstream cin("input.txt");
    ofstream cout("izlez.txt");
    int t;
    cin >> t;
    int r,c;
    string grid[26], s;
    int testCount = 1;
    
    while(t--) {
        for(int i = 0; i < 26; i++) {
            v[i] = rect();
        }
        cin >> r >> c;
        for(int i = 0; i < r; i++) {
            cin >> s;
            grid[i] = s;
        }
        
        for(char x = 'A'; x <= 'Z'; x++) {
            int pos = x-'A';
            for(int i = 0; i < r; i++) {
                for(int j = 0; j < c; j++) {
                    if(grid[i][j] == x) {
                        if(v[pos].i1 == -1) {
                            v[pos].i1 = v[pos].i2 = i;
                            v[pos].j1 = v[pos].j2 = j;
                        } else {
                            v[pos].i1 = min(v[pos].i1,i);
                            v[pos].j1 = min(v[pos].j1,j);
                            
                            v[pos].i2 = max(v[pos].i2,i);
                            v[pos].j2 = max(v[pos].j2,i);
                        }
                    }
                }
            }
        }
        
        queue<rect> q;
        for(char x = 'A'; x <= 'Z'; x++) {
            int pos = x-'A';
            if(v[pos].i1 == -1) continue;
            
            q.push(v[pos]);
            for(int i = v[pos].i1; i <= v[pos].i2; i++)
                for(int j = v[pos].j1; j <= v[pos].j2; j++) {
                    grid[i][j] = x;
                }
        }
        

        
        while(!q.empty()) {
            rect tmp2 = q.front();
            rect tmp = v[grid[tmp2.i1][tmp2.j1]-'A'];
            
//            for(int i = 0; i < r; i++) {
//                for(int j = 0; j < c; j++) {
//                    cout << grid[i][j];
//                }
//                cout << endl;
//            }cout << endl;
            q.pop();
            int ii,jj;
            bool chk;
            
            ///////
            chk = true;
            ii = tmp.i1-1;
            for(int j = tmp.j1; j <= tmp.j2; j++) {
                if(ii >= 0 &&  grid[ii][j] == '?') {} else chk = false;
            }
            if(chk) {
                for(int j = tmp.j1; j <= tmp.j2; j++) {
                    grid[ii][j] = grid[tmp.i1][j];
                }
                v[grid[tmp2.i1][tmp2.j1]-'A'].i1--;
                tmp.i1--;
                q.push(tmp);
            }
            
            ///////
            chk = true;
            ii = tmp.i2+1;
            for(int j = tmp.j1; j <= tmp.j2; j++) {
                if(ii < r &&  grid[ii][j] == '?') {} else chk = false;
            }
            if(chk) {
                for(int j = tmp.j1; j <= tmp.j2; j++) {
                    grid[ii][j] = grid[tmp.i2][j];
                }
                v[grid[tmp2.i1][tmp2.j1]-'A'].i2++;
                tmp.i2++;
                q.push(tmp);
            }
            
            ///////
            chk = true;
            jj = tmp.j1-1;
            for(int i = tmp.i1; i <= tmp.i2; i++) {
                if(jj >= 0 &&  grid[i][jj] == '?') {} else chk = false;
            }
            if(chk) {
                for(int i = tmp.i1; i <= tmp.i2; i++) {

                    grid[i][jj] = grid[i][tmp.j1];
                }
                v[grid[tmp2.i1][tmp2.j1]-'A'].j1--;
                tmp.j1--;
                q.push(tmp);
            }
            
            chk = true;
            jj = tmp.j2 + 1;
            for(int i = tmp.i1; i <= tmp.i2; i++) {
                if(jj < c &&  grid[i][jj] == '?') {} else chk = false;
            }
            if(chk) {
                for(int i = tmp.i1; i <= tmp.i2; i++) {
                    
                    grid[i][jj] = grid[i][tmp.j2];
                }
                v[grid[tmp2.i1][tmp2.j1]-'A'].j2++;
                tmp.j2++;
                q.push(tmp);
            }

            
        }
        cout << "Case #" <<testCount << ":\n";
        for(int i = 0; i < r; i++) {
            for(int j = 0; j < c; j++) {
                cout << grid[i][j];
            }
            cout << endl;
        }
        
        testCount++;
    }
    
    
    return 0;
}
