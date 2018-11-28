#include <iostream>
#include <string>
#include <cstdio>
#include <ctype.h>
#include <limits.h>
#include <cmath>
#include <algorithm>
#include <utility>
#include <vector>
#include <unordered_set>
#include <unordered_map>
#include <array>
#include <queue>
#include <iomanip>
using namespace std; 

#define gc getchar_unlocked
#define lli long long int
#define ld long double

class FastInput{
private:
	template <class T>
	inline static T nextInteger(){
		int c = gc();
		T x = 0;
		bool neg = 0;
		for (; ((c < 48 || c > 57) && c != '-'); c = gc());
		if (c == '-') {
			neg = 1;
			c = gc();
		}
		for (; c > 47 && c < 58 ; c = gc()) {
			x = (x << 1) + (x << 3) + c - 48;
		}
		if (neg)
			x = -x;
		return x;
	}
public:
	inline static int nextInt(){
		return nextInteger<int>();
	}

	inline static lli nextLong(){
		return nextInteger<lli>();
	}

	inline static string nextString(){
		string str = "";
		char c = gc();

		while (c >= 0 && c < 33)
			c = gc();

		while (!isspace(c) && c >= 0) {
			str += c;
			c = gc();
		}
		return str;
	}

	inline static string nextLine(){
		string str = "";
				char c = gc();

		while (c >= 0 && c < 33)
			c = gc();

		while (c != '\n' && c >= 0) {
			str += c;
			c = gc();
		}
		return str;
	}

	inline static ld nextDouble(){
		string str = nextString();
		ld res = {stold(str)};
		return res;
	}
};

int minDistance(int V, double dist[], bool sptSet[])
{
	double LIMIT = 1000000000000.0;
   // Initialize min value
  	double min = LIMIT, min_index;
  
   for (int v = 0; v < V; v++)
     if (sptSet[v] == false && dist[v] <= min)
         min = dist[v], min_index = v;
  
   return min_index;
}
  
// Funtion that implements Dijkstra's single source shortest path algorithm
// for a cost represented using adjacency matrix representation
double dijkstra(int V, double **cost, int src, int end)
{
	double LIMIT = 1000000000000.0;
     double dist[V];     // The output array.  dist[i] will hold the shortest
                      // distance from src to i
  
     bool sptSet[V]; // sptSet[i] will true if vertex i is included in shortest
                     // path tree or shortest distance from src to i is finalized
  
     // Initialize all distances as INFINITE and stpSet[] as false
     for (int i = 0; i < V; i++)
        dist[i] = LIMIT, sptSet[i] = false;
  
     // Distance of source vertex from itself is always 0
     dist[src] = 0;
  
     // Find shortest path for all vertices
     for (int count = 0; count < V-1; count++)
     {
       // Pick the minimum distance vertex from the set of vertices not
       // yet processed. u is always equal to src in first iteration.
       int u = minDistance(V, dist, sptSet);
  
       // Mark the picked vertex as processed
       sptSet[u] = true;
  
       // Update dist value of the adjacent vertices of the picked vertex.
       for (int v = 0; v < V; v++)
  
         // Update dist[v] only if is not in sptSet, there is an edge from 
         // u to v, and total weight of path from src to  v through u is 
         // smaller than current value of dist[v]
         if (!sptSet[v] && cost[u][v] > 0 && dist[u]+cost[u][v] < dist[v])
            dist[v] = dist[u] + cost[u][v];
     }
     return dist[end];
}

int main(){
	lli LIMIT = 1000000000000;
	int T = FastInput::nextInt();
	for (int t = 1; t <= T; t ++){
		int N = FastInput::nextInt();
		int Q = FastInput::nextInt();
		int dis[N][N];
		int E[N], S[N];
		for (int i = 0; i < N; i ++){
			E[i] = FastInput::nextInt();
			S[i] = FastInput::nextInt();
		}
		lli floy_dis[N][N];
		for (int i = 0; i < N; i ++)
			for (int j = 0; j < N; j ++){
				dis[i][j] = FastInput::nextInt();
				floy_dis[i][j] = LIMIT;
			}
		for (int i = 0; i < N; i ++)
			floy_dis[i][i] = 0;
		for (int i = 0; i < N; i ++)
			for (int j = 0; j < N; j ++)
				if (dis[i][j] > 0)
					floy_dis[i][j] = dis[i][j];
		for (int k = 0; k < N; k ++)
			for (int i = 0; i < N; i ++)
				for (int j = 0; j < N; j ++)
					if (floy_dis[i][j] > floy_dis[i][k] + floy_dis[k][j])
						floy_dis[i][j] = floy_dis[i][k] + floy_dis[k][j];
		double **cost = new double*[N];
		for (int i = 0; i < N; i ++){
			cost[i] = new double[N];
			for (int j = 0; j < N; j ++)
				cost[i][j] = LIMIT;
		}
		for (int i = 0; i < N; i ++){
			for (int j = 0; j < N; j ++){
				if (E[i] < floy_dis[i][j])
					continue;
				cost[i][j] = floy_dis[i][j] / (double) S[i];
			}
		}
		// for (int i = 0; i < N; i ++){
		// 	for (int j = 0; j < N; j ++){
		// 		if (cost[i][j] == LIMIT)
		// 			cost[i][j] = -1;
		// 		cout << cost[i][j] << " ";
		// 	}
		// 	cout << endl;
		// }
		// cout << endl;
		cout << "Case #" << t << ": ";
		for (int i = 0; i < Q; i ++){
			int U = FastInput::nextInt() - 1;
			int V = FastInput::nextInt() - 1;
			// cout << fixed;
			// cout << setprecision(6);
			double res = dijkstra(N, cost, U, V);
			printf("%.6f ", res);
		}
		cout << endl;
	}
	return 0;
}