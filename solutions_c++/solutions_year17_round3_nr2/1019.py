#include <iostream>
#include <iomanip>
#include <sstream>
#include <cstdlib>
#include <cstdio>

#include <vector>
#include <queue>
#include <map>
#include <set>
#include <stack>
#include <algorithm> //max...
#include <utility> //pair
#include <complex>
#include <climits> //int, ll...
#include <limits> //double...
#include <cmath> //abs, atan...

#include <cstring> //memset
#include <string>

using namespace std;

typedef long long ll;

typedef pair<int,int> ii;
typedef pair<ll, ll> ll_ll;
typedef vector<int> vi;
typedef map<int, int> mii;
typedef vector<ii> vii;
typedef vector<ll> vll;
typedef vector<pair<ii, int> > viii;
typedef vector<vi> vvi;

const long double pi =acos(-1.0);
stack<int> st;
viii v;
int extra, extra2;
vvi o;
int C, J;
int cant[2];



bool asdf(pair<ii, int> a, pair<ii, int> b){
	return a.first.first < b.first.first;
}

bool asdf2(int a, int b){
	return a> b;
}

int main (){
	int t;
	cin >> t;
	for (int i =0 ; i<t; i++){
		cin >> C >> J;
		cant[0] = cant[1] = 0;
		v.clear();
		int sol = 0;
		int aux, aux2;
		for (int j =0 ; j<C+J; j++){
			cin >> aux >> aux2;
			if (j < C)
				v.push_back(pair<ii, int>(ii(aux, aux2), 0));
			else
				v.push_back(pair<ii, int>(ii(aux, aux2), 1));
		}
		sort(v.begin(), v.end(), asdf);
		o.clear();
		o.push_back(vi());
		o.push_back(vi());

		if (v[0].second == v[v.size()-1].second){
			o[v[0].second].push_back(v[0].first.first + 1440 - v[v.size()-1].first.second);
			cant[v[0].second] += v[0].first.first + 1440 - v[v.size()-1].first.second;
		}
		else{
			sol+=1;
		}
		int ind=1, prev;
		if (v[0].second == 0){
			cant[0] += v[0].first.second - v[0].first.first;
			prev = 0;
		}
		else{
			cant[1] += v[0].first.second- v[0].first.first;
			prev = 1;
		}
		for(; ind < v.size(); ind++){
			if (v[ind].second == prev){
				cant[v[ind].second] += v[ind].first.second - v[ind-1].first.second;
				o[prev].push_back(v[ind].first.first - v[ind-1].first.second);
			}
			else{
				cant[v[ind].second] += v[ind].first.second - v[ind].first.first;
				sol += 1;
			}
		}
		int maxx = -1;
		if (cant[0] > 720){
			maxx = 0;
		}
		else if (cant[1] > 720)
			maxx = 1;
		if (maxx != -1){
			sort(o[maxx].begin(), o[maxx].end(), asdf2);
			for(int j = 0; j < o[maxx].size(); j++){
				/*
				if(v[0].second == maxx && cant[maxx]- extra <= 720){
					sol+=1;
					break;
				}
				if(v[v.size()-1].second == maxx && cant[maxx]- extra2 <= 720){
					sol+=1;
					break;
				}
				if(v[0].second == maxx && v[v.size()-1].second == maxx && cant[maxx]- extra2 -extra <= 720 ){
					sol += 2;
					break;
				}
				*/
				cant[maxx] -= o[maxx][j];
				sol+=2;
				if(cant[maxx] <= 720)
					break;
			}
		}
		/*
		if (cant[maxx] > 720){
			if(v[0].second == maxx && cant[maxx]- extra <= 720){
				sol+=1;
			}
			else if(v[v.size()-1].second == maxx && cant[maxx]- extra2 <= 720){
				sol+=1;
			}else if(v[0].second == maxx && v[v.size()-1].second == maxx && cant[maxx]- extra2 -extra <= 720 ){
				sol += 2;
			}
		}
		*/
		cout << "Case #" << i+1  << ": " << sol << endl;
	}
	return 0;
}
