#include <bits/stdc++.h>

#define pb push_back
#define all(a) a.begin(),a.end()
#define allr(a) a.rbegin(),a.rend()
#define fr first
#define se second
#define mp make_pair
#define sz(a) ll((a).size())
#define memo(a,b) memset(a,b,sizeof(a))
#define MAX 100001
#define INF 1e18+1

using namespace std;

typedef long long ll;
typedef pair<ll,ll> pll;
typedef vector<ll> vll;
typedef vector<pll> vpll;

int r,c,t;
bool f;
char a[26][26];
int main()
{
  ios::sync_with_stdio(false);
  cin.tie(0);cout.tie(0);
  
  cin >> t;

  for(int id = 1;id <= t;++id){

    cin >> r >> c;

    for(int i = 0;i < r;++i){
      for(int j = 0;j < c; ++j){
	cin >> a[i][j];
      }
    }

    for(int i = 0;i < r; ++i){
      for(int j = 0;j < c;++j){

	if(a[i][j] == '?')
	  continue;

	for(int k = i-1;k+1 && a[k][j] == '?';--k)
	  a[k][j] = a[k+1][j];
	
	for(int k = i+1;k<r && a[k][j] == '?';++k)
	  a[k][j] = a[k-1][j];

      }

    }

    f = true;

    for(int i = 0;i < r;++i){

      for(int j = 0;j < c;++j){

	if(a[i][j] == '?'){
	  f = false;
	  break;
	}
      }

      if(!f)
	break;
    }

    if(!f){

     for(int i = 0;i < r; ++i){
      for(int j = 0;j < c;++j){

	if(a[i][j] == '?')
	  continue;

	for(int k = j-1;k+1 && a[i][k] == '?';--k)
	  a[i][k] = a[i][k+1];
	
	for(int k = j+1;k<c && a[i][k] == '?';++k)
	  a[i][k] = a[i][k-1];

      }

     }
    }

    cout << "Case #" << id << ":" << endl;

    for(int i = 0;i < r;++i){
      for(int j = 0;j < c;++j)
	cout<<a[i][j];
      cout<<endl;
    }

  }
	
  return 0;
}
