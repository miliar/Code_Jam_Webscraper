#include <iostream>
#include <algorithm>
#include <string>

using namespace std ;
#define PB push_back
#define MP make_pair
typedef unsigned long long int llu;
typedef long long int ll;

int main() {

    llu t;
    cin >> t;
    
    for (llu num = 1; num <= t; num++) {
        cout << "Case #"<<num<<":" << endl;

        llu r, c;
        string a[100];
        cin >> r >> c;
        
        for (int i = 0; i < r; i++) {
            cin >> a[i];
            char last = a[i][0];
            for (int j = 0; j < c; j++) {
                if (a[i][j] != '?') {
                    last = a[i][j];
                    for (int l = j-1; l >= 0; l--) 
                        if (a[i][l] == '?')
                            a[i][l] = a[i][j];
                }
            }
            if (a[i][c-1] == '?' && last != '?') {
                     for (int l = c-1; l >= 0; l--) 
                        if (a[i][l] == '?')
                            a[i][l] = last;
                
            }
            
            if (a[i][0] == '?' && i > 0) {
                for (int j = 0; j < c; j++)
                    a[i][j] = a[i-1][j];
            }
       // cout << a[i] << endl; 
        }

        if (a[0][0] == '?') {
            for (int i = 0; i < r; i++) {
                if (a[i][0] != '?') {
               //     cout << a[i][0]<<endl;
                    for (int l = i-1; l>= 0; l--)
                        for (int k = 0; k < c; k++)
                            a[l][k] = a[l+1][k];
                    break;
                }
                
            }
        }    
    
        for (int i = 0; i < r; i++)
            cout << a[i]<< endl;
    
    }
}
