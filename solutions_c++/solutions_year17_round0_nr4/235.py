#include<bits/stdc++.h>
#define pb push_back
#define mp make_pair
#define fs first
#define sc second
using namespace std;
int n,nr,T,ret,rez;
int a[110][110],b[110][110];
int x,y,vr[110],vc[110];
char C;
map<int,int> h1,h2;

#define Nmax 20100
#define Mmax 1001000
#define inf 1000000000
int S,D,flux,N,M,nrE,d[Nmax],p[Nmax];
int c[Mmax], v[Mmax], f[Mmax];
pair<int,int> mc[Mmax];
int q[Nmax*Nmax],first,last,viz[Nmax],inq[Nmax];
vector<int> m[Nmax];

inline void add(int x) {
  if(inq[x]) return; inq[x] = viz[x] = 1; q[last++] = x;
}

inline int pop() {
  int x = q[first++];
  return x;
}

inline void reset_stuff(int S) {
  first = last = 0;
  for(int i = 1; i <= N; ++i) {
    viz[i] = inq[i] = 0; d[i] = inf;
  }
  d[S] = 0;
}

inline void addEdge(int x,int y,int cap, int cost) {
  mc[++nrE]=mp(x,y);
  c[nrE] = cap; v[nrE] = cost; f[nrE] = 0;
  m[x].pb(nrE);
  mc[++nrE] = mp(y,x);
  c[nrE] = 0; f[nrE] = 0; v[nrE] = -cost;
  m[y].pb(nrE);
}

inline int getO(int x){
  if(x & 1) return x + 1; return x-1;
}

inline int bfs(int S, int D) {
  reset_stuff(S); add(S);
  while(first < last) {
    int x = pop(); if(x==D) continue;
    for(auto y : m[x]) {
      int ve = mc[y].sc;
      if(f[y] < c[y] && d[ve] > d[x] + v[y]) {
        add(ve); p[ve] = y; d[ve] = d[x] + v[y];
      }
    }
  }
  return viz[D];
}

pair<int,int> update(int S, int D) {
  int ret = 0, retc = 0;
  int flux = inf, curr = D;
  while(curr!=S) {
    int muc = p[curr], par = mc[p[curr]].fs;
    if(c[muc] - f[muc] < flux) flux = c[muc] - f[muc];
    if(!flux) break; curr = par;
  }
  curr = D;
  while(curr!=S) {
    int muc = p[curr], par = mc[p[curr]].fs;
    f[muc] += flux; f[getO(muc)] -= flux; curr = par;
  }
  ret += flux; retc += flux*d[D];
  return mp(ret, retc);
}

pair<int,int> flow(int S, int D) {
  int ret = 0, retc = 0;
  while(true) {
    if(!bfs(S, D)) break;
    pair<int,int> u = update(S,D);
    ret += u.fs, retc += u.sc;
  }
  return mp(ret, retc);
}

int getNod(int i, int j) {
  return (i+1)*n + j;
}

int main() {
  cin.sync_with_stdio(false);
  cin>>T;
  for(int t=1;t<=T;++t) {
    cin>>n>>nr;
    nrE = 0;
    ret = 0;
    rez = 0;
    h1.clear();
    h2.clear();
    for(int i=1;i<=n;++i) {
      for(int j=1;j<=n;++j) {
        a[i][j] = 0;
        b[i][j] = 0;
      }
      vr[i] = 0;
      vc[i] = 0;
    }
    
    for(int i=1;i<=nr;++i) {
      cin>>C>>x>>y;
      if(C == 'x' || C == 'o') {
        ++rez;
        vr[x] = 1;
        vc[y] = 1;
        a[x][y]++;
        b[x][y]++;
      }
      if(C == '+' || C == 'o') {
        ++rez;
        a[x][y]+=2;
        b[x][y]+=2;
        h1[x+y] = 1;
        h2[x-y] = 1;
      }
    }
    
    if(n==1) {
      cout<<"Case #"<<t<<": 2 "; 
      if(a[1][1] == 3) {
        cout<<"0\n";
      } else {
        cout<<"1\no 1 1\n";
      }
      continue;
    }
    
    int curr = 1;
    for(int i=1;i<=n;++i) {
      if(vr[i]) continue;
      while(vc[curr]) ++curr;
      if(b[i][curr] == a[i][curr]) ++ret;
      ++rez;
      b[i][curr] += 1;
      ++curr;
    }
    
    N = n*n + 4*n;
    
    for(int i=1;i<=N;++i) {
      m[i].clear();
    }
    
    
    for(int d=2;d<=2*n;++d) {
      if(!h1[d]) {
        addEdge(1,d,1,0);
      }
      for(int i=1;i<=n;++i) {
        if(d - i >= 1 && d - i <= n) {
          addEdge(d,getNod(i,d-i),1,0);
        }
      }
    }
    
    for(int d=1-n;d<=n-1;++d) {
      if(!h2[d]) {
        addEdge(3*n + n*n + d, N,1,0);
      }
      for(int i=1;i<=n;++i) {
        if(i-d >= 1 && i-d <= n) {
          addEdge(getNod(i,i-d),3*n + n*n + d,1,0);
        }
      }
    }
    
    int x = flow(1,N).fs;
    rez += x;
    
    for(int e=1;e<=nrE;++e) {
      if(f[e] > 0) {
        int x = mc[e].sc;
        if(x > 2*n && x <= 2*n + n*n) {
          int i = x/n - 1;
          int j = x%n;
          if(j==0) {
            j = n;
            --i;
          }
          if(b[i][j] == a[i][j]) ++ret;
          b[i][j] += 2;
        }
      }
    }

    cout<<"Case #"<<t<<": "<<rez<<" "<<ret<<"\n";

    for(int i=1;i<=n;++i) {
      for(int j=1;j<=n;++j) { 
        if(b[i][j] > a[i][j]) {
          int x = b[i][j];
          if(x == 1) cout<<"x ";
          if(x == 2) cout<<"+ ";
          if(x == 3) cout<<"o ";
          cout<<i<<" "<<j<<"\n";
        }
      }     
    }
    
  }
}
