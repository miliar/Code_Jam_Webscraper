#include <iostream>  // includes cin to read from stdin and cout to write to stdout
#include <fstream>
#include <algorithm>

using namespace std;  // since cin and cout are both in namespace std, this saves some text
#define PI 3.14159265358979323846

typedef struct {
    int r;
    int h;
    double c;
    double hc;
    double rh;
}RH;

RH rh[1000];
int visited[1000];

int N, K;
double MAX;

bool cmpR(RH a, RH b) { return a.r>b.r; }
bool cmpH(RH a, RH b) { return a.h>b.h; }

double recur(int c, int d, double s) {
    double ss = 0;
    
    if (d == K) {
        return s;
    }
    
    if (d==0) {
        ss = rh[c].rh;
    }
    else {
        ss = s+rh[c].hc;
    }
    
    double S = 0;
    visited[c] = 1;
    
    for (int i=c; i<N; i++) {
        if (visited[i] == 0) {
            if (d == 0) {
                S = recur(i, d+1, ss);
            }
            else {
                S = recur(i, d+1, ss);
            }
        }
    }
    
    visited[c] = 0;
    
    if (MAX < ss) {
        MAX = ss;
    }
    
    return S;
}

int main() {
    fstream fptr;
    fptr.open("output.txt", ios::out | ios::trunc);
    int T;
    
    cin >> T;  // read t. cin knows that t is an int, so it reads it as such.
    
    for (int t = 1; t <= T; ++t) {
        N = 0;
        K = 0;
        cin >> N >> K;
        
        for (int i=0; i<N; i++) {
            cin >> rh[i].r >> rh[i].h;
            rh[i].c = PI*rh[i].r*rh[i].r;
            rh[i].hc = 2*PI*rh[i].r*rh[i].h;
            rh[i].rh = rh[i].c + rh[i].hc;
        }
        
        sort(rh, rh+N, cmpR);
        
        for (int i=0;i<N;i++) {
            recur(i, 0, 0);
        }
        
        cout.precision(20);
        fptr.precision(20);
        
        cout << "Case #"<< t << ": " << MAX << endl;
        fptr << "Case #"<< t << ": " << MAX << endl;
        
        MAX = 0;
        
        for (int i=0; i<N; i++) {
            visited[i] = 0;
        }
    }

    fptr.close();
    return 0;
}
