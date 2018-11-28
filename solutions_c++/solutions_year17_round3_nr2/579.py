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

struct Int {
    int s; // [
    int e; // )
    int left;
    int right;
    int value;
};

bool operator<(const Int& i1, const Int& i2) {
    if(i1.value != i2.value)
        return i1.value > i2.value;
    return (i1.e - i1.s) < (i2.e - i2.s);
}

int c1;
int c2;
int n, m;
int NN = 24*60;
int a[2000];

vector<Int> iV;

int solve() {
    int left = 3, i, j;
    int right = 3;
    iV.clear();
    for(i=0; i<NN; ++i) {
        if(a[i] == 0) {
            for(j=i; j<NN; ++j) {
                if(a[j] != 0)
                    break;
            }
            if(j == NN)
                right = 3;
            else
                right = a[j];

            if(left == right) {
                iV.push_back(Int());
                iV.back().s = i;
                iV.back().e = j;
                iV.back().left = left;
                iV.back().right = right;
                if(left == right)
                    iV.back().value = 2;
            }
            i = j - 1;
        }
        else {
            left = a[i];
        }
    }
    sort(iV.begin(), iV.end());
    for(i=0; i<iV.size(); ++i) {
        const Int& in = iV[i];
        if((in.left == 1 || in.right == 1) && (in.e - in.s) <= c1) {
            for(j=in.s; j<in.e; ++j) {
                a[j] = 1;
                c1--;
            }
        }
        else if((in.left == 2 || in.right == 2) && (in.e - in.s) <= c2) {
            for(j=in.s; j<in.e; ++j) {
                a[j] = 2;
                c2--;
            }
        }
    }

    bool countStart = 1;
    bool countDoubleStart = 0;
    int l1=0, l2=0;

    for(i=0; i<NN; ++i)
        if(a[i] != 0)
            break;
        else
            l1++;

    for(j=NN - 1; j>0; --j)
        if(a[j] != 0)
            break;
        else
            l2++;

    if(a[i] == a[j])
        countDoubleStart = 1;

    if(a[i] == a[j] && a[i] == 1) {
        if(l1 + l2 <= c1)
            countStart = 0;
    }
    if(a[i] == a[j] && a[i] == 2) {
        if(l1 + l2 <= c2)
            countStart = 0;
    }

    int exch = 0;
    for(i=0; i<NN; ++i) {
        if(a[i]!=0) {
            if(i==0 && a[NN-1]!=a[0] && countStart) {
                ++exch;
                if(countDoubleStart)
                    ++exch;
            }
            if(i>0 && a[i] != a[i-1] && a[i] != 0 && a[i-1] != 0)
                exch++;
        }
        if(a[i] == 0) {
            if(i!=0 || countStart) {
                ++exch;
                if(i==0 && countDoubleStart)
                    ++exch;
            }
            for(j=i; j<NN; ++j) {
                if(a[j] != 0)
                    break;
            }
            if(i>0 && j!=NN && a[i-1] == a[j])
                ++exch;
            if(j == NN)
                --exch;
            i = j - 1;
        }
    }
    return exch;
}

int main() {
    int t, tt, i, j, s, e;
    fin >> t;
    for(tt = 1; tt <= t; ++tt) {
        fin >> n >> m;
        for(i=0; i<= 24*60; ++i)
            a[i] = 0;
        c1 = 12 * 60;
        c2 = 12 * 60;
        for(i=0; i<n; ++i) {
            fin >> s >> e;
            for(j=s; j<e; ++j) {
                a[j] = 1;
                c1--;
            }
        }
        for(i=0; i<m; ++i) {
            fin >> s >> e;
            for(j=s; j<e; ++j) {
                a[j] = 2;
                c2--;
            }
        }
        fout << "Case #" << tt << ": " << solve() << endl;
    }
    return 0;
}
