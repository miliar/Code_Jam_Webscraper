#include <bits/stdc++.h>

using namespace std;

#define int long long
#define all(v) begin(v), end(v)
#define rep(i, n) for(int i = 0; i < (int)(n); i++)
#define reps(i, s, n) for(int i = (int)(s); i < (int)(n); i++)

template<class T1, class T2> void chmin(T1 &a, T2 b){if(a>b)a=b;}
template<class T1, class T2> void chmax(T1 &a, T2 b){if(a<b)a=b;}

using pint = pair<int, int>;
using tint = tuple<int, int, int>;
using vint = vector<int>;

const int inf = 1LL << 55;
const int mod = 1e9 + 7;

int N, Q;
double E[101], S[101];
double D[101][101];
double dist[101][101];

signed main()
{
  cin.tie(0);
  ios_base::sync_with_stdio(0);
  cout << fixed << setprecision(12);
  int T;
  cin >> T;
  rep(t, T) {
    cout << "Case #" << t+1 << ":";
    cin >> N >> Q;
    rep(i, N) cin >> E[i] >> S[i];
    rep(i, N) rep(j, N) {
      cin >> D[i][j];
      if(D[i][j] == -1) D[i][j] = DBL_MAX/3;
    }
    rep(i, N) rep(j, N) rep(k, N) {
      chmin(D[j][k], D[j][i]+D[i][k]);
    }
    //double sum[101] = {};
    //rep(i, N-1) sum[i+1] = sum[i] + D[i][i+1];
    while(Q--) {
      int U, V;
      cin >> U >> V;
      --U, --V;
      //cout<<"HOGE"<<endl;
      double ans = DBL_MAX;
      typedef tuple<double, int, int> TUPLE;
      priority_queue<TUPLE, vector<TUPLE>, greater<TUPLE> > que;
      que.emplace(0, U, U);
      rep(i, 101) rep(j, 101) dist[i][j] = DBL_MAX/3;
      dist[U][U] = 0;
      while(!que.empty()) {
	double cost;
	int now, idx;
	tie(cost, now, idx) = que.top(); que.pop();
	//cout<<now<<" "<<idx<<endl;
	if(now == V) {
	  chmin(ans, dist[now][idx]);
	  //continue;
	  break;
	}
	if(dist[now][idx] < cost) continue;
	rep(i, N) if(D[now][i] != DBL_MAX/3) {
	  if(E[idx] >= D[idx][i] && //sum[now+1]-sum[idx] &&
	     dist[now][idx]+D[now][i]/S[idx] <= dist[i][idx]){
	    //distance[now][idx]+ <= dist[now+1][idx]) {
	    dist[i][idx] = dist[now][idx]+D[now][i]/S[idx];
	    //dist[now+1][idx] = (sum[now+1]-sum[idx])/S[idx];
	    que.emplace(dist[i][idx], i, idx);
	  }
	  if(idx != now && E[now] >= D[now][i] &&//sum[]-sum[now] &&
	     dist[now][idx]+D[now][i]/S[now] <= dist[i][now]) {
	    //distance[now][idx]+(sum[now+1]-sum[now])/S[now] <= dist[now+1][now]) {
	    dist[i][now] = dist[now][idx]+D[now][i]/S[now];
	    //dist[now+1][now] = (sum[now+1]-sum[now])/S[now];
	    que.emplace(dist[i][now], i, now);
	  }
	}
      }
      cout << " "<<ans;
    }
    cout<<endl;
  }

  return 0;
}
