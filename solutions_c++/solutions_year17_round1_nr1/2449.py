#include <bits/stdc++.h>
using namespace std;
//macros
#define pb push_back
#define mp make_pair
#define oo 0x3f3f3f3f
#define MVal(i) numeric_limits<i>::max()
#define mVal(i) numeric_limits<i>::min()
typedef long long ll;
typedef pair<int,int> pii;
typedef vector<int> vi;
typedef vector<pii> vii;
typedef vector<vi> vvi;
typedef map<int,int> mii;
typedef map<pii,int> mpii; 
typedef set<int> si;
typedef set<pii> sii;

int tc, r, c;
char cake[26][26];

void llenar(int x, int y, char l){
	int left = y, right = y, up = x, down = x;

	for(int i = y + 1; i < c; ++i){
		if(cake[x][i] != '?')break;
		right = i;
	}

	for(int i = y - 1; i >= 0; --i){
		if(cake[x][i] != '?')break;
		left = i;
	}

	for(int i = x + 1; i < r; ++i){
		bool f = false;
		for(int j = left; j <= right; ++j){
			if(cake[i][j] != '?'){
				f = true;
				break;
			}
		}

		if(f)break;
		down = i;
	}

	for(int i = x - 1; i >= 0; --i){
		bool f = false;
		for(int j = left; j <= right; ++j){
			if(cake[i][j] != '?'){
				f = true;
				break;
			}
		}
		if(f)break;
		up = i;
	}

	
	for(int i = up; i <= down; ++i)
		for(int j = left; j <= right; ++j)
			cake[i][j] = l;

}

//problem
int main(){
	//files
    freopen("input.in", "r", stdin);
    freopen("output.out", "w", stdout);
	queue<pii> inic;
    scanf("%d", &tc);
	for(int tcc = 1; tcc <= tc; ++tcc){
		//input
		scanf("%d %d", &r, &c);
		for(int i = 0; i < r; ++i){
			scanf("%s", cake[i]);
			for(int j = 0; j < c; ++j){
			   if(cake[i][j] != '?')inic.push(make_pair(i,j));
			}
		}
		//solution
		while(!inic.empty()){
			pii y = inic.front(); inic.pop();
			llenar(y.first, y.second, cake[y.first][y.second]);
		}
		//output
	    printf("Case #%d:\n", tcc);
	    for(int i = 0; i < r; ++i){
	    	printf("%s\n", cake[i]);
	    }
	}

	return 0;
}