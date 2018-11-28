#include <iostream>
#include <stdio.h>

using namespace std;

int main()
{
    int t;
    cin >> t;
    for (int k = 1; k <= t; k++){
        string position;
        int length;
        cin >> position >> length;
        int n = 0;
        for(int i=0; i < position.size() - length + 1; i++ ){
            if (position[i] == '-'){
                for (int j = i; j < i+length; j++){
                    if (position[j] == '-')
                        position[j] = '+';
                    else
                        position[j] = '-';
                }
            n ++;
            }
        }
        bool ok = true;
        for(int i=0; i < position.size(); i++ ){
            if (position[i] == '-'){
                cout << "Case #" << k << ": " << "IMPOSSIBLE" << endl;
                ok = false;
                break;
            }

        }
        if (ok){
            cout << "Case #" << k << ": " << n << endl;
        }
    }
    return 0;
}
