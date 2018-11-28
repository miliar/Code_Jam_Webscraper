#include<bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef pair<int, int> PII;

const int MM = 1e9 + 7;
const double eps = 1e-8;
const int MAXN = 200 + 10;

int a[MAXN][MAXN], b[MAXN][MAXN], c[MAXN][MAXN];

class Network {
public:
    typedef int VAL;    // 费用的类型
    static const int SIZE = 505;       // 最大点数
    static const int INF = 1000000007;  // 流量的极大值
    typedef struct ARC{int t,c; VAL w; ARC* o;}* PTR;
    ARC arc[200005];    // 最大边数，注意一次普通加边操作需要占用两条边
    PTR now[SIZE],e[SIZE];      // cnt[]为该层次下的点数，l[]为层次标号
    int cnt[SIZE],l[SIZE],r[SIZE],edge; // now[]为当前弧，e[]为出边链表
    VAL sum;   // sum为当前流网络下的费用
    void clear(){memset(e,edge=sum=0,sizeof(e));}           // 清空边表
    ARC& REV(PTR x){return arc[(x-arc)^1];}                 // 取反向边
    int flow(int S, int T){return spfa_johnson(S,T,INF);}
    PTR add_edge(int x, int y, int c, VAL w = 0){
        e[x]=&(arc[edge++]=(ARC){y,c,+w,e[x]});
        e[y]=&(arc[edge++]=(ARC){x,0,-w,e[y]});
        return e[x];
    }
    int fillQvQ(int n, int tp){
		for(int i = 1; i <= n; i++){
			for(PTR u=e[i];u;u=u->o){
				if (u->c == 0 && u->t != 0){
				//cout<<(REV(u).t)<<' '<<u->t<<endl;
					b[i][(u->t)-n] |= tp;
				}
			}
		}
		//cout<<endl;
	}
    int aug(int S, int T, int& can){
        int x,z=T,use=can;
        for(x=S;x!=T;x=now[x]->t) if(use>now[x]->c) use=now[z=x]->c;
        for(x=S;x!=T;x=now[x]->t){
                now[x]->c-=use;
            REV(now[x]).c+=use;
            sum+=use*now[x]->w;
        }
        can-=use;
        return z;
    }
    int spfa_johnson(int S, int T, int can){
        if(S==T) return can;
        int in=can,x,m;
        VAL phi[SIZE],len[SIZE],MAXW=1000000007;
        memset(l,0,sizeof(l));
        fill_n(phi,SIZE,MAXW);
        phi[r[0]=T]=0;
        for(int i=m=0;i<=m;i++){
            l[x=r[i%SIZE]]=0;
            for(PTR u=e[x];u;u=u->o){
                if(phi[x]+REV(u).w>=phi[u->t] || !REV(u).c) continue;
                phi[u->t]=phi[x]+REV(u).w;
                if(!l[u->t]) l[r[++m%SIZE]=u->t]=1;
            }
        }
        do{
            typedef pair<VAL,int> TPL;
            priority_queue<TPL> q;
            fill_n(len,SIZE,MAXW);
            memset(l,0,sizeof(l));
            q.push(TPL(len[T]=0,T));
            while(q.size()){
                x=q.top().second; q.pop();
                if(!l[x]) l[x]=1; else continue;
                for(PTR u=e[x];u;u=u->o){
                    if(!REV(u).c || l[u->t]) continue;
                    VAL at=len[x]+phi[x]+REV(u).w-phi[u->t];
                    if(at>=len[u->t]) continue;
                    len[u->t]=at;
                    now[u->t]=&REV(u);
                    q.push(TPL(-at,u->t));
                }
            }
            for(x=0;x<SIZE;x++) phi[x]+=len[x];
        }while(phi[S]<0 && aug(S,T,can)!=T);
        return in-can;
    }
}nico, maki;

void prework(){

}

void read(){

}

void solve(int casi){
	int n, m, K;
//	puts("QvQ");
	cout << "Case #" << casi << ": ";
//	puts("QvQ");
	scanf("%d%d", &n, &K);
//	puts("QvQ");
	m = 2 * n - 1;
	nico.clear(); // + 0, 1~m, m+1~2*m, 2*m+1
	maki.clear(); // x 0, 1~n, n+1~2*n, 2*n+1
	for(int i = 1; i <= n; i++)
		for(int j = 1; j <= n; j++)
			a[i][j] = c[i][j] = 0;
	char s[9];
//	puts("QvQ");
	for(int i = 1; i <= K; i++){
		char s[9];
		int x, y;
		scanf("%s%d%d", s, &x, &y);
		a[x][y] = (s[0] == 'o' ? 3 : (s[0] == '+' ? 1 : 2));
	}
//	puts("QvQ");
	int INF = 1e7;
	//ll ans = 0;
	for(int i = 1; i <= n; i++)
		for(int j = 1; j <= n; j++){
			if (a[i][j] & 1){
				nico.add_edge((i + j - 1), (j - i + n) + m, 1, -INF);
			//	ans += INF;
			}else{
				nico.add_edge((i + j - 1), (j - i + n) + m, 1, -1);
			}
			
			if (a[i][j] & 2){
				maki.add_edge(i, j + n, 1, -INF);
			//	ans += INF;
			}else{
				maki.add_edge(i, j + n, 1, -1);
			}
		}
//	puts("QvQ");
	for(int i = 1; i <= m; i++)
		nico.add_edge(0, i, 1, -1), nico.add_edge(i+m, 2*m+1, 1, -1);
	for(int i = 1; i <= n; i++)
		maki.add_edge(0, i, 1, -1), maki.add_edge(i+n, 2*n+1, 1, -1);
	nico.flow(0, 2 * m + 1);
	maki.flow(0, 2 * n + 1);
//	puts("QvQ");
	for(int i = 1; i <= m; i++)
		for(int j = 1; j <= m; j++)
			b[i][j] = 0;
	nico.fillQvQ(m, 1);
	maki.fillQvQ(n, 2);
	/*for(int i = 1; i <= m; i++){
		for(int j = 1; j <= m; j++)
			cout<<b[i][j]<<' '; cout<<endl;
	}*/
	int ans = 0, cnt = 0;
	for(int i = 1; i <= n; i++)
		for(int j = 1; j <= n; j++){
			if (b[i][j] & 2)
				c[i][j] |= 2;
			if (b[i+j-1][j-i+n] & 1)
				c[i][j] |= 1;
		}
/*	cout<<endl;
	for(int i = 1; i <= n; i++){
		for(int j = 1; j <= n; j++)
			cout<<a[i][j]<<' '; cout<<endl;
		}
	for(int i = 1; i <= n; i++){
		for(int j = 1; j <= n; j++)
			cout<<c[i][j]<<' '; cout<<endl;
		}
*/	for(int i = 1; i <= n; i++)
		for(int j = 1; j <= n; j++)
			if (c[i][j]){
				ans += (c[i][j] & 1) + ((c[i][j] & 2) >> 1);
				if (a[i][j] != c[i][j])
					cnt++;
			}
	s[1] = '+';
	s[2] = 'x';
	s[3] = 'o';
	printf("%d %d\n", ans, cnt);	
	for(int i = 1; i <= n; i++)
		for(int j = 1; j <= n; j++)
			if (c[i][j] != a[i][j]){
				printf("%c %d %d\n", s[c[i][j]], i, j);
			}
}

void printans(){

}


int main(){
//	std::ios::sync_with_stdio(false);
	prework();
	int T = 1;
	cin>>T;
	for(int i = 1; i <= T; i++){
		read();
		solve(i);
		printans();
	}
	return 0;
}


