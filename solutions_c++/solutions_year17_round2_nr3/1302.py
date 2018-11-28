#include <iostream>
#include <vector>
#include <cstdio>
#include <algorithm>
#include <cmath>
#include <set>
#include <queue>

#define TRUE 1
#define FALSE 0

#define DEBUG (FALSE)

using namespace std;

class Edge {       /* Directed edge */
  public:
    int from;      /* Index of the source node */
    int to;        /* Index of the destination node */
    long long length; /* Length of the edge */
    Edge(int f, int t, double l): from(f), to(t), length(l) {}
};

class Candidate {
  public:
    int n;
    double time;
    long long E;
    int S;
    Candidate(int n, double t, long long e, int s): n(n), time(t), E(e), S(s) {}
    
    bool better(Candidate other)
    {
      return (time < other.time) || (E > other.E) || (S > other.S);
    }
};

class Node {
  public:
    vector<int> out; /* Indices of edges that start in this node */
    long long E; /* Endurance */
    int S; /* Speed */
};

class Graph {         /* Directed graph */
  public:
    vector<Node> nodes; /* List of nodes */
    vector<Edge> edges; /* List of edges */

    Graph(int nr_nodes, int nr_edges)
    {
      nodes.resize(nr_nodes);  /* Create nodes, without edges */
      edges.reserve(nr_edges); /* Reserve space for edges */
    }
  
    void add_edge(int from, int to, double length) 
    {
      Edge e = Edge(from, to, length);
      edges.push_back(e); /* Add edge to the list */
      nodes[from].out.push_back(edges.size()-1); /* Add to the source node */
    }

    double Dijkstra(int start, int end)
    /* Modified dijkstra, since this problem is a bit trickier
     */
    {
      set< pair<double, pair<int, pair<long long, int> > > > q;
      vector<double> distances (nodes.size(), INFINITY); /* Init to infinity */
      vector<vector<Candidate> > candidates (nodes.size());
      Candidate c = Candidate(start, 0,0,0);
      vector<int> speeds    (nodes.size(), 0);
      vector<long long> endurances(nodes.size(), 0);
      

      distances[start]=0;             /* Starting point has distance 0 */
      candidates[0].push_back(c);
      q.insert(make_pair(0, make_pair(start,make_pair(0,0))));  /* Put starting point in the queue */
           
      while (!q.empty()) {
        double d = q.begin()->first;
        int n = q.begin()->second.first;
        long long e_left = q.begin()->second.second.first;
        int speed = q.begin()->second.second.second;
        q.erase(q.begin());
        
        for (unsigned int i = 0 ; i < nodes[n].out.size(); i++) {
          Edge &e = edges[nodes[n].out[i]];
          
          /* Check if we can keep the horse for this edge */
          if (e.length <= e_left) {
            bool insert = (candidates[e.to].size() == 0);
            int i = 0;
            double time = d + (e.length/double(speed));
            c = Candidate (e.to, time, e_left - e.length, speed);
            while (( i < candidates[e.to].size() ) && !insert)
            {
              insert = c.better(candidates[e.to][i]);
              i++;
            }
            
            if (insert)
            {
              distances[e.to] = min(distances[e.to], time);
              candidates[e.to].push_back(c);
              q.insert(make_pair(time, make_pair(e.to,make_pair(e_left - e.length, speed))));
            }
          }
          
          /* Switch horses */
          if (e.length <= nodes[n].E) {
            bool insert = (candidates[e.to].size() == 0);
            int i = 0;
            double time = d + (e.length/double(nodes[n].S));
            c = Candidate (e.to, time, nodes[n].E - e.length, nodes[n].S);
            while (( i < candidates[e.to].size() ) && !insert)
            {
              insert = c.better(candidates[e.to][i]);
              i++;
            }
            
            if (insert)
            {
              distances[e.to] = min(distances[e.to], time);
              candidates[e.to].push_back(c);
              q.insert(make_pair(time, make_pair(e.to,make_pair(nodes[n].E-e.length, nodes[n].S))));
            }
          }
        }
      }
      
      return distances[end];
    }

    void print_all()
    {
      for (unsigned int i = 0; i < nodes.size(); i++) {
        Node n = nodes[i];
        cout << "Node " << i << " has edges to: ";
        for (unsigned int j = 0; j < n.out.size(); ++j) {
          cout << edges[n.out[j]].to << " " ;
        }
        cout << endl;
      }
    }
};

void doit(int run)
{
  int N, Q;
  
  cin >> N >> Q;
  {
    int i,j;
    Graph gr = Graph(N+1,N*N);
  
    for (i = 1; i <= N; i++) {
      unsigned int a, b, d;
      
      cin >> gr.nodes[i].E >> gr.nodes[i].S;
      
    }
    
    for (i = 1; i <= N; i++) {
      for (j = 1; j <= N; j++) {
        long long D;
        cin >> D;
        
        if (D != -1) gr.add_edge(i,j,D);
      }
    }
    
    /*gr.print_all();*/
    printf("Case #%d:", run);

    for (i = 0; i < Q; i++)
    {
      vector<double> distances;
      int U,V;
      cin >> U >> V;
      
      printf(" %.6f", gr.Dijkstra(U,V));
    
    }
    printf("\n");

  }
}

int main (void)
{
	int runs=0;
        int run = 1;
	
	cin >> runs;
	while (runs--)
	{
		if (DEBUG) cout << runs << endl;
		
		doit(run);
                run++;
	}
	return 0;
}
