#pragma comment(linker, "/STACK:108777216")
#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <string>
#include <cmath>
#include <vector>
#include <deque>
#include <utility>
#include <algorithm>
using namespace std;

int const MAX_N = 2048;
int const MAX_CH = 300100;
long long const LL_INF = 1000000000000000000LL;

char st[MAX_CH];
int tst,n,m,surv[MAX_N],s[MAX_N][MAX_N];
pair<long long, long long> amnt[MAX_N][MAX_N];

//----------------------------- Graphs: Maximum flow (simple bfs, scaling method, Dinic) ----------------------------------------

typedef long long Flow_Type;
Flow_Type const INF_VALUE = 1000000000000LL;

//typedef int Flow_Type;
//Flow_Type const INF_VALUE = 2100000000;

//-------------------------------------- Graphs: Maximum flow (simple bfs) --------------------------------------------------
//                                 (works for every directed/undirected network-graph)
/*                               Time: O((N*E) * E), but often it is faster, because count of "while" iterations is often
	                                                    less than (N*E)
									Memory: O(N + E)                                                                          */
class Maximum_Flow_Simple_BFS {
	public:
		int MAX_VERTEX;
		int * flag, * from, * e_id, * och;

		struct edge {
			Flow_Type capacity, flow;
			int end_vertex, reverse_edge_index, edge_input_index;

			edge() {
				capacity = flow = 0;
				end_vertex = reverse_edge_index = edge_input_index = -1;
			}

			edge(Flow_Type capacity, Flow_Type flow,
					int end_vertex, int reverse_edge_index, int edge_input_index = -1) :
				        capacity(capacity), flow(flow),
					    end_vertex(end_vertex), reverse_edge_index(reverse_edge_index), edge_input_index(edge_input_index) {}
		};
		vector<edge> * e;

	private:
		int find_path(int n, int s, int t) {   // find path from "s" to "t" vertex
				                                // n - total number of vertexes
				                                // (returned flag "0/1")
			if (t == s)
				return 0;

			for (int i=0; i<n; i++) {
				flag[i] = 0;
				from[i] = -1;
				e_id[i] = -1;
			}

			flag[s] = 1;

			int p_read = 0, p_write = 1;
			och[p_read] = s;
	
			while (p_read < p_write) {
				int v = och[p_read++];
				for (int i=0; i<(int) e[v].size(); i++)
					if (!flag[e[v][i].end_vertex])
						if (e[v][i].capacity > e[v][i].flow) {
							flag[e[v][i].end_vertex] = 1;
							from[e[v][i].end_vertex] = v;
							e_id[e[v][i].end_vertex] = i;

							och[p_write] = e[v][i].end_vertex;
							p_write++;
						}
			}

			return flag[t];
		}

		Flow_Type augment(int n, int s, int t) {
			int i = t;
			Flow_Type mn = INF_VALUE;

			while (i!=s) {
				int j = from[i];
				mn = min(mn, e[j][e_id[i]].capacity-e[j][e_id[i]].flow);
				i = j;
			}

			i = t;
			while (i!=s) {
				int j = from[i];
				int d = e_id[i];
				e[j][d].flow += mn;
				e[i][e[j][d].reverse_edge_index].flow -= mn;
				i = j;
			}

			return mn;
		}

	public:
		void clear() {
			if (e)
				for (int i=0; i<MAX_VERTEX; i++)
					e[i].clear();
		}

		Maximum_Flow_Simple_BFS(int init_MAX_VERTEX) {
			MAX_VERTEX = init_MAX_VERTEX;
			flag = new int [MAX_VERTEX];
			from = new int [MAX_VERTEX];
			e_id = new int [MAX_VERTEX];
			och = new int [MAX_VERTEX];
			e = new vector<edge> [MAX_VERTEX];
		}

		~Maximum_Flow_Simple_BFS() {
			delete [] e;
			delete [] och;
			delete [] e_id;
			delete [] from;
			delete [] flag;
		}

		void add_edge(int a, int b, Flow_Type capacity, Flow_Type back_capacity = 0, int edge_input_index = -1) {
			if (a == b)
				return;   // incorrect edge

			e[a].push_back(edge(capacity, 0, b, (int) e[b].size(), edge_input_index));
			e[b].push_back(edge(back_capacity, 0, a, ((int) e[a].size())-1, edge_input_index));
		}

