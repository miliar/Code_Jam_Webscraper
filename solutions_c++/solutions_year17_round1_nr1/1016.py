#define _CRT_SECURE_NO_WARNINGS
#include<iostream>
#include<sstream>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<climits>
#include<cmath>
#include<string>
#include<vector>
#include<set>
#include<map>
#include<queue>
#include<numeric>
#include<functional>
#include<algorithm>
#include<bitset>
#include<tuple>
#include<unordered_set>
#include<random>
#include<array>
#include<cassert>
using namespace std;
#define INF (1<<29)
#define rep(i,n) for(int i=0;i<(int)(n);i++)
#define all(v) v.begin(),v.end()
#define uniq(v) v.erase(unique(all(v)),v.end())



int h, w;
char f[25][25];



int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);

	int t;
	cin>>t;
	rep(i,t){
		
		cin>>h>>w;
		rep(y, h)rep(x, w)cin >> f[y][x];

		/*rep(y,h){
			vector<pair<int,char>> v;
			rep(x,w){
				if (f[y][x]!='?'){
					v.emplace_back(x,f[y][x]);
				}
				int prev=0;
				for (auto p : v){

				}
			}
		}*/

		for (int y=0;y<h;y++){
			char c = '?';
			for (int x=0;x<w;x++){
				if (f[y][x] == '?')f[y][x]=c;
				else c = f[y][x];
			}
		}
		for (int y = 0; y<h; y++){
			char c = '?';
			for (int x = w-1; x>=0; x--){
				if (f[y][x] == '?')f[y][x] = c;
				else c = f[y][x];
			}
		}

		for (int x = 0; x<w; x++){
			char c = '?';
			for (int y = 0; y < h; y++){
				if (f[y][x] == '?')f[y][x] = c;
				else c = f[y][x];
			}
		}
		for (int x = 0; x<w; x++){
			char c = '?';
			for (int y = h - 1; y >= 0; y--){
				if (f[y][x] == '?')f[y][x] = c;
				else c = f[y][x]; 
			}
		}




		cout << "Case #" << i + 1 << ":\n";
		rep(y, h){
			rep(x, w)cout << f[y][x];
			cout<<endl;
		}
	}

	return 0;
}