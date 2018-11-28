#include <bits/stdc++.h>

using namespace std;

typedef long long int ll;
typedef double ld;

typedef pair<ll, ll> ii;
typedef vector<ll> vi;
typedef vector<ii> vii;

#define PB push_back

#define FOR(prom,a,b) for ( ll prom = (a); prom < (ll)(b); ++prom )
#define F(a) FOR(i,0,a)
#define FF(a) FOR(j,0,a)

#define EPS (1e-10)

#define EQ(a,b) (fabs(a-b) <= fabs(a+b) * EPS)


namespace f {
ll N;
struct Edge { ll from, to, residue; };
vector<Edge> edges;
vector<vi> graph; // graph[node] = indices of outgoing edges
set<ii> used;

void add_edge(ll from, ll to, ll capacity) {
    graph[from].push_back(edges.size());
    edges.push_back(Edge{from, to, capacity});
    graph[to].push_back(edges.size());
    edges.push_back(Edge{to, from, 0});
}

vi back;
bool bfs(ll source, ll sink) {
    back=vi(N,-1);
    back[source] = -2;
    queue<ll> q;
    q.push(source);
    while (!q.empty() && back[sink] == -1) {
        ll node = q.front();
        q.pop();
        for(ll e:graph[node]){
            Edge & edge = edges[e];
            if (edge.residue && back[edge.to] == -1) {
                back[edge.to] = e;
                q.push(edge.to);
            }
        }
    }
    return back[sink] != -1;
}

ll maxflow(ll source, ll sink) {
    ll total_flow = 0;
    while (bfs(source, sink)) {
        // find size of the flow
        ll flow = 1<<30, node = sink;
        while (back[node] != -2) {
            Edge & edge = edges[back[node]];
            flow = min(flow, edge.residue);
            node = edge.from;
        }
        // push the flow
        node = sink;
        while (back[node] != -2) {
            Edge & edge = edges[back[node]],
                 & edge2 = edges[back[node]^1];
            edge.residue -= flow;
            edge2.residue += flow;
            node = edge.from;
        }
        total_flow += flow;
    }
    return total_flow;
}
}

pair<ll, ll> possibleCounts( ll Q, ll R )
{
    ll maxC = ( 10 * Q ) / 9, 
       minC = ( 10 * Q + 10 ) / 11;
    
    ll minCC = ( minC + R - 1 ) / R,
       maxCC = maxC / R;
    
    return make_pair( minCC, maxCC );
}

ii mergeRanges ( const ii & a, const ii & b )
{
    ll left = max( a.first, b.first ), right = min( a.second, b.second );
    if ( left > right ) throw 0;
    return make_pair( left, right );
}

inline ll getNodeId ( ll n, ll p, ll N )
{
    return n + p * N + 1;
}

int main ()
{
    ll T; cin >> T;
    for ( ll t = 0; t < T; ++t ) {
        ll N, P; cin >> N >> P;
        
        vector<ll> R( N );
        for ( ll n = 0; n < N; ++n )
            cin >> R[ n ];
        
        vector<vector<ll>> Q( N, vector<ll>( P ) );
        vector<vector<ii>> RANGE( N, vector<ii>( P ) );
        for ( ll n = 0; n < N; ++n )
            for ( ll p = 0; p < P; ++p ) {
                cin >> Q[ n ][ p ];
                RANGE[ n ][ p ] = possibleCounts( Q[ n ][ p ], R[ n ] );
                //cerr << "range: " << n << " " << p << " = " << RANGE[ n ][ p ].first << " " << RANGE[ n ][ p ].second << endl;
            }
                
        
        f::N = 2 + P * N;
        f::graph = vector<vi>( f::N );
        f::edges.clear();
        f::used.clear();
        
        queue<pair<ii, ii>> q;
        for (ll p = 0; p < P; ++p) {
            q.push( make_pair( make_pair( (ll)0, p ), RANGE[ 0 ][ p ] ) );
            if ( RANGE[ 0 ][ p ].first <= RANGE[ 0 ][ p ].second )
            f::add_edge( 0, getNodeId( 0, p, N ), 1 );
            if ( RANGE[ N - 1 ][ p ].first <= RANGE[ N - 1 ][ p ].second )
            f::add_edge( getNodeId( N - 1, p, N ), f::N - 1, 1 );
        }
        
        while (!q.empty()) {
            auto node = q.front(); q.pop();
            ll n = node.first.first, p = node.first.second;
            ii range = node.second;
            
            if ( n + 1 < N ) {
                for ( ll p2 = 0; p2 < P; ++p2 ) {
                    try {
                        ii newRange = mergeRanges( range, RANGE[ n + 1 ][ p2 ] );
                        q.push( make_pair( make_pair( n + 1, p2 ), newRange ) );
                        auto tr = make_pair( getNodeId( n, p, N ), getNodeId( n + 1, p2, N ) );
                        if ( !f::used.count( tr ) ) {
                            //cerr << "from: " << n << " " << p << " => " << (n + 1) << " " << p2 << endl;
                            f::add_edge( tr.first, tr.second, 1 );
                            f::used.insert( tr );
                        }
                    } catch (...) {}
                }
            }
        }
        
        ll result = f::maxflow(0, f::N - 1);
        cout << "Case #" << (t + 1) << ": " << result << endl;
    }
    return 0;
}