#include <bits/stdc++.h>
#define optimizar_io ios_base::sync_with_stdio(0);cin.tie
using namespace std;

const int INF = 1<<30;

struct Grafo{

	int n; bool bi;
    vector<vector<int>> ady;
    Grafo(int N, bool B = true)
        : n(N), bi(B), ady(N) {}

    void AgregarArista(int u, int v) {
        if (bi) ady[v].push_back(u);
        ady[u].push_back(v);
    }

	int BFS(int s,int f) {
        queue<int> q;
        vector<int> d(n, INF);
        q.push(s), d[s] = 0;

        while (!q.empty()) {
            int u = q.front(); q.pop();
            for (int v : ady[u])
                if (d[u] + 1 < d[v])
                    d[v] = d[u] + 1,
                    q.push(v);
        }
        return d[f];
    }
};

int main(){

	string s;
	int K;
	int N;
	int T;
	int ans;
	int ini;

	optimizar_io(0);

	cin >> T ;

	for(int caso = 1 ; caso <= T; caso ++){
		cin >> s >> K ;
		N = s.size();
		Grafo G = Grafo(1<<N,false);
		for(int u = 0 ; u < 1<<N ; u++){
			for(int j = 0 ; j <= N-K; j++){				
				int v = u;
				for(int k = 0 ; k < K ; k++)
					v ^=  (1<<(j+k));		 
				G.AgregarArista(u,v);					 		
			}
		}
		ini = 0;
		for(int i = 0 ; i < N ; i ++)
			if(s[i] == '+')
				ini |= (1<<i);

		ans = G.BFS(ini,(1<<N)-1);
		if(ans == INF)
			cout << "Case #"<< caso << ": " << "IMPOSSIBLE" << '\n';
		else
			cout << "Case #"<< caso << ": " << ans << '\n';

	}

	return 0;
}