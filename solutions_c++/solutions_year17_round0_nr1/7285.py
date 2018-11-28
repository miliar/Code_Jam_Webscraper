#include <bits/stdc++.h>
using namespace std;

typedef int ll;
typedef vector<ll> vi;
typedef vector<vi> vvi;
typedef pair<ll, ll> ii;
typedef vector<ii> vii;
typedef vector<vii> vvii;
typedef set<ii> sii;
typedef queue<ll> q;

#define FOR(i,n) for(i=0;i<n;i++)
#define all(a) a.begin(), a.end()
#define endl '\n'
#define pb push_back
#define mp make_pair
#define F first
#define S second


int solve(vector<bool> bits, int N)
{
  queue<int> flips;
  int moves = 0;

  for (int i = 0; i < bits.size(); ++i)
  {
    if (!flips.empty() && flips.front() <= i - N)
      flips.pop();

    if ((bits[i] ^ (flips.size() % 2 == 0)) == 1)
    {
      if (i > bits.size() - N)
        return -1; // IMPOSSIBLE

      moves++;
      flips.push(i);
    } 
  }

  return moves;
}



int main(){

	#ifndef ONLINE_JUDGE
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	#endif
	ios::sync_with_stdio(false);
	cin.tie(NULL);

	int n,i,m,k,ans;
	cin>>n;
	k = n;

	while(n--){
		string temp;
		vector<bool> bits;
		cin>>temp>>m;

		FOR(i,temp.size()){
			if(temp[i] == '+')
				bits.pb(1);
			else
				bits.pb(0);
		} 

		cout<<"Case #"<<(k-n)<<": ";
		ans = solve(bits, m);
		if(ans == -1)
			cout<<"IMPOSSIBLE\n";
		else
			cout<<ans<<endl;

	}


	return 0;
}
