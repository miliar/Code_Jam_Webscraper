#include <cstdio>
#include <cstdlib>
#include <string>
#include <cmath>
#include <algorithm>
#include <vector>
#include <map>
#include <utility>
#include <iostream>
using namespace std;

int main(int p_Argc, char  **p_Argv)
{
    int nCas;
    cin >> nCas;
    cin.ignore();

    for (int cas = 0; cas < nCas; cas++){
        string s;
        int K;
        cin >> s >> K;
        cin.ignore();

        int j = 0;
        int flip = 0;
        while ( j <= s.size() - K){
            if (s[j] == '+'){
                j++;
            }else{
                flip++;
                for (int l = 0; l < K; l++){
                    s[j+l] = s[j+l] == '+' ? '-' : '+';
                }
            }
        }
        bool ok = true;
        for (int j = s.size() - K; j < s.size(); j++){
            if (s[j] == '-')
                ok = false;
        }

        cout << "Case #" << cas + 1 <<": ";
        if (ok){
            cout << flip << endl;
        }else{
            cout << "IMPOSSIBLE"<<endl;
        }

    }

    return 0;

}





