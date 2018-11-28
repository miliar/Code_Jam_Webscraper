//----------------------------------------------------------------
//OMLBEGIN: Flow Network
#include<vector>
#include<deque>
#include<functional>
#include<tuple>
#include<climits>
using namespace std;


struct Network {
	struct Node;
	
	struct Edge {
		int index;
		Node *u, *v;
		int cap, flow;
		
		Node* from(Node* pos) {
			if(pos == u) return v;
			return u;
		}
		void addFlow(Node* pos, int toAdd) {
			if(pos == u) flow += toAdd;
			else flow -= toAdd;
		}
		int getCap(Node* pos) {
			if(pos == u) return cap-flow;
			return flow;
		}
	};
	struct Node {
		int index;
		vector<Edge*> conn;
	};
	int n = 0, m = 0;
	deque<Node> nodes;
	deque<Edge> edges;
	
	Node* addNode() {
		nodes.push_back({n++});
		return &nodes.back();
	}
	Edge* addEdge(Node* u, Node* v, int cap = 1, int flow = 0) {
		edges.push_back({m++, u, v, cap, flow});
		u->conn.push_back(&edges.back());
		v->conn.push_back(&edges.back());
		return &edges.back();
	}
	
	int dinic(Node* source, Node* sink) {
		int result = 0;
		while(1) {
			//First divide into layers
			vector<int> level(n, -1);
			{
				deque<tuple<int, Node*> > que(1, make_tuple(0, source) );
				level[source->index] = 0;
				
				while(que.size() > 0) {
					int lev; Node* cur;
					tie(lev, cur) = que.front();
					que.pop_front();
					
					for(auto ep : cur->conn) if(ep->getCap(cur) > 0) {
						Node* next = ep->from(cur);
						if(level[next->index] == -1) {
							level[next->index] = lev+1;
							que.push_back(make_tuple(lev+1, next));
						}
					}
				}
				
				if(level[sink->index] == -1)
					return result;
			}
			
			//Now perform dfs to saturate the edges
			vector<int> connIndex(n, 0);
			
			function<int (Node*, int)> dfs = [&](Node* cur, int cap) {
				if(cur == sink)
					return cap;
				
				for(int& i = connIndex[cur->index]; i < (int)cur->conn.size(); i++) {
					Edge* edge = cur->conn[i]; Node* next = edge->from(cur);
					if(edge->getCap(cur) > 0 && level[cur->index] < level[next->index]) {
						int ret = dfs(next, min(cap, edge->getCap(cur) ) );
						if(ret > 0) {
							edge->addFlow(cur, ret);
							return ret;
						}
					}
				}
				return 0;
			};
			int ret;
			do {
				ret = dfs(source, INT_MAX);
				result += ret;
			}while(ret > 0);
		}
	}
};
//OMLEND: Flow Network
//----------------------------------------------------------------
#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	
	int T;
	cin >> T;
	
	for(int TCASE = 1; TCASE <= T; TCASE++) {
		int n, m;
		cin >> n >> m;
		
		static bool hasp[100][100], hasx[100][100];
		fill(hasp[0], hasp[0] + 100*100, false);
		fill(hasx[0], hasx[0] + 100*100, false);
		
		int aquiredPoints = 0;
		
		for(int i=0;i<m;i++) {
			char type;
			int r, c;
			cin >> type >> r >> c;
			r--, c--;
			
			if(type == '+' || type == 'o')
				hasp[r][c] = true, aquiredPoints++;
			if(type == 'x' || type == 'o')
				hasx[r][c] = true, aquiredPoints++;
		}
		
		static bool addp[100][100], addx[100][100];
		fill(addp[0], addp[0] + 100*100, false);
		fill(addx[0], addx[0] + 100*100, false);
		
		//First find the addx
		{
			vector<bool> rowUsed(n, false), colUsed(n, false);
			vector<int> rows, cols;
			
			for(int i=0;i<n;i++)
				for(int j=0;j<n;j++)
					if(hasx[i][j]) {
						rowUsed[i] = true;
						colUsed[j] = true;
					}
			
			for(int i=0;i<n;i++) {
				if(!rowUsed[i]) rows.push_back(i);
				if(!colUsed[i]) cols.push_back(i);
			}
			
			for(int i=0;i<(int)rows.size();i++)
				addx[rows[i]][cols[i]] = true, aquiredPoints++;
		}
		
		//Next find the addp
		{
			Network net;
			Network::Node *source = net.addNode(), *sink = net.addNode();
			vector<Network::Node*> diagl, diagr;
			vector<vector<Network::Node*> > squareSource(n), squareSink(n);
			
			vector<Network::Edge*> diaglEdge, diagrEdge;
			vector<vector<Network::Edge*> > square(n), squareFrom(n), squareTo(n);
			
			for(int i=0;i<2*n-1;i++) {
				diagl.push_back(net.addNode());
				diaglEdge.push_back(net.addEdge(source, diagl[i]));
				
				diagr.push_back(net.addNode());
				diagrEdge.push_back(net.addEdge(diagr[i], sink));
			}
			
			for(int i=0;i<n;i++)
				for(int j=0;j<n;j++) {
					squareSource[i].push_back(net.addNode());
					squareSink[i].push_back(net.addNode());
					
					squareFrom[i].push_back(net.addEdge(diagl[i+j], squareSource[i][j]));
					square[i].push_back(net.addEdge(squareSource[i][j], squareSink[i][j]));
					squareTo[i].push_back(net.addEdge(squareSink[i][j], diagr[i+n-1-j]));
				}
			
			//Now remove capacities from paths that are already used
			for(int i=0;i<n;i++)
				for(int j=0;j<n;j++) if(hasp[i][j]) {
					diaglEdge[i+j]->cap = 0;
					squareFrom[i][j]->cap = 0;
					square[i][j]->cap = 0;
					squareTo[i][j]->cap = 0;
					diagrEdge[i+n-1-j]->cap = 0;
				}
			
			aquiredPoints += net.dinic(source, sink);
			for(int i=0;i<n;i++)
				for(int j=0;j<n;j++) if(square[i][j]->flow == 1)
					addp[i][j] = true;
		}
		
		//Finally deduce the added models
		vector<tuple<char, int, int> > added;
		for(int i=0;i<n;i++)
			for(int j=0;j<n;j++) {
				if((addx[i][j] && addp[i][j]) || (hasx[i][j] && addp[i][j]) || (addx[i][j] && hasp[i][j]))
					added.push_back(make_tuple('o', i+1, j+1));
				else if(addx[i][j])
					added.push_back(make_tuple('x', i+1, j+1));
				else if(addp[i][j])
					added.push_back(make_tuple('+', i+1, j+1));
			}
		
		cout << "Case #" << TCASE << ": " << aquiredPoints << ' ' << added.size() << '\n';
		for(auto cur : added) {
			char type; int r, c;
			tie(type, r, c) = cur;
			cout << type << ' ' << r << ' ' << c << '\n';
		}
	}
	
	return 0;
}