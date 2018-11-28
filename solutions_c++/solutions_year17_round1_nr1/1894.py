#include <iostream>
#include <vector>
#include <string>
#include <cstdlib>


using namespace std;

void probA(){
    int r, c;
    int t;
    cin >>t;
    for (int l=1; l<=t; l++){
        cin >> r >> c;
        vector <string> v(r);

        for (int i=0; i<r; i++)
            cin>>v[i];

        char curchar = '#';
        // horizontal
        for (int i=0; i<r; i++){

            // forward
            curchar = '#';
            for (int j=0; j<c; j++){

                if (v[i][j] != '?')
                    curchar = v[i][j];
                else if (curchar != '#')
                    v[i][j] = curchar;
            }
            // backward
            curchar = '#';
            for (int j=c-1; j>=0; j--){
                if (v[i][j] != '?')
                    curchar = v[i][j];
                else if (curchar != '#')
                    v[i][j] = curchar;
            }
        }

        // vertical
        for (int j=0; j<c; j++){

            // downward
            curchar = '#';
            for (int i=0; i<r; i++){
                if (v[i][j] != '?')
                    curchar = v[i][j];
                else if (curchar != '#')
                    v[i][j] = curchar;

            }

            //upward
            curchar = '#';
            for (int i=r-1; i>=0; i--){
                if (v[i][j] != '?')
                    curchar = v[i][j];
                else if (curchar != '#')
                    v[i][j] = curchar;

            }
        }

        cout << "Case #" << l << ":\n";

        for (int i=0; i<r; i++)
            cout << v[i] << endl;
    }
}

int main() {
    freopen ("in.txt", "r", stdin);
    freopen ("out.txt", "w", stdout);

    probA();
    return 0;
}