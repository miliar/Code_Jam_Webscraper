#include <bits/stdc++.h>
using namespace std;

// push-relabel-matching
const int maxn = 2*50015, maxm = 150005;
int N, M, S, T;
int max_h;

typedef unsigned int flow_t;
typedef unsigned int excess_t;

struct Edge {
	int to, next;
	void set(int _to, int _next){
	  to=_to;
	  next=_next;
	}
};
Edge edges[2*maxm];
int edge_list_begin[maxn], lastEdge = 2;
inline void add_edge(int a, int b) {
    b+=N;
	edges[lastEdge].set(b, edge_list_begin[a]);
	edge_list_begin[a] = lastEdge++;
	edges[lastEdge].set(a, edge_list_begin[b]);
	edge_list_begin[b] = lastEdge++;
}
int h[maxn], e[maxn], match[maxn];
int q[2*maxn], qbegin, qend, pushcnt;
inline void enqueue(int u) {
    if(qend == 2*maxn) qend=0;
    q[qend++]=u;
}
inline void pop() {
    ++qbegin;
    if(qbegin==2*maxn) qbegin=0;
}

inline void global_relabel(){
    int* qq = q;
    if(qend < maxn) qq = q+maxn;
    int l=0, r=0;
    fill(h, h+N+M, max_h);
    fill(match, match+N, -1);
    for(int i=N;i<N+M;++i){
        if(~match[i]) {
            match[match[i]] = i;
        } else {
            qq[r++]=i;
            h[i] = 0;
        }
    }
    while(l!=r){
        int u = qq[l++];
        for(int p = edge_list_begin[u];p;p = edges[p].next){
            int v = edges[p].to;
            if(h[v] == max_h){
                h[v] = h[u]+1;
                if(~match[v]){
                    h[match[v]] = h[u]+2;
                    qq[r++] = match[v];
    }   }   }   }
}

inline void init_matching() {
	fill(h, h + N, 1);
	fill(h+N, h+N+M, 0);
	fill(e, e+N, 1);
	fill(match, match+N+M, -1);
	qbegin = qend = 0;
	for(int i=0;i<N;++i){
        enqueue(i);
	}
	pushcnt = 0;
	max_h = N+M+5;
}
excess_t max_matching() {
	init_matching();
	while (qbegin!=qend) {
		int u = q[qbegin];
		int minh = max_h;
		for (int p = edge_list_begin[u]; p; p = edges[p].next) {
			int v = edges[p].to;
			minh = min(minh, h[v]+1);
			if (h[u] == h[v] + 1) {
                if(~match[v]){
                    enqueue(match[v]);
                    e[match[v]]=1;
                }
                match[v] = u;
                h[v]+=2;
                e[u]=0;
                pop();
                break;
			}
		}
        ++pushcnt;
		if (e[u]) {
            if(minh >= max_h){
                e[u]=0;
                pop();
            }
			h[u] = minh;
		}
		if(pushcnt == 2*N){
            global_relabel();
            pushcnt = 0;
		}
	}
	excess_t hits=0;
	for(int i=N;i<N+M;++i){
        if(~match[i]){
            ++hits;
            match[match[i]] = i;
        }
	}
	return hits;
}

int grmatch(int i){
    return match[i]==-1 ? -1 : match[i]-N;
}

void init(int lSize, int rSize){
    N=lSize+1;
    M=rSize+1;
}

void reset(){
    lastEdge = 2;
    fill(edge_list_begin, edge_list_begin+N+M+5, 0);
}

int main()
{
    freopen("inD.txt", "r", stdin);
    freopen("outD.txt", "w", stdout);
    int T;cin >> T;
    for(int cas=1;cas<=T;++cas){
        cout << "Case #" << cas << ": ";

        int N, M, a, b;
        char c;
        cin >> N >> M;
        init(2*N+1, 2*N+1);
        map<pair<int, int>, char> board, board2;
        vector<int> px(N+1), py(N+1), pd1(2*N+1), pd2(2*N);
        while(M--){
            cin >> c >> a >> b;
            board[{a, b}]=board2[{a, b}]=c;
            if(c=='o'||c=='x'){
                ++px[a];
                ++py[b];
            }
            if(c=='o'||c=='+'){
                ++pd1[a+b];
                ++pd2[N+a-b];
            }
        }
        a=1, b=1;
        while(a<=N && b<=N){
            if(px[a])++a;
            else if(py[b]) ++b;
            else {
                if(board2.count(make_pair(a, b))){
                    assert(board2[make_pair(a, b)]=='+');
                    board2[{a, b}]='o';
                } else{
                    board2[{a, b}]='x';
                }
                ++a, ++b;
            }
        }
        for(int d1=2;d1<=2*N;++d1){
            for(int d2=-N+1;d2<N;++d2){
                if((d1^d2)&1) continue;
                a = (d1+d2)/2, b= (d1-d2)/2;
                if(a<1||a>N||b<1||b>N)continue;
                if(pd1[d1] || pd2[d2+N]) continue;
                add_edge(d1, d2+N);
            }
        }
        max_matching();
        for(int d1=2;d1<=2*N;++d1){
            if(match[d1]!=-1){
                a = (d1+grmatch(d1)-N)/2, b= (d1-grmatch(d1)+N)/2;
                if(board2.count({a, b})){
                    assert(board2[make_pair(a, b)]=='x');
                    board2[{a, b}]='o';
                } else {
                    board2[{a, b}]='+';
                }
            }
        }
        vector<tuple<char, int, int> > out;
        int score=0;
        for(auto &e:board2){
            if(e.second!=board[e.first]) out.emplace_back(e.second, e.first.first, e.first.second);
            score+=(e.second=='o'?2:1);
            assert(e.second=='o'||e.second=='+'||e.second=='x');
        }
        cout << score << " " << out.size() << "\n";
        for(auto &e:out){
            cout << get<0>(e) << " " << get<1>(e) << " " << get<2>(e) << "\n";
        }
        cerr << 3*N-2-score << " " << score << " " << out.size() << "\n";

        reset();
    }

    return 0;
}

