#include <bits/stdc++.h>
using namespace std;

template<class T> struct MaxFlow {
    struct edge { 
        int source, destination;
        T capacity, residue;
        edge(int s, int d, T cap, T res) : source(s), destination(d), capacity(cap), residue(res) { }
    };

    vector< vector<int> > V;
    vector<edge> E;

    MaxFlow(int N) { V.resize(N); }
    void add_arc(int source, int destination, T capacity);
    T get_flow(int source, int sink);
};

// {{{
template<class T> void MaxFlow<T>::add_arc(int source, int destination, T capacity) {
    // assert( max(source,destination) < int( V.size() ) );
    int e = E.size();
    V[source].push_back( e );
    V[destination].push_back( e+1 );
    E.push_back( edge( source, destination, capacity, capacity ) );
    E.push_back( edge( destination, source, capacity, 0 ) );
}

template<class T> T MaxFlow<T>::get_flow(int source, int sink) {
    // assert( max(source,sink) < int( V.size() ) );

    T flowSize = 0;
    int N = V.size();

    while (1) { // use BFS to find augmenting paths
        vector<int> from(N,-1);
        queue<int> Q;
        Q.push(source);
        from[source] = -2;

        while (!Q.empty()) {
            int where = Q.front(); Q.pop();
            for (int e : V[where]) {
                int dest = E[e].destination;  if (from[dest] != -1) continue;
                T res    = E[e].residue;      if (res == 0) continue;
                from[dest] = e;
                Q.push(dest);
                if (dest == sink) break;
            }
            if (from[sink] >= 0) break;
        }

        if (from[sink]==-1) return flowSize; // if there is no path, we are done

        // construct a maximum set of augmenting paths in the graph given by from[]
        for (int e : V[sink]) {
            int where = E[e].destination;         if (from[where]==-1) continue; // no path leads here
            T res = E[e].capacity - E[e].residue; if (res == 0) continue; // can't push anything more

            // walk the path and determine the delta
            T canPush = res;
            int curr = where; 
            while (1) { 
                if (from[curr] == -2) break; 
                canPush = min( canPush, E[ from[curr] ].residue );
                curr    = E[ from[curr] ].source;
            }

            // walk the path again and update capacities
            flowSize       += canPush;
            E[e  ].residue += canPush;
            E[e^1].residue -= canPush;
            curr = where;
            while (1) { 
                if (from[curr] == -2) break; 
                E[ from[curr]   ].residue -= canPush;
                E[ from[curr]^1 ].residue += canPush;
                curr = E[ from[curr] ].source;
            }
        }
    }
}
// }}}

vector< vector<bool> > solve(
        const vector< vector<bool> > &oldmap,
        const vector< vector< pair<int,int> > > &rows,
        const vector< vector< pair<int,int> > > &cols
    ) 
{
    vector< vector<bool> > newmap = oldmap;
    // build flow network
    int N = newmap.size(), B = rows.size();
    MaxFlow<int> MF(N*N + 2*B + 2);
    int source = N*N + 2*B, sink = N*N + 2*B + 1;
    for (int b=0; b<B; ++b) MF.add_arc( source, N*N+b, 1 );
    for (int b=0; b<B; ++b) MF.add_arc( N*N+B+b, sink, 1 );
    for (int b=0; b<B; ++b) {
        bool has = false;
        for (const auto &pt : rows[b]) has |= oldmap[pt.first][pt.second];
        if (!has) for (const auto &pt : rows[b]) MF.add_arc( N*N+b, N*pt.first+pt.second, 1 );
    }
    for (int b=0; b<B; ++b) {
        bool has = false;
        for (const auto &pt : cols[b]) has |= oldmap[pt.first][pt.second];
        if (!has) for (const auto &pt : cols[b]) MF.add_arc( N*pt.first+pt.second, N*N+B+b, 1 );
    }
    int flow = MF.get_flow(source,sink);
    //for (unsigned i=0; i<MF.E.size(); ++i) cout << MF.E[i].source << " " << MF.E[i].destination << " " << MF.E[i].capacity << " " << MF.E[i].residue << endl;
    for (const auto &e : MF.E) if (e.destination < N*N && e.source < N*N+B && e.residue == 0) {
        newmap[e.destination/N][e.destination%N] = true;
    }
    return newmap;
}

int main() {
    int T;
    cin >> T;
    for (int t=1; t<=T; ++t) {
        int N, M;
        cin >> N >> M;
        vector< vector<bool> > plus (N, vector<bool>(N,false));
        vector< vector<bool> > cross(N, vector<bool>(N,false));
        while (M--) {
            string typ; int r, c;
            cin >> typ >> r >> c;
            --r; --c;
            if (typ == "o" || typ == "+") plus[r][c] = true;
            if (typ == "o" || typ == "x") cross[r][c] = true;
        }
        
        vector< vector<bool> > newplus, newcross;
        // solve for crosses
        {
            vector< vector< pair<int,int> > > rows(N);
            for (int r=0; r<N; ++r) for (int c=0; c<N; ++c) rows[r].push_back( {r,c} );
            vector< vector< pair<int,int> > > cols(N);
            for (int r=0; r<N; ++r) for (int c=0; c<N; ++c) cols[c].push_back( {r,c} );
            newcross = solve( cross, rows, cols );
        }
        // solve for pluses
        {
            vector< vector< pair<int,int> > > rows(2*N-1);
            for (int s=0; s<2*N-1; ++s) for (int r=0; r<N; ++r) {
                int c = s-r;
                if (0 <= c && c < N) rows[s].push_back( {r,c} );
            }
            vector< vector< pair<int,int> > > cols(2*N-1);
            for (int d=-(N-1); d<=(N-1); ++d) for (int r=0; r<N; ++r) {
                int c = r-d;
                if (0 <= c && c < N) cols[d+(N-1)].push_back( {r,c} );
            }
            newplus = solve( plus, rows, cols );
        }
        // calc output
        vector< pair<int,int> > outcoord;
        vector<char> outsym;
        int score = 0;
        for (int r=0; r<N; ++r) for (int c=0; c<N; ++c) {
            if (newplus[r][c]) ++score;
            if (newcross[r][c]) ++score;
            if (plus[r][c] == newplus[r][c] && cross[r][c] == newcross[r][c]) continue;
            outcoord.push_back( {r,c} );
            if (newplus[r][c] && newcross[r][c]) outsym.push_back('o');
            if (!newplus[r][c] && newcross[r][c]) outsym.push_back('x');
            if (newplus[r][c] && !newcross[r][c]) outsym.push_back('+');
        }
        // print output
        cout << "Case #" << t << ": " << score << " " << outcoord.size() << endl;
        for (unsigned i=0; i<outcoord.size(); ++i) {
            cout << outsym[i] << " " << outcoord[i].first+1 << " " << outcoord[i].second+1 << endl;
        }
    }
}
// vim: fdm=marker