		Flow_Type max_flow(int n, int s, int t) {
			if (n <= 0 || n > MAX_VERTEX || s < 0 || s >= n || t < 0 || t >= n)
				return -1;   // inconsistent "n","s" or "t" value

			Flow_Type ans = 0;
			while (find_path(n,s,t)) ans += augment(n,s,t);
			return ans;   // maximum flow value

			// IN CASE OF UNDIRECTED NETWORK, WHERE WE ADD EDGES WITH SAME CAPACITY AND BACK_CAPACITY:
			//    mf_prc->add_edge(a,b,cap,cap,i);
			//
			// for recovering flow by every edge later you should do something like this:
			/*
				using namespace Namespace_Maximum_Flow;
				Maximum_Flow_Simple_BFS * mf_prc;

				int const MAXE = 30100;
				int ans_found[MAXE], edge_save_A[MAXE], edge_save_B[MAXE];

				int main() {
					int n;
					scanf("%d",&n);
					for (int i=0; i<n; i++) scanf("%*d %*d");
					int m;
					scanf("%d",&m);
					mf_prc = new Maximum_Flow_Simple_BFS(n);
					mf_prc->clear();
					for (int i=0; i<m; i++) {
						int a,b,cap;
						scanf("%d%d%d",&a,&b,&cap);
						a--; b--;
						edge_save_A[i] = a;
						edge_save_B[i] = b;
						mf_prc->add_edge(a,b,cap,cap,i);
					}

					printf("%d\n",mf_prc->max_flow(n,0,n-1));

					for (int i=0; i<n; i++)
						for (int j=0; j<(int) mf_prc->e[i].size(); j++) {
							int v = mf_prc->e[i][j].end_vertex;
							if (mf_prc->e[i][j].flow > 0 && !ans_found[mf_prc->e[i][j].edge_input_index]) {
								printf("%d %d %d\n",i+1,v+1,mf_prc->e[i][j].flow);
								ans_found[mf_prc->e[i][j].edge_input_index] = 1;
							}
						}

					for (int i=0; i<m; i++)
						if (!ans_found[i])
							printf("%d %d %d\n",edge_save_A[i]+1,edge_save_B[i]+1,0);

					delete mf_prc;
					return 0;
				}
			*/

			// IN CASE OF UNDIRECTED NETWORK, WHERE WE ADD 2 EDGES WITH EQUAL CAPACITIES:
			//     mf_prc->add_edge(a,b,cap,0,i);
			//     mf_prc->add_edge(b,a,cap,0,i);
			//
			// for recovering flow by every edge later you should do something like this:
			/*
				using namespace Namespace_Maximum_Flow;
				Maximum_Flow_Simple_BFS * mf_prc;

				int const MAXE = 30100;
				int ans_found[MAXE], edge_save_A[MAXE], edge_save_B[MAXE];

				int main() {
					int n;
					scanf("%d",&n);
					for (int i=0; i<n; i++) scanf("%*d %*d");
					int m;
					scanf("%d",&m);
					mf_prc = new Maximum_Flow_Simple_BFS(n);
					mf_prc->clear();
					for (int i=0; i<m; i++) {
						int a,b,cap;
						scanf("%d%d%d",&a,&b,&cap);
						a--; b--;
						edge_save_A[i] = a;
						edge_save_B[i] = b;
						mf_prc->add_edge(a,b,cap,0,i);
						mf_prc->add_edge(b,a,cap,0,i);
					}

					printf("%d\n",mf_prc->max_flow(n,0,n-1));

					for (int i=0; i<n; i++)
						for (int j=0; j<(int) mf_prc->e[i].size(); j++) {
							int v = mf_prc->e[i][j].end_vertex;
							if (mf_prc->e[i][j].flow > 0 && !ans_found[mf_prc->e[i][j].edge_input_index]) {
								printf("%d %d %d\n",i+1,v+1,mf_prc->e[i][j].flow);
								ans_found[mf_prc->e[i][j].edge_input_index] = 1;
							}
						}

					for (int i=0; i<m; i++)
						if (!ans_found[i])
							printf("%d %d %d\n",edge_save_A[i]+1,edge_save_B[i]+1,0);

					delete mf_prc;
					return 0;
				}
			*/

			// IN CASE OF DIRECTED NETWORK, WHERE WE ADD DIRECTED EDGES WITH GIVEN CAPACITY:
			//    mf_prc->add_edge(a,b,cap,0,i);
			//
			// for recovering flow by every edge later you should do something like this:
			/*
				using namespace Namespace_Maximum_Flow;
				Maximum_Flow_Simple_BFS * mf_prc;

				int const MAXN = 110;
				int row[MAXN],column[MAXN],mas[MAXN][MAXN];

				int main() {
					int n,sum1=0,sum2=0;
					cin>>n;
					for (int i=0; i<n; i++) {
						cin>>row[i];
						sum1+=row[i];
					}
					for (int i=0; i<n; i++) {
						cin>>column[i];
						sum2+=column[i];
					}
	
					mf_prc = new Maximum_Flow_Simple_BFS(2*n+2);
	
					for (int i=1; i<=n; i++) mf_prc->add_edge(0,i,row[i-1]);
					for (int i=1; i<=n; i++)
						for (int j=n+1; j<=2*n; j++)
							mf_prc->add_edge(i,j,100);
					for (int i=n+1; i<=2*n; i++) mf_prc->add_edge(i,2*n+1,column[i-n-1]);
	
					int ans = mf_prc->max_flow(2*n+2,0,2*n+1);
	
					if (ans!=sum1 || sum1!=sum2 || sum2!=ans) cout<<"NO";
					else {
						cout<<"YES\n";
						for (int i=1; i<=n; i++)
							for (int j=0; j<(int) mf_prc->e[i].size(); j++)
								if (mf_prc->e[i][j].end_vertex >= n+1 && mf_prc->e[i][j].flow > 0)
									mas[i-1][mf_prc->e[i][j].end_vertex-n-1] = mf_prc->e[i][j].flow;
						for (int i=0; i<n; i++) {
							for (int j=0; j<n; j++) cout<<mas[i][j]<<' ';
							cout<<'\n';
						}
					}

					delete mf_prc;
					return 0;
				}
			*/
		}
};
//---------------------------------------------------------------------------------------------------------------------------

