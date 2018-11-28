//~  Inshaallah
/*
ID: omarmuh1
PROG: test
LANG: C++
*/
#include <iostream>
#include <cmath>
#include <algorithm>
#include <vector>
#include <stack>
#include <ext/pb_ds/assoc_container.hpp>
#include <queue>
#include <map>
#include <ctime>
#include <iomanip>
#include <string.h>
#include <stdio.h>
#include <set>

using namespace std;
using namespace __gnu_pbds;

#define ll long long
#define pb push_back
#define mp make_pair
#define ff first
#define ss second
#define pp pop_back
#define pii pair<int ,int>
#define pll pair<ll , ll>
#define mid(x , y)	(x+y)/2
#define sz(x) int(x.size())
#define db		cout << "****" << endl;
#define all(x) 	x.begin() , x.end()
#define lgn 	19
#define N 	100007
#define INF 	1000000009
#define LLINF 	1000000000000000009
#define tr(i, c) for(__typeof((c).begin()) i = (c).begin(); i!=(c).end(); i++)
#define Help_me  ios_base::sync_with_stdio(false);

typedef tree<int,null_type,less<int>,rb_tree_tag,tree_order_statistics_node_update> omar;

template<class T> bool umin(T& a, T b) { if(a > b){ a = b;return 1;}return 0;}
template<class T> bool umax(T& a, T b) { if(a < b){ a = b;return 1;}return 0;}

//~ freopen("test.out" , "r" , stdin);
//~ freopen("test.out" , "w",  stdout);

int a, b, c, d, t, n, m;
char s[30][30];

int main()
{
	freopen("test.in" , "r" , stdin);
	freopen("test.out" , "w",  stdout);	
	
	scanf("%d", &t);
	
	for(int test=1; test<=t; test++){
		scanf("%d%d", &n, &m);
		
		for(int i=1;i<=n;i++)
			for(int j=1; j<=m; j++)
				scanf(" %c", &s[i][j]);
		
		for(int i=1; i<=n; i++){
			a = 0, b = 0;
			char sf = '?';
			
			for(int j=1; j<=m; j++){
				if(s[i][j] != '?')
					a = 1;
			}
			
			if(a){
				for(int j=1; j<=m; j++){
					if(s[i][j] == '?')
						s[i][j] = sf;
					else{
						sf = s[i][j];
						
						for(int u=b+1; u<j; u++)
							s[i][u] = sf;
						
						b = j;
					}
				}
			}else{
				if(i>1){
					for(int j=1; j<=m; j++)
						s[i][j] = s[i-1][j];
				}
			}
		}
		
		for(int i=n; i>=1; i--){
			a = 0;
			
			for(int j=1; j<=m; j++)
				if(s[i][j] != '?')
					a = 1;
			
			if(!a){
				for(int j=1; j<=m; j++)
					s[i][j] = s[i+1][j];
			}
		}
		
		printf("Case #%d:\n", test);
		
		for(int i=1; i<=n; i++){
			for(int j=1; j<=m; j++)
				cout << s[i][j];
			printf("\n");
		}
	}
	
 	return 0;
}

