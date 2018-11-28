#include <iostream>
#include <string>
#include <ctime>
#include <cstdio>
#include <cstdlib>
#include <vector>
#include <iomanip>
#include <cmath>
#include <algorithm>
#include <set>
#include <map>
#include <queue>
using namespace std;
#define mp(X,Y) make_pair(X,Y)
#define F first
#define S second
typedef long long ll;
typedef pair<int,int> PII;
typedef pair<ll,ll> PLL;

int V;
const int MAX_V = 1010;
vector<int> G[MAX_V];
int match[MAX_V];
bool used[MAX_V];
bool used_row[MAX_V];
bool used_col[MAX_V];
bool x_row[MAX_V];
bool x_col[MAX_V];
int a[110][110];
bool placed[110][110];

void show_result(int n){
  char str[4] = {'.','x','+','o'};
  cout << endl;
  for(int i = 0 ;i < n ; i ++){
    for(int j = 0 ;j < n ; j ++){

      cout << str[a[i][j]] << " ";
    }
    cout << endl;
  }
  cout << endl;
}
void add_edge(int u,int v)
{
	G[u].push_back(v);
	G[v].push_back(u);
}

void clear_edge(){
  for(int i = 0 ;i < MAX_V; i++){
    G[i].clear();
  }
}
bool dfs(int v)//
{
	used[v]=1;
	for(int i=0;i<G[v].size();i++)
	{
		int u=G[v][i],w=match[u];
		if(w<0||!used[w]&&dfs(w))
		{
			match[u]=v;
			match[v]=u;
			return 1;
		}
	}
	return false ;
}

int hungary()
{
	int res=0;
	memset(match,-1,sizeof(match));
	for(int v=0;v<V;v++)
	{
		if(match[v]<0)
		{
			memset(used,0,sizeof(used));
			if(dfs(v))
			{
				res++;
			}
		}
	}
	return res;
}



int main(){
    ios::sync_with_stdio(0);
    freopen("1.in","r",stdin);
    freopen("out.txt","w",stdout);
    int t;
    int cas = 1;
    cin >> t;
    while(t--){
        cout << "Case #" << cas++<<": ";
        int n,m;
        cin >> n >> m;
        char ch;
        int r,c;
        for(int i = 0; i < MAX_V; i ++){
          used_row[i] = used_col[i] = false;
          x_row[i] = x_col[i] = false;
        }
        for(int i = 0 ;i < n ; i ++)
        for(int j = 0 ;j < n ; j ++)
          a[i][j] = placed[i][j] = 0;
        for(int i = 0 ; i < m ; i++){
          cin >> ch >> r >> c;
          r--;c--;
          if(ch != '+'){
            x_row[r] = x_col[c] = true;
            a[r][c] += 1;
          }
          if(ch != 'x'){
            a[r][c] += 2;
            int r_ = r + c, c_ = r - c + 3 * n;
            used_row[r_] = used_col[c_] = true;
          }
        }
        // x
        for(int i = 0 ;i < n ; i ++){
          if(x_row[i])continue;
          for(int j = 0 ;j < n ; j ++){
            if(x_col[j])continue;
            placed[i][j] = 1;
            a[i][j] += 1;
            x_col[j] = 1;
            break;
          }
        }

        // +
        clear_edge();
        V = 4 * n;

        for(int i = 0 ;i < n ; i ++){
          for(int j = 0 ;j < n; j ++){
            int r = i + j;
            int c = i - j + 3 * n;
            if(used_row[r])continue;
            if(used_col[c])continue;
            add_edge(r,c);
          }
        }
        int retx = hungary();
        for(int i = 0 ; i < 2 * n - 1; i ++){
          if(used_row[i])continue;
          int j = match[i];
          if(j == -1)continue;
          int r = (i + j - 3 * n) / 2;
          int c = (i - j + 3 * n) / 2;
          a[r][c] += 2;
          placed[r][c] = 1;
          //cout << "row : " << r << "  col : " << c << endl;
        }
        //show_result(n);
        int y = 0;
        int z = 0;
        for(int i = 0 ; i <n ; i++){
          for(int j = 0 ; j< n ; j++){
              y += (a[i][j] + 1) / 2;
              z += placed[i][j];
          }
        }
        cout << y << " " << z << endl;
        char str[4] =  {'.','x','+','o'};
        for(int i = 0 ; i < n ; i ++){
          for(int j = 0 ;j < n ; j ++){
            if(placed[i][j]){
              cout << str[a[i][j]] << " " << i + 1 << " " << j + 1 << endl;
            }
          }
        }




    }
    return 0;
}
