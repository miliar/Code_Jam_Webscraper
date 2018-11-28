#ifdef VX_PRECOMPILED
    #include "precomp.h"
    typedef mpz_class big;
    // I use 4 cores :)
    #define MAX_THREADS 4
#else
    #include <bits/stdc++.h>
    #include<sys/stat.h>
    #include<unistd.h>
    // http://gmplib.org/ (uncomment if solution uses big nums)
    // most likely you'll get an error about mpz_class not being declared...
    //#include "gmpxx.h"
    #define big mpz_class
    // I figure that when other people want to test my solutions they shouldn't
    // get the whole multi-threaded mess that requires and deletes folders and files...
    #define MAX_THREADS 1
#endif

#define for_each(q,s) for(typeof(s.begin()) q=s.begin(); q!=s.end(); q++)
typedef long long int64;
#define long int64

using namespace std;

namespace MinCostFlow
{
    typedef int     Cost;
    typedef int     Cap;
    
    const Cost CINF  = 1000; //infinite (cost)
    const Cap  INF   = 1000;  //infinite (capacity)
    const int  MAX   = 1000+2; //maximum vertices
    const int  EDGES = 1000*1000 + 2*1000; // maximum edges
    struct network
    {
        int source, sink;
        int V, E;
        int    u;
        Cost cost[2*EDGES];
        Cap  capacity[2*EDGES];
        int  destination[2*EDGES];
        int  next[2*EDGES];
        int  first[MAX];

        network()
        {
            E = 0;
            V = 0; 
            negativeEdges = false;
        }
        int addVertex()
        {
            assert(V < MAX);
            first[V] = -1;
            return V++;
        }
        bool negativeEdges;
        void addEdge(int from, int to, Cap edgecapacity, Cost edgecost)
        {
            if (edgecost < 0) {
                negativeEdges = true;
            }
            assert(E + 2 <= 2 * EDGES);
            cost       [E] = edgecost;
            capacity   [E] = edgecapacity;
            destination[E] = to;
            next       [E] = first[from];
            first[from] = E++;
            
            cost       [E] = -edgecost;
            capacity   [E] = 0;
            destination[E] = from;
            next       [E] = first[to];
            first[to] = E++;
        }
        
        int    parentEdge[MAX];
        Cost   distance  [MAX];
        
        bool BellmanFord()
        {
            distance[source] = 0;
            for (int i=0; i<V; i++) {
                bool change = false;
                for (int j=0; j<E; j++) {
                    if (capacity[j] > 0) {
                        int u = destination[j^1];
                        int v = destination[j];
                        if (distance[u] + cost[j] < distance[v]) {
                            parentEdge[v] = j;
                            distance[v] = distance[u] + cost[j];
                            change = true;
                        }
                    }
                }
                if (! change) {
                    //no negative cycles
                    return false;
                }
            }
            // Didn't finish after V-1 iterations, there are negative cycles
            return true;
        }
        
        int  heapNode[2*EDGES];
        Cost heapCost[2*EDGES];
        int  heapSize;
        void insert(int v, Cost c)
        {
            int x = heapSize;
            heapSize++;
            while(x > 0) {
                int p = (x - 1) / 2;
                if ( heapCost[p] >= c ) {
                    heapCost[x] = heapCost[p];
                    heapNode[x] = heapNode[p];
                    x = p;
                } else {
                    break;
                }
            }
            heapCost[x] = c;
            heapNode[x] = v;
        }
        void pop(int &resv, Cost &resd)
        {
            assert(heapSize > 0);
            resv = heapNode[0];
            resd = heapCost[0];
            heapSize--;
            int v = heapNode[ heapSize];
            Cost c = heapCost[ heapSize];
            heapCost[heapSize] = CINF; //needed so that heapCost[r] is CINF
                                         // when r does not exist:
            int x = 0;
            while (x*2 + 1 < heapSize) {
                int l = x*2 + 1, r = x*2 + 2;
                if (c <= heapCost[l] && c <= heapCost[r]) {
                    break;
                } else if (heapCost[l] <= c && heapCost[l] <= heapCost[r]) {
                    //raise l
                    heapCost[x] = heapCost[l];
                    heapNode[x] = heapNode[l];
                    x = l;
                } else {
                    //raise r
                    heapCost[x] = heapCost[r];
                    heapNode[x] = heapNode[r];
                    x = r;
                }
            }
            heapNode[x] = v;
            heapCost[x] = c;
        }
        void Dijkstra()
        {
            distance[source] = 0;
            heapCost[0] = 0;
            heapNode[0] = source;
            heapSize = 1;
            while (heapSize > 0) {
                int u;
                Cost d;
                pop(u,d);
                if (d <= distance[u]) {
                    for (int e = first[u]; e != -1; e = next[e] ) {
                        int v = destination[e];
                        if (capacity[e] > 0) {
                            Cost nd = d + cost[e];
                            if (nd < distance[v]) {
                                parentEdge[v] = e;
                                distance[v] = nd;
                                insert(v, distance[v] );
                            }
                        }
                    }
                }
            }
        }
        Cost totalCost;
        Cap  totalFlow;       
        void minCostMaxFlow()
        {
            totalCost = 0;
            totalFlow = 0;
            double fix = 0;
            while(true) {
                fill(distance, distance + V, CINF);
                fill(parentEdge, parentEdge + V, -1);
                if (negativeEdges) {
                    negativeEdges = false;
                    if (BellmanFord()) {
                        //negative cycle
                        totalFlow = -1;
                        return;
                    }
                } else {
                    Dijkstra();
                }
                if (parentEdge[sink] == -1) {
                    break;
                }
                Cap f      = INF; 
                Cost tcost = 0;
                for (int x = sink; parentEdge[x] != -1; ) {
                    int e = parentEdge[x];
                    tcost += cost[e];
                    f = std::min(f, capacity[e] );
                    x = destination[e^1];
                }
                if (totalFlow >= INF - f) {
                    totalFlow = INF;
                    totalCost = CINF;
                    break;
                }
                totalFlow += f;
                totalCost += f * (tcost + fix);
                if (totalFlow >= INF) {
                    break;
                }
                // Residual network:
                for (int x = sink; parentEdge[x] != -1; ) {
                    int e = parentEdge[x];
                    capacity[e] -= f;
                    capacity[e^1] += f;
                    x = destination[e^1];
                }
                // Fix negative edges using potentials:
                for (int i=0; i < E; i++) {
                    int u = destination[i ^ 1];
                    int v = destination[i];
                    cost[i] += distance[u] - distance[v];
                }
                fix += distance[sink];

            }
        }
    };
}

