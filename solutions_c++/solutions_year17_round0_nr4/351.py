#include <iostream>
#include <algorithm>
#include <set>
#include <vector>
using namespace std;
typedef long long ll;
struct model{char type;ll row;ll col;};
bool comp(const ll lhs, const ll rhs){
	if(abs(lhs) != abs(rhs)){return abs(lhs) > abs(rhs);}
	return lhs > rhs;
}
vector<model> calc(ll N, vector<model> models){
	set<ll> rows_with_x,cols_with_x;
	vector<ll> diag_left,diag_right;
	ll points = 0;
	for(ll i = 0; i < models.size(); i++){
		if(models[i].type=='o'){
			rows_with_x.insert(models[i].row);
			cols_with_x.insert(models[i].col);
			diag_left.push_back(models[i].row-models[i].col);
			diag_right.push_back(models[i].row+models[i].col-N-1);
			points += 2;
		}
		else if(models[i].type=='x'){
			rows_with_x.insert(models[i].row);
			cols_with_x.insert(models[i].col);
			points++;
		}
		else if(models[i].type=='+'){
			diag_left.push_back(models[i].row-models[i].col);
			diag_right.push_back(models[i].row+models[i].col-N-1);
			points++;
		}
	}
	vector<ll> rows_without_x, cols_without_x;
	for(ll i = 1; i <= N; i++){
		if(rows_with_x.count(i)==0){rows_without_x.push_back(i);}
		if(cols_with_x.count(i)==0){cols_without_x.push_back(i);}
	}
	vector<ll> diag_index;
	for(ll i = N-1; i >= -N+1; i--){diag_index.push_back(i);}
	sort(diag_index.begin(),diag_index.end(),comp);
	vector<ll> tmp_row,tmp_col;
	for(ll d_diag : diag_index){
		for(ll p_diag : diag_index){
			ll testCol = (p_diag-d_diag+N+1)/2;
			ll testRow = (d_diag+p_diag+N+1)/2;
			if((d_diag+p_diag+N+1)%2!=0 || testRow < 1 || testRow>N || testCol < 1 || testCol > N){continue;}
			bool crossing_diags = true;
			for(ll diag : diag_left){
				if(diag == d_diag){crossing_diags = false;break;}
			}
			for(ll diag : diag_right){
				if(diag == p_diag){crossing_diags = false;break;}
			}
			if(crossing_diags){
				tmp_row.push_back(testRow);
				tmp_col.push_back(testCol);
				diag_left.push_back(testRow-testCol);
				diag_right.push_back(testRow+testCol-N-1);
			}
		}
	}
	vector<model> newmodels;
	ll changes = 0;
	for(ll i = 0; i < rows_without_x.size(); i++){
		ll row = rows_without_x[i];
		ll col = cols_without_x[i];
		char type = 'x';
		for(ll j = 0; j < models.size(); j++){
			if(models[j].row ==row && models[j].col==col)type = 'o';
		}
		for(ll j = 0; j < tmp_row.size(); j++){
			if(tmp_row[j]==row && tmp_col[j]==col){
				type = 'o';
				points++;
				tmp_row[j] = -1;
				tmp_col[j] = -1;
			}
		}
		model current;
		current.type = type;
		current.row = row;
		current.col = col;
		newmodels.push_back(current);
		changes++;
		points++;
	}
	for(ll i = 0; i < tmp_row.size(); i++){
		ll row = tmp_row[i];
		ll col = tmp_col[i];
		if(row == -1 || col == -1)continue;
		char type = '+';
		for(ll j = 0; j < models.size(); j++){
			if(models[j].row ==row && models[j].col ==col){
				type = 'o';
			}
		}
		model current;
		current.type = type;
		current.row = row;
		current.col = col;
		newmodels.push_back(current);
		changes++;
		points++;
	}
	cout << points << " " << changes << endl;
	return newmodels;
}

int main(){
	ll t;
	cin >> t;
	for (ll c = 1; c <= t; c++) {
		ll n,m;
		cin >> n >> m;
		vector<model> models(m);
		for(ll j = 0; j < m; j++){
			char type;ll row,col;
			cin >> type >> row >> col;
			model current;
			current.type = type;
			current.row = row;
			current.col = col;
			models[j] = current;
		}
		cout << "Case #" << c << ": ";
		vector<model> ans = calc(n, models);
		for(ll i = 0; i < ans.size(); i++){
			cout << ans[i].type << ' ' << ans[i].row << ' ' << ans[i].col << endl;
		}
	}
}