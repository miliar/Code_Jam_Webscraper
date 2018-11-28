#include <iostream>

using namespace std;

int main()
{
    int K;
    cin >> K;
    int vuelta = 1;
    while (K--){

        string s;
        int l;
        cin >> s >> l;
        int i=0, flip=0;
        while (i + l <= s.length()){
            if (s[i] == '-'){
               for (int j = 0;j < l ; j++){
                    s[i + j] = (s[i + j] == '+')?'-' : '+';
                }
                flip++;
            }

            i++;
        }
        int ok = 1;
        for (int m = 0; m< l ; m++){
          if (s[(i-1) + m] == '-'){
            ok=0;
          }
        }
        if (ok){
          cout << "Case #" << vuelta++ <<": " << flip << endl;
        }
        else {
            cout << "Case #" << vuelta++ <<": IMPOSSIBLE" <<  endl;
        }

    }

    return 0;
}
