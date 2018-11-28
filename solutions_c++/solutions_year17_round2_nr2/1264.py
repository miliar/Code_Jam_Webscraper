#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <vector>
#include <set>
#include <queue>
#include <string>
using namespace std;

ifstream fin("input.txt");
ofstream fout("output.txt");

// {R, O, Y, G, B, V}.
int n;
char chh[6]={'R', 'O', 'Y', 'G', 'B', 'V'};
int a[6];

void getColor(char ch, char& c1, char& c2) {
    if(ch == 'R' || ch == 'Y' || ch == 'B'){
        c1 = c2 = ch;
    }
    else if(ch == 'O') {
        c1 = 'R';
        c2 = 'Y';
    }
    else if(ch == 'G') {
        c1 = 'Y';
        c2 = 'B';
    }
    else {
        c1 = 'R';
        c2 = 'B';
    }
}

int countR() {
    int i, s=0;
    for(i=0; i<6; ++i) {
        char c1, c2;
        getColor(chh[i], c1, c2);
        if(c1 == 'R' || c2 == 'R')
            s+=a[i];
    }
    return s;
}

int countB() {
    int i, s=0;
    for(i=0; i<6; ++i) {
        char c1, c2;
        getColor(chh[i], c1, c2);
        if(c1 == 'B' || c2 == 'B')
            s+=a[i];
    }
    return s;
}

int countY() {
    int i, s=0;
    for(i=0; i<6; ++i) {
        char c1, c2;
        getColor(chh[i], c1, c2);
        if(c1 == 'Y' || c2 == 'Y')
            s+=a[i];
    }
    return s;
}

bool ok(char ch1, char ch2) {
    char ch11, ch12, ch22, ch21;
    getColor(ch1, ch11, ch12);
    getColor(ch2, ch22, ch21);

    return !(ch11 == ch21 || ch11 == ch22 || ch12 == ch21 || ch12 == ch22);
}

string s;
string ans;

bool back(int i) {
    int j,l;
    if(i == n) {
        if(ok(s[0], s[n-1])) {
            ans = s;
            return true;
        }
        else {
            return false;
        }
    }

    int leftN = n - i;
    if(leftN % 2 == 1 && i != 0)
        leftN++;
    if(countR() >= leftN/2 + 1)
        return false;

    if(countY() >= leftN/2 + 1)
        return false;

    if(countB() >= leftN/2 + 1)
        return false;

    for(j=0; j<6; ++j)
        if(a[j] > 0 && (i==0 || ok(s[i-1], chh[j]))) {
            //string bks = s;
            int bkaj = a[j];

            s+=chh[j];
            a[j]--;
            if(back(i+1))
                return true;
            a[j] = bkaj;
            //s = bks;
            s.pop_back();
        }
    return false;
}

string solve() {
    s="";
    ans="";
    back(0);
    if(ans != "")
        return ans;
    return "IMPOSSIBLE";
}

int main() {
    string ans;
    int i, t, s, tt;
    fin >> t;
    for(int tt = 1; tt <= t; ++tt) {
        fin >> n;
        for(i=0; i<6; ++i)
            fin>>a[i];
        ans = solve();
        fout << "Case #" << tt << ": " << ans << endl;
    }
    return 0;
}