//=========================================================
// program:
//
struct solver
{
    int N,C, M;
    int P[1000];
    int buyer[1000];
    
    
    tuple<int,int> solve()
    {
        vector<int> A, B;
        MinCostFlow::network *G = new MinCostFlow::network();        
        for (int i = 0; i < M; i++) {
            if (buyer[i] == 1) {
                A.push_back( P[i] );
            } else {
                B.push_back( P[i] );
            }
            G->addVertex();
        }
        G->source = G->addVertex();
        G->sink = G->addVertex();
        for (int i = 0; i < A.size(); i++) {
            G->addEdge(G->source, i, 1, 0);
        }
        for (int i = 0; i < B.size(); i++) {
            G->addEdge( A.size() + i, G->sink, 1, 0);
        }
        for (int i = 0; i < A.size(); i++) {
            for (int j = 0; j < B.size(); j++) {
                int u = A[i];
                int v = B[j];
                bool can;
                int cost = 0;
                if (u != v) {
                    can = true;
                    cost = 0;
                } else {
                    if (u == 1 && v == 1) {
                        can = false;
                        cost = -1;
                    } else {
                        can = true;
                        cost = 1;
                    }
                }
                if (can) {
                    G->addEdge(i, A.size() + j, 1, cost);
                }
            }
        }
        G->minCostMaxFlow();
        int y = M - G->totalFlow;
        int z = G->totalCost;
        delete G;
        return make_tuple(y,z);
    }
    
    void init() { }
    void read() {
        cin >> N >>C >> M;
        assert(C == 2);
        for (int i = 0; i < M; i++) {
            cin >> P[i];
            cin >> buyer[i];
        }
    }
    #if MAX_THREADS > 1
        ofstream cout;
    #endif
    void write(int cn) {
        int y,z;
        tie(y,z) = solve();
        cout << "Case #"<<cn<<": "<< y << " " << z << endl;
    }
    
};

//=========================================================
// I/O:
//
#if MAX_THREADS > 1
    void run(const char* x)
    {
        int r = system(x);
        cerr<<x<<" "<<"("<<r<<")"<<endl;
    }
#endif

int main(int argc, const char* argv[])
{
    int TestCases, mode;
    #if MAX_THREADS == 1
        // Simple and straight forward. 
        cin >> TestCases;
        solver * theSolver = new solver;
        theSolver->init();
        for (int i=1; i<= TestCases; i++) {
            theSolver->read();
            theSolver->write(i);
        }
        delete theSolver;    
    #else
        cin>>TestCases;
        //-------------------------------------------
        // Copy the whole input to a file...
        ofstream f;
        f.open("tests/.input");
        f << cin.rdbuf();
        f.close();
        // Yeah...wipe that folder... Cause we will need its files to be empty
        run("rm ./tests/.t*");
        int k = 0;
        mode = 0;
        // We create some extra threads...
        while (k < MAX_THREADS) {
            if ( fork() == 0 ) {
                mode = k + 1;
                break;
            }
            k++;
        }
        // Reopen the input, this happens for each of the threads...
        if (mode != 0) {
            assert( freopen( "tests/.input","r",stdin) );
        }
    
        solver * theSolver = new solver;
        theSolver->init();
        for (int i=1; i<= TestCases; i++) {
            // Yeah, I don't like this much either
            ofstream f;
            char fn1[200], fn2[200];
            sprintf(fn1, "tests/.test.%d", i);
            sprintf(fn2, "tests/.test.%d.done", i);
            if (mode == 0) {
                // main thread shall just join stuff together as it becomes ready
                struct stat stFileInfo;
                // When a thread finishes a test case, it writes the .done file
                // Wait for that...
                while ( stat(fn2, &stFileInfo) !=0 ) {
                    sleep(1);
                }
                // Now copy the output file...
                ifstream f(fn1);
                cout << f.rdbuf();
            } else {
                // The trick is to make each thread read all the inputs, whether
                // it will process it or not...
                theSolver->read();
                // If fn1 exists, it is being processed already. Else process it
                f.open(fn1, ios_base::out | ios_base::in);
                if ( !f ) {
                    theSolver->cout.open(fn1, ios_base::out);
                    cerr << "[" << i << "/"<<TestCases<<"] "<<mode << endl;
                    theSolver->write(i);
                    theSolver->cout.close();
                    f.open(fn2);
                    f << "1" << endl;
                }
            }
        }
        delete theSolver;
    #endif

    
    return 0;
}
