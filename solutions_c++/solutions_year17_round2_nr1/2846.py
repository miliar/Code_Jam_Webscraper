#include <vector>
#include <iostream>
#include <string>
#include <sstream>
#include <fstream>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <set>
#include <exception>
#include <utility>
#include <tuple>
#include <map>
#include <unordered_map>
#include <memory>
#include <limits>
#include <iomanip>

//#define NDEBUG // If defined, asserts are nop.
#undef NDEBUG // Asserts will throw
#include <cassert>

using namespace std;

#define FOR(i,a,b) for(int i=(a);i<(b);++i)
#define REP(i,n) FOR(i,0,n)
#define UN(a) sort(all(a)),(a).resize(unique(all(a))-(a).begin())
#define pb push_back

typedef vector<int> vi;
typedef pair<int, int> pii;
typedef long long ll;

template<class T>
void printV(const T& t){
    for(auto&v:t){
        cout<<v<<", ";
    }
    cout<<endl;
}

template<class T>
void printM(const T& t){

    for(auto&v:t){
        for(auto&vv:v){
            cout<<vv<<", ";
        }
        cout<<endl;
    }
}

// M[y, x] access pattern.
template<class T>
vector<vector<T>> loadMatrix(ifstream& fh, int y, int x){
    vector<vector<T>> M;

    T iR;
    for(int i = 0; i < y; ++i){
        M.push_back(vector<T>());

        for(int j = 0; j < x; ++j){
            fh >> iR;
            M[i].push_back(iR);
        }
    }

    return M;
}

// TODO: rename: readVector
template<class T>
vector<T> loadVector(ifstream& fh, int n){
    vector<T> V;

    T v;
    for(int i = 0; i < n; ++i){
        fh >> v;
        V.push_back(v);
    }

    return V;
}

int main(int len, const char** args){
    string file;
        
    if(len > 1){
        file = string(args[1]);
    }
    else{
        file = "tiny.in";
    }

    ifstream fh(file.c_str());

    string line;
    fh >> line;
    int ncases = stoi(line);

    string num;
    ofstream out(file + ".out");
    for(int i = 0; i < ncases; ++i){
        // TODO: write one-liner fn for this.
        string sr,sc;
        fh >> sr;
        fh >> sc;
        int D = stoi(sr);
        int N = stoi(sc);

        vector<vector<int>> M= loadMatrix<int>(fh, N, 2);

        //double tBest = (double)numeric_limits<double>::max()/1.2;
        double tBest = -1.0;
        for(int i = M.size()-1; i >= 0; --i){
            int k = M[i][0];
            int s = M[i][1];

            double t = (double)(D - k) / (double)s;
            tBest = max(t, tBest);
        }

        double ans = (double)D / tBest;


        stringstream ss;
        ss<<setprecision(10)<<std::fixed;
        ss<< "Case #" << i+1 << ": " << ans << endl;

        string sans = ss.str();
        cout << sans;
        out << sans;
    }

    return 0;
}
