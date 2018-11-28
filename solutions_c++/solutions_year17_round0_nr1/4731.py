#include <iostream>
#include <string>

using namespace std;

int main()
{
    int t;
    cin >> t;
    for (int i = 1; i <= t; i++){
        int k,c;
        c = 0;
        string s;
        string comp = "-+";
        cin >> s >> k;
        for (int x = 0; x < s.size()-k+1; x++){
            if (s[x] == comp[0]){
                for (int y = 0; y < k; y++){
                    if (s[x+y] == comp[0]){
                        s[x+y] = comp[1];
                    }
                    else{
                        s[x+y] = comp[0];
                    }
                }
                c++;
            }
        }
        int b = 1;
        for (int x = s.size()-k+1; x < s.size(); x++){
            if (s[x] == comp[0]){
                b = 0;
                cout << "Case #" << i << ":  IMPOSSIBLE" << endl;
                break;
            }
        }
        if (b){
            cout << "Case #" << i << ": " << c << endl;
        }
    }
    return 0;
}
