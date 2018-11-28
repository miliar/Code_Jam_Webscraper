#include <stdio.h>
#include <limits.h>

#include <iostream>
#include <string>
#include <cmath>
  
//#define V 9
int V = 9;

using namespace std;
  
int minDistance(int dist[], bool sptSet[])
{
   int min = INT_MAX, min_index;
   for (int v = 0; v < V; v++)
     if (sptSet[v] == false && dist[v] <= min)
         min = dist[v], min_index = v;
   return min_index;
}
  
int dijkstra(int **graph, int src)
{
     int* dist = new int[V];
     bool* sptSet = new bool[V];
     for (int i = 0; i < V; i++)
        dist[i] = INT_MAX, sptSet[i] = false;
     dist[src] = 0;
     for (int count = 0; count < V-1; count++)
     {
       int u = minDistance(dist, sptSet);
       sptSet[u] = true;
       for (int v = 0; v < V; v++)
         if (!sptSet[v] && graph[u][v] && dist[u] != INT_MAX 
                                       && dist[u]+graph[u][v] < dist[v])
            dist[v] = dist[u] + graph[u][v];
     }
     return dist[V-1];
}

int stringToN(string S){
	int x=0;
	for(int i=0; i<S.length(); i++)
		if(S.at(S.length()-i-1)=='+')
			x += 1 << i;
	return x;
}

int main()
{
	string S;
	int K;
	int Si;
	int **graph;
	int minPath;
	int T;
	int iTotal = 1;

	cin >> T;

	while(T--){
		cin >> S;
		cin >> K;
		Si = stringToN(S);
		V = pow(2,S.length());
		graph = new int*[V];
		for(int i=0; i<V; i++){
			graph[i] = new int[V];
			for(int j=0; j<V; j++){
				graph[i][j]=0;
			}
		}
		for(int i=0; i<V; i++){
			int mask = 0;
			int temp;
			for(int j=0; j<K; j++){
				mask = mask + (1 << j);
			}
			for(int j=0; j<(S.length()-K+1); j++){
				temp = i ^ mask;
				graph[i][temp]=1;
				mask = mask << 1;
			}
		}
		minPath = dijkstra(graph, Si);
		if(minPath==INT_MAX)
			cout << "Case #" << iTotal << ": " << "IMPOSSIBLE" << endl;
		else
	    	cout << "Case #" << iTotal << ": " << minPath << endl;
	    iTotal++;
	    for(int i=0; i<V; i++){
			delete[] graph[i];
		}
		delete[] graph;
	}
  
    return 0;
}