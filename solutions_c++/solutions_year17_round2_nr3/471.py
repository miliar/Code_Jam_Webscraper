#include <bits/stdc++.h>
#define forn(i, n) for(i=0;i<n;++i)
#define form(i, m) for(i=m-1;i>=0;--i)
#define forab(i, a, b) for(i=a;i<b;++i)
#define forba(i, b, a) for(i=b;i>a;--i)
#define VC vector<char>
#define VVC vector<vector<char> >
#define SC set<char>
#define PII pair<int,int>
#define pb push_back
#define print(vec, type) copy(vec.begin(), vec.end(), ostream_iterator<type>(cout, " "))
using namespace std;


int i, j, k;
int N, Q;
int E[105], S[105];
double D[105][105], DD[105][105];
double inf = numeric_limits<double>::infinity();
int U[105], V[105];

void read(){
  cin >> N >> Q;
  forab(i, 1, N+1){
    cin >> E[i] >> S[i];
  }
  double tmp;
  forab(i, 1, N+1)
    forab(j, 1, N+1){
      cin >> D[i][j];
      if(D[i][j] == -1)
        D[i][j]=inf;
    }
  forab(i, 1, Q+1){
    cin >> U[i] >> V[i];
  }
}

void solve(){
  // 1.
  // find shortest path for every two cities u->v
  forab(i, 1, N+1)
    D[i][i]=0;
  forab(k, 1, N+1){
    forab(i, 1, N+1){
      forab(j, 1, N+1){
        if(D[i][j]>D[i][k]+D[k][j])
          D[i][j]=D[i][k]+D[k][j];
      }
    }
  }
  // 2.
  // for evrey city u, v
  // if horse u->v endurable
  // set u->v to time
  forab(i, 1, N+1){
    forab(j, 1, N+1){
      DD[i][j]=inf;
    }
  }
  forab(i, 1, N+1){
    DD[i][i]=0;
  }
  forab(i, 1, N+1){
    forab(j, 1, N+1){
      if(D[i][j]<=E[i]+1e-8)
      DD[i][j] = D[i][j]/S[i];
    }
  }

  // 3. 
  // bfs for query
  // priority queue
  forab(k, 1, N+1){
    forab(i, 1, N+1){
      forab(j, 1, N+1){
        if(DD[i][j]>DD[i][k]+DD[k][j])
          DD[i][j]=DD[i][k]+DD[k][j];
      }
    }
  }
}

int main(){
  int T;
  cin >> T;
  for(int ii=1; ii<=T; ii++){
    // cout << setprecision(15);
    cout << "Case #" << ii << ": ";
    read();
    solve();

    // forab(i, 1, N+1){
    //   forab(j, 1, N+1){
    //     cout << DD[i][j] << ' ';
    //   }
    //   cout << endl;
    // }
    forab(i, 1, Q+1){
      cout << setprecision(15) << DD[U[i]][V[i]] << ' ';
    }
    cout << endl;
  }
  return 0;
}