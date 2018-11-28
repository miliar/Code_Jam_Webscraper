#include <iostream>  // includes cin to read from stdin and cout to write to stdout
#include <iterator>
#include <queue>
#include <map>
#include <set>
#include <algorithm>
#include <string>
#include <sstream>
using namespace std;  // since cin and cout are both in namespace std, this saves some text

int binary(string S, char o = '+', char l = '-');

int binary(string S, char o, char l){
    int s = 0;
    for(int i=0; i<S.size();i++){
        if(S[i] == l){
            s <<= 1;
            s |= 1;
        }
        else if(S[i] == o){
            s <<= 1;
        }
    }
    return s;
}

int full(int k){
    int r = 0;
    for(int i = 0; i < k; i++){
        r <<= 1;
        r |= 1;
    }
    return r;
}

template <typename T> ostream & operator<<(ostream & out, set<T> s){
    ostream_iterator<T> output( out, " " );
    out << "< ";
    std::copy(s.begin(), s.end(), output );
    out << ">";
    return out;
}

template <typename T> ostream & operator<<(ostream & out, vector<T> s){
    ostream_iterator<T> output( out, " " );
    out << "[ ";
    std::copy(s.begin(), s.end(), output );
    out << "]";
    return out;
}

map < vector<int>, set<int> > N;

set<int> next(int x, int y, int z){
    vector <int> k(3);
    k[0] = x, k[1] = y, k[2] = z; 
    if(N.find(k) != N.end()) return N[k];
    set<int> n;
    int zz = full(z);
    int xx;
    for(int i=0; i <= (y - z); i++){
        xx = x ^ zz;
        zz <<= 1;
        n.insert(xx);
    }
    return N[k] = n;
}

int bfs(int s, int l, int k, int f = 0);

int bfs(int s, int l, int k, int f){
    queue < pair<int,int> >Q;
    Q.push(make_pair(s,0));
    set <int> V;
    set <int> N;
    set <int> D;
    set <int> n;
    n.insert(0);
    pair <int,int> p;
    V.insert(s);
    while(!Q.empty()){
        if(Q.front().first == f) return Q.front().second;
        V.insert(Q.front().first);
        N = next(Q.front().first, l, k);
        D.clear();
        set_difference(N.begin(), N.end(), V.begin(), V.end(), inserter(D, D.begin()));
        for(set<int>::iterator it = D.begin();
        it != D.end();
        it++){
            Q.push(make_pair(*it, Q.front().second+1));
        }
        Q.pop();
    }
    return -1;
}

int solve(string S, int k){
    return bfs(binary(S), S.size(), k);
}

int main() {
    int t, k;
    string S;
    int r;
    cin >> t;  // read t. cin knows that t is an int, so it reads it as such.
    for (int i = 1; i <= t; ++i) {
        cin >> S >> k;  // read n and then m.
        r = solve(S, k);
        cout << "Case #" << i << ": ";
        r==-1?cout<<"IMPOSSIBLE":cout << r;
        cout << endl;
        // cout knows that n + m and n * m are ints, and prints them accordingly.
        // It also knows "Case #", ": ", and " " are strings and that endl ends the line.
    }
    return 0;
}
