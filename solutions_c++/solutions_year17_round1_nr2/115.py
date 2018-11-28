#include "bits/stdc++.h"
using namespace std;
const int N = 55;
int t;
int n , m;
int r[N];
int arr[N][N];
map < int , int > mp1;
map < int , int > mp2;
inline pair < int , int > get(int arr , int r){
	int qr = ((arr * 10) / (9 * r));
	int ql = ((arr * 10 + 11 * r - 1) / (11 * r));
	return make_pair(ql , qr);
}
inline int convert(int i , int j){
	return (i - 1) * m + j;
}
namespace flow{
    const int V = 2e3 + 3;
    const int E = 2e6 + 6;
    const int inf = 1e9 + 9;
    vector < int > v[V];
    int a[E];
    int b[E];
    int c[E];
    int cur;
    int s , t;
    void init(){
        s = 0;
        t = n * m + 1;
        cur = 0;
        for(int i = 0 ; i < V ; ++i){
        	v[i].clear();
        }
    }
    void addedge(int x , int y , int z){
        a[cur] = x;
        b[cur] = y;
        c[cur] = z;
        v[x].emplace_back(cur);
        ++cur;
        a[cur] = y;
        b[cur] = x;
        c[cur] = 0;
        v[y].emplace_back(cur);
        ++cur;
    }
    int dist[V];
    int que[V];
    int qs , qe;
    bool bfs(){
        qs = 0;
        qe = 0;
        for(int i = s ; i <= t ; ++i){
            dist[i] = V;
        }
        que[qe++] = s;
        dist[s] = 0;
        while(qs < qe){
            int node = que[qs++];
            for(int edge : v[node]){
                if(c[edge]){
                    int next = b[edge];
                    if(dist[next] > dist[node] + 1){
                        dist[next] = dist[node] + 1;
                        que[qe++] = next;
                    }
                }
            }
        }
        return dist[t] < V;
    }
    int visited[V];
    int timer;
    int dfs(int node , int val){
        if(node == t){
            return val;
        }
        if(visited[node] == timer){
            return 0;
        }
        visited[node] = timer;
        int tot = 0;
        for(int edge : v[node]){
            if(c[edge]){
                int next = b[edge];
                if(dist[next] == dist[node] + 1){
                    int tmp = dfs(next , min(val - tot , c[edge]));
                    tmp = min(tmp , val - tot);
                    if(tmp){
                        c[edge] -= tmp;
                        c[edge ^ 1] += tmp;
                        tot += tmp;
                    }
                    if(tot == val){
                        break;
                    }
                }
            }
        }
        return tot;
    }
    int getflow(){
        int res = 0;
        while(bfs()){
            ++timer;
            res += dfs(s , inf);
        }
        return res;
    }
}
int main(){
	scanf("%d" , &t);
	for(int tc = 1 ; tc <= t ; ++tc){
		printf("Case #%d: " , tc);
		scanf("%d %d" , &n , &m);
		for(int i = 1 ; i <= n ; ++i){
			scanf("%d" , &r[i]);
		}
		for(int i = 1 ; i <= n ; ++i){
			for(int j = 1 ; j <= m ; ++j){
				scanf("%d" , &arr[i][j]);
			}
		}
		flow :: init();
		for(int i = 1 ; i <= m ; ++i){
			if(get(arr[1][i] , r[1]).first <= get(arr[1][i] , r[1]).second){
				flow :: addedge(0 , convert(1 , i) , 1);
			}
		}
		for(int i = 2 ; i <= n ; ++i){
			for(int j = 1 ; j <= m ; ++j){
				for(int k = 1 ; k <= m ; ++k){
					auto pre = get(arr[i - 1][j] , r[i - 1]);
					auto cur = get(arr[i][k] , r[i]);
					int l = pre.first;
					int r = pre.second;
					int ql = cur.first;
					int qr = cur.second;
					if(l > qr || r < ql || l > r || ql > qr){
						continue;
					}
					flow :: addedge(convert(i - 1 , j) , convert(i , k) , 1);
				}
			}
		}
		for(int i = 1 ; i <= m ; ++i){
			if(get(arr[n][i] , r[n]).first <= get(arr[n][i] , r[n]).second){
				flow :: addedge(convert(n , i) , n * m + 1 , 1);
			}
		}
		printf("%d\n" , flow :: getflow());
	}
}