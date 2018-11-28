#include<iostream>
using namespace std;

int main() {

    int r, c, t;
    cin >> t;
    char a[30][30];
    char ch;
    char pos[30];
    
    for (int k = 0; k < t; k++) {
        cin >> r >> c;
        for (int i = 0; i < r; i++) pos[i] = '.';
        
        for (int i = 0; i < r; i++) {
            for (int j = 0; j < c; j++) {
                cin >> ch;
                a[i][j] = ch;
                if (pos[i] == '.' && ch != '?') pos[i] = a[i][j]; 
            }
        }
        
        for (int i = 0; i < r; i++) {
            ch = pos[i];
            if (ch == '.') continue;
            
            int p = 0;
            while (p < c) {
                if (a[i][p] == '?') a[i][p] = ch;
                else ch = a[i][p];
                p++;
            }
        }
        
        int p = -1;
        
        for (int i = 0; i < r; i++) {
            if (a[i][0] != '?') {
                p = i;
                break;
            }
        } 
        
        for (int i = 0; i < r; i++) {
            if (a[i][0] == '?') {
                for (int j = 0; j < c; j++) a[i][j] = a[p][j];
            }
            else p = i;
        }
        
        cout << "Case #" << k + 1 << ":" << endl;
        for (int i = 0; i < r; i++) {
            for (int j = 0; j < c; j++) {
                cout << a[i][j];
            }
            cout << endl;
        }
        
    }
    
    return 0;
}            
                   
               
          
            
                        
