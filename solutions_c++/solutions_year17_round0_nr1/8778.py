#include <bits/stdc++.h>

using namespace std;

#define uniq(x)  x.erase(unique(x.begin(),x.end()), x.end()) //Unique value find from vector
#define upper(arr,n,fixed) upper_bound(arr,arr+n,fixed)-arr  //Upper value search;
#define lower(arr,n,fixed) upper_bound(arr,arr+n,fixed)-arr  //Lower value search;
#define FOR(i,a,n) for(int i=a; i<(int)n; i++)
#define FORI(i,a,n) for(int i=a; i>=(int)n; i--)
#define pii pair<int,int>
#define vpii vector<pii>
#define mp make_pair
#define fi first
#define se second
#define pb push_back
#define sz(a) int((a).size())
#define fastIO() ios_base::sync_with_stdio(false); cin.tie(0)
#define endl "\n"
#define all(a) a.begin(), a.end()
#define MEMSET(p,i) memset(p,i,sizeof(p))


int BFS(string s, int k)
{
	map<string,int> M;
	queue<string> Q;

	M[s] = 1;
	Q.push(s);

	int n = sz(s);
	while(!Q.empty())
	{
		string cur = Q.front();
		Q.pop();

		FOR(i,0,n-k+1){
			string aux = cur;
			FOR(j,i,i+k)
				aux[j] = (aux[j] == '+') ? '-' : '+';

			if(M[aux] == 0){
				M[aux] = M[cur]+1;
				Q.push(aux);
			}
		}
	}

	string resp;
	FOR(i,0,n)
		resp += "+";

	return M[resp]-1;
}


int main(void)
{
	int t, k;
	cin >> t;

	FOR(i,0,t)
	{
		string s;
		cin >> s >> k;

		int answer = BFS(s,k);

		cout << "Case #" << i+1 << ": ";
		if(answer == -1)
			cout << "IMPOSSIBLE\n";
		else cout << answer << endl;
	}

	return 0;
}