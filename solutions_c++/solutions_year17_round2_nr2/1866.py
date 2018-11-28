#if 0
#include <iostream>
#include<stdio.h>
#include<vector>
#include<stdio.h>
#include<algorithm>
using namespace std;
#define pii pair<long long,long long>
#define F(i,a,b) for(ll i = (ll)(a); i <= (ll)(b); i++)
#define RF(i,a,b) for(ll i = (ll)(a); i >= (ll)(b); i--)
#define PI 3.14159265
#define ll long long
#define ff first
#define ss second
#define pb(x) push_back(x)
#define mp(x,y) make_pair(x,y)
#define debug(x) cout << #x << " = " << x << endl
#define INF 1000000009
#define mod 1000000007
vector< pair<ll int, char> >v;
bool comp(pair< ll int, char >p, pair< ll int, char > q)
{
	return p.first>q.first;
}
int main()
{
	ios::sync_with_stdio(0);
	ll int t;
	cin >> t;
	ll int caser = 0;
	ll int N, R, O, Y, G, B, V;
	while (t--)
	{
		for (int i = 0; i<3; i++)
			v.clear();
		caser++;
		cin >> N >> R >> O >> Y >> G >> B >> V;
		//cout<<N<<R<<O<<Y<<G<<B<<V;
		v.push_back(make_pair(R, 'R'));
		v.push_back(make_pair(Y, 'Y'));
		v.push_back(make_pair(B, 'B'));


		sort(v.begin(), v.end(), comp);
		// cout<<v[0].first<<" "<<v[1].first<<" "<<v[2].first;
		if (v[2].first == 0)
		{
			cout << "Case #" << caser << ": ";
			if (v[0].first == v[1].first)
			{

				for (int i = 0; i<v[0].first; i++)
				{
					cout << v[0].second << v[1].second;
				}
			}
			else
			{
				cout << "IMPOSSIBLE";
			}
			cout << "\n";
		}
		else
		{
			cout << "Case #" << caser << ": ";
			if (v[0].first>v[1].first + 1)
			{
				cout << "IMPOSSIBLE";
			}
			else if (v[0].first == v[1].first + 1)
			{
				ll int  h = v[1].first - v[2].first;
				for (int i = 0; i<h; i++)
					cout << v[0].second << v[1].second;
				cout << v[0].second;
				for (int i = 0; i<v[2].first; i++)
				{
					cout << v[1].second << v[0].second << v[2].second;
				}

			}
			else
			{
				ll int  h = v[1].first - v[2].first;
				for (int i = 0; i<h; i++)
					cout << v[0].second << v[1].second;

				for (int i = 0; i<v[2].first; i++)
				{
					cout << v[0].second << v[1].second << v[2].second;
				}

			}
			cout << "\n";
		}

	}
	return 0;
}
#endif
#include<iostream>
#include<climits>
#include<cmath>
#include<algorithm>
using namespace std;
int main(){
	int t, n, man = 0, r, o, y, g, b, v, x;
	cin >> t;
	while (t--){
		man++;
		cin >> n >> r >> o >> y >> g >> b >> v;
		cout << "Case #" << man << ": ";
		x = max(max(r, y), b);
		if (x == r){
			if (x>y + b){
				cout << "IMPOSSIBLE";
			}
			else {
				while (x != (y + b)){
					if (y>b){
						cout << "R" << "Y" << "B";
					}
					else{
						cout << "R" << "B" << "Y";
					}
					y--;
					b--;
					x--;
				}
				while (y != 0){
					cout << "R" << "Y";
					y--;
				}
				while (b != 0){
					cout << "R" << "B";
					b--;
				}
			}
		}
		else if (x == y){
			if (x>r + b){
				cout << "IMPOSSIBLE";
			}
			else {
				while (x != (r + b)){
					if (r>b){
						cout << "Y" << "R" << "B";
					}
					else{
						cout << "Y" << "B" << "R";
					}
					r--;
					b--;
					x--;
				}
				while (r != 0){
					cout << "Y" << "R";
					r--;
				}
				while (b != 0){
					cout << "Y" << "B";
					b--;
				}
			}
		}
		else if (x == b){
			if (x>r + y){
				cout << "IMPOSSIBLE";
			}
			else {
				while (x != (r + y)){
					if (r>y){
						cout << "B" << "R" << "Y";
					}
					else{
						cout << "B" << "Y" << "R";
					}
					r--;
					y--;
					x--;
				}
				while (r != 0){
					cout << "B" << "R";
					r--;
				}
				while (y != 0){
					cout << "B" << "Y";
					y--;
				}
			}
		}
		cout << endl;

	}
	return 0;
}