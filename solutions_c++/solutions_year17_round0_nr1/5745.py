#include <iostream>  // includes cin to read from stdin and cout to write to stdout
#include <string>

using namespace std;  // since cin and cout are both in namespace std, this saves some text

bool Verifica(int num, string str) {
    bool ver_ok = true;
    for (int i = 0; i < num; ++i)
        if (str[i] == '-')
            ver_ok = false;
    return ver_ok;
}

int main() {
  int t_T;
  string s_S;
  int k_K;
  int flip1 = 0;
  int flip2 = 0;
  string S2;

  int flip = 0;

  cin >> t_T;
  for (int ie = 1; ie <= t_T; ++ie) {
    cin >> s_S;
    cin >> k_K;

    S2 = s_S;
    int n = s_S.size();
    flip = 0;
    int x = 0;
    while (!Verifica(n, s_S) && x <= (n-k_K)) {
        x = 0;
        bool inversione = false;
        while (x <= (n-k_K) && !inversione) {
            if (s_S[x] == '-') {
                for (int i = x; i < x+k_K; ++i)
                    if (s_S[i] == '-')
                        s_S[i] = '+';
                    else
                        s_S[i] = '-';
                flip++;
                inversione = true;
            }
            x++;
        }
//        cout << s_S << endl;
    }

    if (Verifica(n, s_S))
        flip1 = flip;
//        cout << "Case #" << ie << ": " << flip << endl;
    else
        flip1 = -1;
//        cout << "Case #" << ie << ": " << "IMPOSSIBLE" << endl;

    flip = 0;
    s_S = S2;
    x = n;
    while (!Verifica(n, s_S) && x >= k_K-1) {
        x = n-1;
        bool inversione = false;
        while (x >= k_K-1 && !inversione) {
            if (s_S[x] == '-') {
                for (int i = x; i > x-k_K; --i)
                    if (s_S[i] == '-')
                        s_S[i] = '+';
                    else
                        s_S[i] = '-';
                flip++;
                inversione = true;
            }
            x--;
        }
//        cout << s_S << endl;
    }

    if (Verifica(n, s_S))
        flip2 = flip;
//        cout << "Case #" << ie << ": " << flip << endl;
    else
        flip2 = -1;
//        cout << "Case #" << ie << ": " << "IMPOSSIBLE" << endl;


    if (flip1 != -1 && flip2 != -1)
        if (flip1 <= flip2)
            cout << "Case #" << ie << ": " << flip1 << endl;
        else
            cout << "Case #" << ie << ": " << flip2 << endl;
    else
        cout << "Case #" << ie << ": " << "IMPOSSIBLE" << endl;

  }
  return 0;
}


