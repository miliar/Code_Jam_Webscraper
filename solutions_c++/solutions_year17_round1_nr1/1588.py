#define _CRT_SECURE_NO_WARNINGS
#include<bits/stdc++.h>
#include<unordered_map>
using namespace std;
typedef	long long ll;
typedef unsigned long long ull;
#define all(v) ((v).begin()),((v).end())
#define sz(v) ((int)((v).size()))
#define PI(n) ((double)acos(n))
#define pw2(n) (1LL<<(n))
#define sfi1(v) scanf("%d",&v)
#define sfi2(v1,v2) scanf("%d%d",&v1,&v2)
#define sfi3(v1,v2,v3) scanf("%d %d %d",&v1,&v2,&v3)
int dx8[8] = { 1, -1, 0, 0, 1, 1, -1, -1 };
int dy8[8] = { 0, 0, 1, -1, 1, -1, 1, -1 };
void file()
{
#ifndef ONLINE_JUDGE
	freopen("in.txt", "r", stdin);
	//freopen("out.txt", "w", stdout);
#else
	// online submission
#endif
}
void fast()
{
	std::ios_base::sync_with_stdio(0);
	cin.tie(NULL); cout.tie(NULL);
}
char a[26][26];
char a1[26][26];
int r, c;
void make(int i, int j){
	
	// row right
	for (int x = j + 1; x < c; x++){
		if (a[i][x] == '?'){
			a[i][x] = a[i][j];
		}
		else {
			x = c;
		}
	}
	// col  left
	for (int x = j - 1; x>=0; x--){
		if (a[i][x] == '?'){
			a[i][x] = a[i][j];
		}
		else {
			x = -1;
		}
	}

}
int main()
{
	file();
	fast();
	freopen("A-large.in", "r", stdin);
	freopen("out.txt", "w", stdout);
	int t;
	cin >> t;
	int t1 = 1;
	while (t--){

		
		cin >> r >> c;
		set<char>s;
		for (int i = 0; i < r; i++){
			for (int j = 0; j < c; j++){
				cin >> a[i][j];
				if (a[i][j] != '?')
					s.insert(a[i][j]);
				a1[i][j] = a[i][j];
			}
		}
		for (int i = 0; i < r; i++){
			for (int j = 0; j < c; j++){
				if (a[i][j] != '?'){
					make(i, j);
				}
			}
		}
		int r1 = r - 1;
		for (int i = 0; i< r1; i++){
			for (int j = 0; j < c; j++){
				if(a[i][j] != '?'&&a[i + 1][j] == '?')
					a[i+1][j] = a[i][j];
			}
		}
		for (int i = r1; i>=0; i--){
			if (i == 0)
				break;
			for (int j = 0; j < c; j++){
				if (a[i][j]!= '?' && a[i - 1][j] == '?')
					a[i-1][j] = a[i][j];
			}
		}
		for (int i = 0; i < r; i++){
			for (int j = 0; j < c; j++){
				if (a[i][j] == '?'){
					for (auto it : s){
						char ch = it;
						set<char> s2;
						if (j - 1 >= 0 && a1[i][j - 1] == '?'){
							s2.insert(a[i][j - 1]);
						}
						if (i - 1 >= 0 && a1[i-1][j] == '?'){
							s2.insert(a[i - 1][j]);
						}
						if (i - 1 >= 0 &&j-1>=0&& a1[i - 1][j-1] == '?'){
							s2.insert(a[i - 1][j-1]);
						}
						if (s2.empty()){
							a[i][j] = ch;
							break;
						}
						else if(s2.find(ch)==s2.end()){
							a[i][j] = ch;
							break;
						}
					}
					
				}
			}
		}
		cout << "Case #" << t1++ << ":" << endl;
		for (int i = 0; i < r; i++){
			for (int j = 0; j < c; j++){
				cout << a[i][j];
			}
			cout << endl;
		}

	}
}