#include<bits/stdc++.h>
using namespace std;

const int N = 60;
const int M = 3000;
typedef long long LL;

int T, n, m, B, g[N], b[M], a[N][N];
vector<int> V[N][N];

typedef pair<int,int> pii;
pii p[N][N];

int S[N][M<<2], l[M<<2], r[M<<2], lazy[N][M<<2];

#define lson o<<1
#define rson o<<1|1
#define gmid l[o]+r[o]>>1

void build(int id, int o, int ll, int rr){
	l[o] = ll;
	r[o] = rr;
	S[id][o] = lazy[id][o] = 0;
	if(ll < rr){
		int mid = gmid;
		build(id, lson, ll, mid);
		build(id, rson, mid+1, rr);
	}
}

void update(int id, int o, int ll, int rr, int v);

int pushdown(int id, int o){
	int mid = gmid;
	if(lazy[id][o]){
		update(id, lson, l[o], mid, lazy[id][o]);
		update(id, rson, mid+1, r[o], lazy[id][o]);
		lazy[id][o] = 0;
	}
	return mid;
}

void update(int id, int o, int ll, int rr, int v){
	if(l[o]==ll && r[o]==rr){
		S[id][o] += (rr - ll + 1) * v;
		lazy[id][o] += v;
		return;
	}
	int mid = pushdown(id, o);
	if(rr <= mid){
		update(id, lson, ll, rr, v);
	} else if(ll > mid){
		update(id, rson, ll, rr, v);
	} else {
		update(id, lson, ll, mid, v);
		update(id, rson, mid+1, rr, v);
	}
	S[id][o] = S[id][lson] + S[id][rson];
}

int query(int id, int o, int p){
	if(l[o]==p && r[o]==p){
		return S[id][o];
	}
	int mid = pushdown(id, o);
	int ret;
	if(p <= mid)	ret = query(id, lson, p);
	else 	ret = query(id, rson, p);
	S[id][o] = S[id][lson] + S[id][rson];
	return ret;
}

int getsum(int p){
    int ret = 0, s, g = 1000000000;
    for(int i=0; i<n; i++){
		s = query(i, 1, p);
		g = min(g, s);
    }
    return g;
}

int getl(int a, int x){
	int low=0, top=1000000, mid, ret=top;
	LL tmp;
	while(low <= top){
		mid = low + top >> 1;
		tmp = 11LL * mid * x - a * 10;
		if(tmp >= 0){
            ret = min(ret, mid);
            top = mid - 1;
		} else {
			low = mid + 1;
		}
	}
	return ret;
}

int getr(int a, int x){
	int low=0, top=1000000, mid, ret=0;
	LL tmp;
	while(low <= top){
		mid = low + top >> 1;
		tmp = 9LL * mid * x - a * 10;
		if(tmp <= 0){
            ret = max(ret, mid);
            low = mid + 1;
		} else {
			top = mid - 1;
		}
	}
	return ret;
}

pii cal(int a, int x){
    int l = getl(a, x);
    int r = getr(a, x);
    return make_pair(l, r);
}

bool cross(pii a, pii b){
	if(a.first > a.second || b.first > b.second){
		return 0;
	}
	if(a.second == 0 || b.second == 0){
		return 0;
	}
	int x = max(a.first, b.first);
	int y = min(a.second, b.second);
	return x <= y;
}

int cur[N];

bool cmp(const pii &A, const pii &B){
	return A.second < B.second || (A.second == B.second && A.first < B.first);
}

bool vis[N][N];

int main(){
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
	scanf("%d", &T);
	for(int t=1; t<=T; t++){
		scanf("%d %d", &n, &m);
		for(int i=0; i<n; i++){
			scanf("%d", g+i);
		}
		for(int i=0; i<n; i++){
			for(int j=0; j<m; j++){
				scanf("%d", &a[i][j]);
				p[i][j] = cal(a[i][j], g[i]);
			}
		}
		int ans = 0;
        B = 0;
		for(int i=0; i<n; i++){
			sort(p[i], p[i]+m, cmp);
			for(int j=0; j<m; j++){
				if(p[i][j].second>0 && p[i][j].first<=p[i][j].second){
					b[B++] = p[i][j].first;
					b[B++] = p[i][j].second;
				}
			}
        }

        sort(b, b+B);
        B = unique(b, b+B) - b;

        for(int i=0; i<n; i++){
			build(i, 1, 1, B);
			for(int j=0; j<m; j++){
				if(p[i][j].second>0 && p[i][j].first<=p[i][j].second){
					int l = p[i][j].first = lower_bound(b, b+B, p[i][j].first) - b + 1;
					int r = p[i][j].second = lower_bound(b, b+B, p[i][j].second) - b + 1;
					update(i, 1, l, r, 1);
				} else {
					p[i][j].first = -1;
				}
			}
        }

        memset(cur, 0, sizeof(cur));
        memset(vis, 0, sizeof(vis));
        for(int i=1; i<=B; i++){
            int s = getsum(i);
            if(s > 0){
				ans+=s;
				for(int j=0; j<n; j++){
					int r = s;
					cur[j] = 0;
                    while(r){
						int k = cur[j];
						cur[j]++;
						if(p[j][k].first>=0 && p[j][k].first<=i && i<=p[j][k].second){
							if(!vis[j][k]){
								vis[j][k] = 1;
								update(j, 1, p[j][k].first, p[j][k].second, -1);
								r--;
							}
						}
                    }
				}
            }
        }

        printf("Case #%d: %d\n", t, ans);
	}
	return 0;
}
