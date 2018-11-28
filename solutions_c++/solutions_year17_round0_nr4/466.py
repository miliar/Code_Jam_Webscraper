#include <bits/stdc++.h>
using namespace std;
#define ll long long
#define mp make_pair
#define pb push_back
#define fst first
#define snd second
const ll MODP = 1000000007;

//char sp[100][100], sc[100][100]; //original info
char f[100][100], f2[100][100]; // original -> new
void solve(void){
	int score = 0;
	int n, m;
	cin >> n >> m;
	//for(int i=0;i<n;i++)for(int j=0;j<n;j++) {sp[i][j] = '.'; sc[i][j] = '.';}
	for(int i=0;i<n;i++)for(int j=0;j<n;j++) {f[i][j] = '.';}
	vector<pair<int, int> > plus, cross;
	set<int> ci, cj, ps, pd; 
	for(int i=0;i<m;i++){
		char c;	int ti, tj;
		cin >> c >> ti >> tj; ti--; tj--;
		if (c=='o' || c=='+'){
			plus.pb(mp(ti,tj));
			//sp[ti][tj] = '+';
			ps.insert(ti+tj); pd.insert(ti-tj);
			score++;
		}
		if (c=='o' || c=='x'){
			cross.pb(mp(ti,tj));
			//sc[ti][tj] = 'x';
			ci.insert(ti); cj.insert(tj);
			score++;
		}
		f[ti][tj] = c;
	}
	memcpy(f2, f, sizeof(char)*100*100);
	//add cross component
	vector<int> remi, remj;
	for(int i=0;i<n;i++) if (ci.find(i)==ci.end()) remi.pb(i);
	for(int j=0;j<n;j++) if (cj.find(j)==cj.end()) remj.pb(j);
	for(int k=0;k<remi.size();k++){
		if (f2[remi[k]][remj[k]]=='.'){
			f2[remi[k]][remj[k]] = 'x';
		}else f2[remi[k]][remj[k]] = 'o';
	}
	score += remi.size();

	//add plus component
	for(int i=0;i<n;i++){
		if (0<i && i+1<n) continue;
		for(int j=0;j<n;j++){
			if (ps.find(i+j)==ps.end() && pd.find(i-j)==pd.end()){
				if (f2[i][j]=='.'){
					f2[i][j] = '+';
				}else f2[i][j] = 'o';
				ps.insert(i+j); pd.insert(i-j);
				score++;
			}
		}
	}
	for(int j=0;j<n;j++){
		if (0<j && j+1<n) continue;
		for(int i=0;i<n;i++){
			if (ps.find(i+j)==ps.end() && pd.find(i-j)==pd.end()){
				if (f2[i][j]=='.'){
					f2[i][j] = '+';
				}else f2[i][j] = 'o';
				ps.insert(i+j); pd.insert(i-j);
				score++;
			}
		}
	}	


	//output
	vector<char> ans_c;
	vector<int> ans_i, ans_j;
	for(int i=0;i<n;i++){
		for(int j=0;j<n;j++){
			if (f[i][j] != f2[i][j]){
				ans_c.pb(f2[i][j]);
				ans_i.pb(i); ans_j.pb(j);
			}
		}
	}
	cout << score << " " << ans_c.size() << endl;
	for(int i=0;i<ans_c.size();i++){
		cout << ans_c[i] << " " << ans_i[i]+1 << " " << ans_j[i]+1 << endl;
	}
	return;
}

int main(void){
	int T;
	cin >> T;
	for(int tcnt=1;tcnt<=T;tcnt++){
		cout << "Case #" << tcnt << ": ";
		solve();
	}
	return 0;
}