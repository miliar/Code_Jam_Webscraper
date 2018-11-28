#include <fstream>
#include <string>
#include <sstream>
using namespace std;


bool tidy(long long y) {
    stringstream ss;
    ss << y;
    string s;
    ss >> s;

    for(int x = 1; x < s.length(); ++x) {
        if(s[x] < s[x-1]) return false;
    }
    return true;
}

int main() {

    ifstream fin("tidy.in");
    ofstream fout("tidy.out");
    
    long long t, n, y;
    fin >> t;

    for(int x = 1; x <= t; ++x) {
        fin >> n;
        y = n;
        while(!tidy(y)) --y;
        fout << "Case #" << x << ": " << y << endl;
    }

    fin.close();
    fout.close();
    return 0;
}