long long const MX_VAL = 1024;

pair<long long, long long> find_count(long long x, long long init_w) {
	long long fr = x / init_w;
	long long min_ans = LL_INF, max_ans = -LL_INF;

	for (long long gg=fr-MX_VAL; gg<=fr+MX_VAL; gg++)
		if (gg > 0) {
			long long W = gg * init_w;

			if (x * 100 >= 90 * W   && x * 100 <= 110 * W) {
				min_ans = min(min_ans, gg);
				max_ans = max(max_ans, gg);
			}
		}

	if (min_ans > LL_INF/2)
		min_ans = max_ans = 0;

	return make_pair(min_ans, max_ans);
}


int p[128];

int inters(pair<long long, long long> a, pair<long long, long long> b) {
	return max(a.first,b.first) <= min(a.second,b.second);
}

int check_it() {
	int ans = 0;
	for (int i=0; i<m; i++) {
		int up = i;
		int down = p[i];
		if (amnt[0][up].first <= 0 || amnt[1][down].first <= 0) continue;
		if (!inters(amnt[0][up],amnt[1][down])) continue;
		ans++;
	}
	return ans;
}

int main() {
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);

	gets(st);
	sscanf(st,"%d",&tst);
	for (int q=1; q<=tst; q++) {
		scanf("%d%d",&n,&m);
		for (int i=0; i<n; i++) scanf("%d",&surv[i]);

		for (int i=0; i<n; i++)
			for (int j=0; j<m; j++) {
				scanf("%d",&s[i][j]);
				amnt[i][j] = find_count(s[i][j], surv[i]);
			}

		/*for (int i=0; i<n; i++) {
			printf("\n");
			for (int j=0; j<m; j++)
				printf("[%lld,%lld] ",amnt[i][j].first,amnt[i][j].second);
		}
		printf("\n\n");
*/



		int ans = 0;
		if (n == 1)
			for (int i=0; i<m; i++) ans += amnt[0][i].first > 0;
		else {
			for (int i=0; i<m; i++) p[i] = i;
			ans = max(ans, check_it());
			while (next_permutation(p,p+m)) ans = max(ans, check_it());
		}

		printf("Case #%d: %d\n",q,ans);
	}
	return 0;
}
