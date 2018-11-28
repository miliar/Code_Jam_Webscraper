#include <bits/stdc++.h>
using namespace std;
#define ll long long
#define ld double
#define vi vector<int>
#define pb push_back
#define mp make_pair
#define F first
#define S second
#define pii pair<int,int>
#define vll vector<ll >
#define rep(i, begin, end) for (__typeof(end) i = (begin) - ((begin) > (end)); i != (end) - ((begin) > (end)); i += 1)
#define all(a) (a).begin(), (a).end()
#define print(s) cerr<<#s<<" : ";for(auto i:(s))cerr<<i<<" ";cerr<<"\n";
#define sd(t) scanf("%d",&(t))
#define pd(t) printf("%d\n",(t))
#define endl "\n"
string s[100];
vector<int> partitions[100];
bool notempty[100];
int main(){
	int t = 1, n, r, c;
	sd(t);
	for(int tt = 1; tt <= t; tt++){
		sd(r); sd(c);
		memset(notempty, 0, sizeof notempty);
		for(int i = 0; i < r; i++){
			cin >> s[i];
			int prev = 0;
			for(int j = 0; j < c; j++){
				if(s[i][j] != '?'){
					for(int k = prev; k <= j; k++) s[i][k] = s[i][j];
					prev = j + 1;
					notempty[i] = 1;
				}
			}
			if(notempty[i]){
				for(int k = prev; k < c; k++) s[i][k] = s[i][prev - 1];
			}
		}
		for(int i = 0; i < r; i++){
			if(!notempty[i]){
				bool done = 0;
				for(int k = i + 1; k < r; k++){
					if(!done && notempty[k]){
						for(int j = 0; j < c; j++) s[i][j] = s[k][j];
							done = 1;
					}
				}
				for(int k = i - 1; k >= 0; k--){
					if(!done && notempty[k]){
						for(int j = 0; j < c; j++) s[i][j] = s[k][j];
							done = 1;
					}
				}
			}
		}
		printf("Case #%d:\n", tt);
		for(int i = 0; i < r; i++){
			cout << s[i] << endl;
		}
	}
}