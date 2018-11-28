#include <fstream>
#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

typedef unsigned long long int llint;

bool foo(string& s){
    int n = s.length();
    bool flag = false;
    for (int i = 0 ; i < n - 1; ++i){
        if (int(s[i]) > int(s[i+1])){
            flag = true;
            s[i] = char(int(s[i]) - 1);
            for (int j = i+1; j < n; ++ j) s[j] = '9';
        }
    }
    return flag;
}

int main()
{
    ofstream tofile;
    tofile.open("output");
    ifstream fromfile;
    fromfile.open("input.in");

    int T;
    fromfile >> T;
    for (int t(0); t<T; ++t){

        string s;
        fromfile >> s;
        while (foo(s));
        s.erase(0, min(s.find_first_not_of('0'), s.size()-1));
        tofile << "Case #" << t+1 << ": ";
        tofile << s << endl;

    }

    fromfile.close();
    tofile.close();
    cout<< "DONE";



}
