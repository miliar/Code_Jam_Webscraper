#include <cstdio>
#include <algorithm>
#include <cmath>
#include <queue>
#include <vector>
#include <map>
#include <set>

using namespace std;

typedef long long LL;
typedef pair<int , int> P2;
typedef pair<pair<int , int> , int> P3;
typedef pair<pair<int , int> , pair<int , int> > P4;
#define Fst first
#define Snd second
#define PB(a) push_back(a)
#define MP(a , b) make_pair((a) , (b))
#define M3P(a , b , c) make_pair(make_pair((a) , (b)) , (c))
#define M4P(a , b , c , d) make_pair(make_pair((a) , (b)) , make_pair((c) , (d)))
#define repp(i,a,b) for(int i = (int)(a) ; i < (int)(b) ; ++i)
#define repm(i,a,b) for(int i = (int)(a) ; i > (int)(b) ; --i)

const int EK_MAX = 210;
const int EK_EDGE_MAX = 10210;

template <class T> class EK{
public:
	vector<int> V[EK_MAX];
	pair<int , int> edge[EK_EDGE_MAX];
	T f[EK_EDGE_MAX * 2];
	int d[EK_MAX];
	int n;
	
	int rev(int a){
		return a / 2 * 2 + (a + 1) % 2;
	}
	
	void bfs(int s){
		fill(d , d + EK_MAX , -1);
		d[s] = 0;
		queue<int> Q;
		Q.push(s);
		while(!Q.empty()){
			int x = Q.front(); Q.pop();
			for(vector<int>::iterator it = V[x].begin() ; it != V[x].end() ; ++it){
				if(f[*it] == 0) continue;
				int y = (*it) % 2 == 1 ? edge[(*it)/2].first : edge[(*it)/2].second;
				if(d[y] >= 0) continue;
				d[y] = d[x] + 1;
				Q.push(y);
			}
		}
	}
	
	void dft(){
		n = 0;
		fill(f , f + EK_EDGE_MAX * 2 , 0);
		repp(i,0,EK_EDGE_MAX) V[i].clear();
	}
	
	int put(int a , int b , T c){
		edge[n] = make_pair(a , b);
		V[a].push_back(2*n);
		V[b].push_back(2*n+1);
		f[2*n] = c;
		f[2*n+1] = 0;
		return n++;
	}
	
	T ans(int s , int t){
		while(1){
			bfs(s);
			if(d[t] < 0){
				T x = 0;
				for(vector<int>::iterator it = V[s].begin() ; it != V[s].end() ; ++it){
					x += f[(*it)/2*2+1] * ((*it) % 2 == 0 ? 1 : -1);
				}
				return x;
			}
			queue<int> Q;
			T y = 1e9+7;
			for(int i = t ; i != s ;){
				for(vector<int>::iterator it = V[i].begin() ; it != V[i].end() ; ++it){
					if(f[rev(*it)] == 0) continue;
					int z = (*it) % 2 == 1 ? edge[(*it)/2].first : edge[(*it)/2].second;
					if(d[z] == d[i] - 1){
						i = z;
						y = min(y , f[rev(*it)]);
						Q.push(*it);
						break;
					}
				}
			}
			while(!Q.empty()){
				int x = Q.front(); Q.pop();
				f[rev(x)] -= y;
				f[x] += y;
			}
		}
	}
};

int T;
int N,M;
bool a[111],b[111];
bool p[111],q[111],r[111],s[111];
int putt[111][111] , putx[111][111];
vector<P3> ans;
EK<int> u[2];

void def(){
	fill(a,a+111,0);
	fill(b,b+111,0);
	fill(p,p+111,0);
	fill(q,q+111,0);
	fill(r,r+111,0);
	fill(s,s+111,0);
	repp(i,0,111){
		fill(putt[i],putt[i]+111,0);
		fill(putx[i],putx[i]+111,0);
	}
	ans.clear();
	u[0].dft();
	u[1].dft();
}

int main(){
	scanf("%d" , &T);
	repp(t,0,T){
		printf("Case #%d: " , t + 1);
		scanf("%d%d" , &N , &M);
		def();
		repp(i,0,M){
			char c;
			int x,y;
			scanf(" %c%d%d" , &c , &x , &y);
			if(c == '+'){
				putt[x][y] = -1;
				if((x+y)%2 == 0){
					p[(x+y)/2] = q[(x-y+N+1)/2] = 1;
				} else {
					r[(x+y)/2] = s[(x-y+N+1)/2] = 1;
				}
			} else if(c == 'x'){
				putx[x][y] = -1;
				a[x] = b[y] = 1;
			} else if(c == 'o'){
				putt[x][y] = putx[x][y] = -1;
				a[x] = b[y] = 1;
				if((x+y)%2 == 0){
					p[(x+y)/2] = q[(x-y+N+1)/2] = 1;
				} else {
					r[(x+y)/2] = s[(x-y+N+1)/2] = 1;
				}
			}
		}
		{
			int x = 1 , y = 1;
			while(x <= N && y <= N){
				while(a[x]) ++x;
				while(b[y]) ++y;
				if(x > N || y > N) break;
				putx[x][y] = 1;
				++x;
				++y;
			}
		}
		repp(i,1,N+1){
			repp(j,1,N+1){
				if((i+j)%2==0){
					u[0].put((i+j)/2,N+(i-j+N+1)/2,1);
				} else {
					u[1].put((i+j)/2,N+(i-j+N+1)/2,1);
				}
			}
			if(!p[i]) u[0].put(0,i,1);
			if(!q[i]) u[0].put(N+i,2*N+1,1);
			if(!r[i]) u[1].put(0,i,1);
			if(!s[i]) u[1].put(N+i,2*N+1,1);
		}
		u[0].ans(0,2*N+1);
		u[1].ans(0,2*N+1);
		repp(w,0,2){
			repp(i,0,u[w].n){
				int x = u[w].edge[i].first;
				int y = u[w].edge[i].second - N;
				int z = (N+1+w) % 2;
				if(u[w].f[i*2] == 0 && x != 0 && y <= N){
					putt[x+y+(w+z-N-1)/2][x-y+(w-z+N+1)/2] = 1;
				}
			}
		}
		int point = 0;
		repp(i,1,N+1){
			repp(j,1,N+1){
				if(putt[i][j] > 0){
					if(putx[i][j] != 0){
						ans.PB(M3P(i,j,2));
					} else {
						ans.PB(M3P(i,j,0));
					}
				} else if(putx[i][j] > 0){
					if(putt[i][j] != 0){
						ans.PB(M3P(i,j,2));
					} else {
						ans.PB(M3P(i,j,1));
					}
				}
				if(putt[i][j] != 0) ++point;
				if(putx[i][j] != 0) ++point;
			}
		}
		printf("%d %d\n" , point , (int)ans.size());
		for(auto z : ans){
			printf("%c %d %d\n" , z.second > 0 ? z.second == 1 ? 'x' : 'o' : '+' , z.first.first , z.first.second);
		}
	}
	return 0;
}
