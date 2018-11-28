#include <algorithm>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <string>
#include <vector>
#include <cmath>
#include <queue>
#include <set>
#include <map>
using namespace std;
typedef pair<int,int> pii;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef long long ll;

#define r first
#define c second

vector< vector<char> > grid;
vector<pair<int, int> > vars;
vector<pair<int, int> > empties;
map< pair<int, int>, int> indices;
vector< vector<int> > clauses;
map< pair<int, int>, int> indices2;
set<int> graph[200];
bool marked[200];
bool assigned[100];
bool good[100];

int rows, cols;

vector<pair<int, int> > add(int r, int c, int dr, int dc){
	vector<pair<int, int> > v;
	if(r==-1 || r==rows || c==-1 || c==cols || grid[r][c] == '#'){
		return v;
	}
	if(grid[r][c] == '/'){
		v = add(r-dc, c-dr, -dc, -dr);
	}
	if(grid[r][c] == '\\'){
		v = add(r+dc, c+dr, dc, dr);
	}
	if(grid[r][c] == '.'){
		v = add(r+dr, c+dc, dr, dc);
		v.push_back(make_pair(r, c));
	}
	if(grid[r][c] == '-' || grid[r][c] == '|'){
		v.push_back(make_pair(-1, -1));
	}
	return v;
}

bool goon;

int no(int x){
	if(x>=100){
		return x-100;
	}
	else{
		return x+100;
	}
}

bool dfs(int start, int end){
	//cout << "from" << start << endl;
	//cout << "getting" << end << endl;
	if(marked[start]) return false;
	if(start==end) {
		//cout << "yeh?" << endl;
		return true;
	}
	marked[start] = true;
	for(auto i : graph[start]){
		//cout << "to" << i << endl;
		if(dfs(i, end)) return true;
	}
	return false;
}

void dfs2(int start){
	if(assigned[start]) return;
	assigned[start] = true;
	for(auto i : graph[start]){
		if(i>=100){
			good[i-100] = false;
		}
		else{
			good[i] = true;
		}
		dfs2(i);
	}
	
	return;
}

int main() {
	int t;
	cin >> t;
	for(int i=1; i<=t; i++){
		grid.clear();
		vars.clear();
		empties.clear();
		clauses.clear();
		indices.clear();
		indices2.clear();
		for(int i=0; i<200; i++){
			graph[i].clear();
		}
		goon = false;
		cin >> rows >> cols;
		for(int i=0; i<rows; i++){
			vector<char> u;
			for(int j=0; j<cols; j++){
				char x;
				cin >> x;
				u.push_back(x);
				
			}
			grid.push_back(u);
			
		}
		for(int i=0; i<rows; i++){

			for(int j=0; j<cols; j++){
				//cout << grid[i][j] << endl;
				if(grid[i][j] == '.'){
					indices[make_pair(i, j)] = empties.size();
					empties.push_back(make_pair(i, j));
					vector<int> v;
					clauses.push_back(v);
				
				}
				if(grid[i][j] == '-' || grid[i][j] == '|'){
					indices2[make_pair(i, j)] = vars.size();
					vars.push_back(make_pair(i, j));
				}
				
			}
			
			
		}
		
		bool goon = false;
		for(int i=0; i<vars.size(); i++){ 
			vector<pair<int, int> > u;
			vector<pair<int, int> > v;
			u = add(vars[i].r+1, vars[i].c, 1, 0);
			v = add(vars[i].r-1, vars[i].c, -1, 0);
			if(!((u.size()>=1 && u[0].r == -1) || (v.size()>=1 && v[0].r == -1))){
				for(int j=0; j<u.size(); j++){
					clauses[indices[u[j]]].push_back(i+100);
				}
				for(int j=0; j<v.size(); j++){
					clauses[indices[v[j]]].push_back(i+100);
				}
			}else{
				//cout << i << endl;
				graph[i+100].insert(i);

			}
			u = add(vars[i].r, vars[i].c+1, 0, 1);
			v = add(vars[i].r, vars[i].c-1, 0, -1);
			if(!((u.size()>=1 && u[0].r == -1) || (v.size()>=1 && v[0].r == -1))){
				for(int j=0; j<u.size(); j++){
					clauses[indices[u[j]]].push_back(i);
				}
				for(int j=0; j<v.size(); j++){
					clauses[indices[v[j]]].push_back(i);
				}
			}else{
				//cout << i+100 << endl;
				graph[i].insert(i+100);
			}
		}
		for(int i=0; i<clauses.size(); i++){
			//cout << clauses[i].size() << endl;
			//cout << "_______" << endl;
			//for(int j=0; j<clauses[i].size(); j++){
				//cout << clauses[i][j] << endl;
			//}
			//cout << endl;
			if(clauses[i].size()==0){
				//cout << "here" << endl;
				goon = true;
			}
			if(clauses[i].size()==2){
				int x = clauses[i][0];
				int y = clauses[i][1];
				
				if(x-y==100 || y-x==100) continue;
				//cout << x << " " << y << endl;
				graph[no(x)].insert(y);
				graph[no(y)].insert(x);
			}
			if(clauses[i].size()==1){
				
				int x = clauses[i][0];
				graph[no(x)].insert(x);
			}
			
		}
		bool possible[200];
		for(int i=0; i<vars.size(); i++){
			for(int j=0; j<vars.size()+100; j++){
				marked[j] = false;
			}
			possible[i] = true;
			if(dfs(i, i+100)) {
				possible[i] = false;	
			}
			for(int j=0; j<vars.size()+100; j++){
				marked[j] = false;
			}
			possible[i+100] = true;
			if(dfs(i+100, i)) {
				possible[i+100] = false;	
			}
			if(!possible[i] && !possible[i+100]){
				//cout << i << endl;
				goon = true;
			}
		}
		for(int i=0; i<vars.size(); i++){
			//cout << possible[i] << " " << possible[i+100] << endl;
		}
		
		if(goon){
			cout << "Case #" << i << ": IMPOSSIBLE" << endl; 
			continue;
		}
		

		for(int i=0; i<vars.size(); i++){
			assigned[i] = false;
		}
		for(int i=0; i<vars.size(); i++){
			if(!assigned[i]){
				if(possible[i]){
					good[i] = true;
					dfs2(i);
				}
				else{
					good[i] = false;
					dfs2(i+100);
				}
			}
		}
		cout << "Case #" << i << ": POSSIBLE" << endl; 
		for(int i=0; i<rows; i++){
			for(int j=0; j<cols; j++){
				if(grid[i][j]!='-' && grid[i][j]!='|')
					cout << grid[i][j];	
				else{
					if(good[indices2[make_pair(i,j)]]){
						cout << '-';
					}
					else{
						cout << '|';
					}
				}
			}
			cout << endl;
			
		}
	}	
}





