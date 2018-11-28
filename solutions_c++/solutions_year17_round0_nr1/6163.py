#include <fstream>
#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

int main()
{
    ofstream tofile;
    tofile.open("output");
    ifstream fromfile;
    fromfile.open("input");

    int T;
    fromfile >> T;
    for (int t(0); t<T; ++t){

        string s;
        fromfile >> s;
        int k;
        fromfile >> k;

        cout << s << " " << k << endl;
        int n = s.length();
        int str[1000];

        int res = 0;
        for(int i = 0; i < n; ++i){
            if (s[i] == '-') str[i] = 1;
            else str[i] = 0;
        }

        for (int i = 0; i <= n - k; ++i){
            if (str[i] == 1){
                ++res;
                for (int j = i; j < i+k; ++j){
                    str[j] = 1 - str[j];
                }
            }
        }

        //!1!!!
        for (int i = max(n - k + 1, 0); i < n; ++i){
            if (str[i]==1) {res = -1; break;}
        }
        tofile << "Case #" << t+1 << ": ";
        if (res<0) tofile << "IMPOSSIBLE" << endl;
        else tofile << res << endl;

    }

    fromfile.close();
    tofile.close();
    cout<< "DONE";



}
