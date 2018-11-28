#include <iostream>
#include <vector>
#include <algorithm>

#include <limits>
using namespace std; 
 
int main(int argc, char *argv[]) { 
	
    int tests;
    cin >> tests;
    
    for (int t = 1; t <= tests; t++) {
        int R, C;
        cin >> R >> C;
        cin.ignore(numeric_limits<streamsize>::max(), '\n');
        char** cake = new char*[R];
        for(int i = 0; i < R; i++) {
            cake[i] = new char[C];
            for(int j = 0; j < C; j++) {
                cake[i][j] = cin.get();
            }
            cin.ignore(numeric_limits<streamsize>::max(), '\n');
        }
        vector<char> seen;
        for(int i = 0; i < R; i++) {
            for(int j = 0; j < C; j++) {
                if (cake[i][j] != '?') {
                    if(std::find(seen.begin(), seen.end(), cake[i][j]) != seen.end()) continue;
                    int l = 0, r = 0;
                    seen.push_back(cake[i][j]);
                    for(int k = j+1; k < C; k++) {
                        if(cake[i][k] != '?') break;
                        cake[i][k] = cake[i][j];
                        r++;
                    }
                    for(int k = j-1; k >= 0; k--) {
                        if(cake[i][k] != '?') break;
                        cake[i][k] = cake[i][j];
                        l++;
                    }
                    for(int k = i-1; k >= 0; k--) {
                        bool should_break = false;
                        for (int p = j-l; p <= j+r; p++) {
                            if(cake[k][p] != '?') should_break = true;
                        }
                        if(should_break) break;
                        for (int p = j-l; p <= j+r; p++) {
                            cake[k][p] = cake[i][j];
                        }
                    }
                    for(int k = i+1; k < R; k++) {
                        bool should_break = false;
                        for (int p = j-l; p <= j+r; p++) {
                            if(cake[k][p] != '?') should_break = true;
                        }
                        if(should_break) break;
                        for (int p = j-l; p <= j+r; p++) {
                            cake[k][p] = cake[i][j];
                        }
                    }
                }
            }
        }
        
        
        cout << "Case #" << t << ":" << endl;
        for(int i = 0; i < R; i++) {
            for(int j = 0; j < C; j++) {
                cout << cake[i][j];
            }
            cout << endl;
        }
        
        for (int i = 0; i < R; i++) {
            delete[] cake[i];
        }
        delete[] cake;
    }
    
    
	return 0; 
} 
