using namespace std;
#include <bits/stdc++.h>
#define rep(i,n) for(int i=0; i<(n); i++)
#define mem(x,val) memset((x),(val),sizeof(x));
#define rite(x) freopen(x,"w",stdout);
#define read(x) freopen(x,"r",stdin);
#define all(x) x.begin(),x.end()
#define sz(x) ((int)x.size())
#define sqr(x) ((x)*(x))
#define pb push_back
#define clr clear()
#define inf (1<<30)
#define ins insert
#define xx first
#define yy second
#define eps 1e-9
typedef long long i64;
typedef unsigned long long ui64;
typedef string st;
typedef vector<int> vi;
typedef vector<st> vs;
typedef map<int,int> mii;
typedef map<st,int> msi;
typedef set<int> si;
typedef set<st> ss;
typedef pair<int,int> pii;
typedef vector<pii> vpii;
#define mx 0
// void bfs(char m, char & a[][], int i, int j){
// 	if(a[i-1][j-1] == '?' && a[i-1][j] == '?' && a[i][j-1] == '?' ){
// 		a[i-1][j-1] = m;
// 		bfs(m, a, i-1, j-1);
// 	}
// 	if(a[i+1][j+1] == '?' && a[i+1][j] == '?' && a[i][j+1] == '?'){
// 		a[i+1][j+1] = m;
// 		bfs(m, a, i+1, j+1);
// 	}
// 	if(a[i-1][j+1] == '?' && a[i-1][j] == '?' && a[i][j+1] == '?'){
// 		a[i-1][j+1] = m;
// 		bfs(m, a, i+1, j+1);
// 	}


// }
int main() {
   	ios_base::sync_with_stdio(0);cin.tie(NULL);
   	//Solution
   	int T; 
   	cin >> T;
   	for (int t = 1; t <=T; ++t)
   	{
   		char grid[30][30];
   		for (int i = 0; i < 30; ++i)
   		{
   			for (int j = 0; j < 30; ++j)
   			{
   				grid[i][j] = '?';
   			}
   		}


   		int a, b;
   		cin >> a >> b;
   		for (int i = 0; i < a; ++i)
   		{
   			for (int j = 0; j < b; ++j)
   			{
   				cin >> grid[i][j];
   			}
   		}
   		char g2 [30][30];

   		for (int i = 0; i < a; ++i)
   		{
   			for (int j = 0; j < b; ++j)
   			{
   				g2[i][j] = grid[i][j];
   			}
   		}

   		
   		for (int i = 0; i < a; ++i)
							   		{
							   			for (int j = 0; j < b; ++j)
							   			{
	   				   						if(g2[i][j]!= '?'){
	   				   				   				int k = j+1, l = j-1;
	   				   				   				while(g2[i][k]== '?'&& k<b ){
	   				   				   					g2[i][k] = g2[i][j];
	   				   				   					k++;
	   				   				   					
	   				   				   				}
	   				   				   				while(g2[i][l]=='?' && l>=0){
	   				   				   					g2[i][l] = g2[i][j];
	   				   				   					l--;
	   				   				
	   				   				   				}
	   				   					}
	   				   				}
	   				   				}
   		bool fl = false;
   		for (int i = 0; i < a; ++i)
   						   		{
   						   			for (int j = 0; j < b; ++j)
   						   			{
   						   				if(g2[i][j]=='?') fl = true;
   						   			}
   						   		}
   		if(fl){ 
   									for (int i = 0; i < a; ++i)
							   		{
							   			for (int j = 0; j < b; ++j)
							   			{
	   				   						if(g2[i][j]!= '?'){
	   				   				   				int k = i+1, l = i-1;
	   				   				   				while(g2[k][j]== '?'&& k<a ){
	   				   				   					g2[k][j] = g2[i][j];
	   				   				   					k++;
	   				   				   					
	   				   				   				}
	   				   				   				while(g2[l][j]=='?' && l>=0){
	   				   				   					g2[l][j] = g2[i][j];
	   				   				   					l--;
	   				   				
	   				   				   				}
	   				   						}
	   				   					}
	   				   				}
   				   				}


   		cout << "Case #" << t << ":"<< endl;
   		for (int i = 0; i < a; ++i)
   		{
   			for (int j = 0; j < b; ++j)
   			{
   					cout << g2[i][j];
   			}
   			cout << endl;
   		}
   		// cout << endl;



   	}
	
   	
   	
   	return 0;
}


//g++-4.9 -std=c++11 a.cpp -o a && ./a < a.in > a.out