#include<iostream>
#include<fstream>
#include<vector>
#include<string>
#include<list>
#include<tuple>
#include<map>

using namespace std;

class Grid {
private:
	int N;
	int N2;
	int score;
	map<char, int> num;
	vector<vector<char>> cells;
	vector<map<char, int>> check_row;
	vector<map<char, int>> check_col;
	vector<map<char, int>> check_sum;
	vector<map<char, int>> check_diff;
	vector<int> total_NG_row;
	vector<int> total_NG_col;
	vector<int> total_NG_sum;
	vector<int> total_NG_diff;

public:
	Grid(int N) {
		this->N = N;
		this->N2 = N*N;
		this->score = 0;
		this->cells.resize(this->N);
		for (auto& rows : this->cells) {
			rows.assign(this->N, '.');
		}
		this->check_row.assign(this->N, { { '+', 0 },{ 'x', 0 },{ 'o', 0 } });
		this->check_col.assign(this->N, { { '+', 0 },{ 'x', 0 },{ 'o', 0 } });
		this->check_sum.assign(this->N * 2 - 1, { { '+', 0 },{ 'x', 0 },{ 'o', 0 } });
		this->check_diff.assign(this->N * 2 - 1, { { '+', 0 },{ 'x', 0 },{ 'o', 0 } });

		this->total_NG_row.assign(this->N, 0);
		this->total_NG_col.assign(this->N, 0);
		this->total_NG_sum.assign(this->N * 2 - 1, 0);
		this->total_NG_diff.assign(this->N * 2 - 1, 0);

		this->num = { { '+', 0 },{ 'x', 0 },{ 'o', 0 } };
	}

	void set(char model, int row0, int col0) {
		auto row = row0 - 1;
		auto col = col0 - 1;
		auto sum = row + col;
		auto diff = row - col + this->N - 1;

		auto pre_model = this->cells[row][col];
		this->cells[row][col] = model;

		this->check_row[row][pre_model]--;
		this->check_col[col][pre_model]--;
		this->check_sum[sum][pre_model]--;
		this->check_diff[diff][pre_model]--;
		if (pre_model == '+') this->score -= 1;
		if (pre_model == 'x') this->score -= 1;
		if (pre_model == 'o') this->score -= 2;
		this->num[pre_model]--;

		this->check_row[row][model]++;
		this->check_col[col][model]++;
		this->check_sum[sum][model]++;
		this->check_diff[diff][model]++;
		if (model == '+') this->score += 1;
		if (model == 'x') this->score += 1;
		if (model == 'o') this->score += 2;
		this->num[model]++;

		this->total_NG_row[row] = this->check_row[row]['x'] + this->check_row[row]['o'];
		this->total_NG_col[col] = this->check_col[col]['x'] + this->check_col[col]['o'];
		this->total_NG_sum[sum] = this->check_sum[sum]['+'] + this->check_sum[sum]['o'];
		this->total_NG_diff[diff] = this->check_diff[diff]['+'] + this->check_diff[diff]['o'];
	}

	int get_grid_size() {
		return this->N;
	}

	char get_cell(int row, int col) {
		return this->cells[row - 1][col - 1];
	}

	int get_score() {
		return this->score;
	}

	void debug() {
		cout << "===" << endl;
		cout << "score: " << this->score << endl;
		cout << "total_NG_row : ("; for (auto val : this->total_NG_row) { cout << " " << val; } cout << " )" << endl;
		cout << "total_NG_col : ("; for (auto val : this->total_NG_col) { cout << " " << val; } cout << " )" << endl;
		cout << "total_NG_sum : ("; for (auto val : this->total_NG_sum) { cout << " " << val; } cout << " )" << endl;
		cout << "total_NG_diff: ("; for (auto val : this->total_NG_diff) { cout << " " << val; } cout << " )" << endl;

		for (int row = 0; row < this->N; row++) {
			for (int col = 0; col < this->N; col++) {
				cout << this->cells[row][col];
			}
			cout << endl;
		}

		cout << endl;
	}

	bool is_legal(int row0, int col0) {
		auto row = row0 - 1;
		auto col = col0 - 1;
		auto sum = row + col;
		auto diff = row - col + this->N - 1;

		if (this->total_NG_row[row] > 1) return false;
		if (this->total_NG_col[col] > 1) return false;
		if (this->total_NG_sum[sum] > 1) return false;
		if (this->total_NG_diff[diff] > 1) return false;
		return true;
	}

	bool is_legal(char model, int row0, int col0) {
		auto row = row0 - 1;
		auto col = col0 - 1;
		auto sum = row + col;
		auto diff = row - col + this->N - 1;

		auto pre_model = this->cells[row][col];

		int pre_X = (pre_model == '+' || pre_model == 'o') ? 1 : 0;
		int pre_L = (pre_model == 'x' || pre_model == 'o') ? 1 : 0;
		int post_X = (model == '+' || model == 'o') ? 1 : 0;
		int post_L = (model == 'x' || model == 'o') ? 1 : 0;

		if (this->total_NG_row[row] - pre_L + post_L > 1) return false;
		if (this->total_NG_col[col] - pre_L + post_L > 1) return false;
		if (this->total_NG_sum[sum] - pre_X + post_X > 1) return false;
		if (this->total_NG_diff[diff] - pre_X + post_X > 1) return false;

		return true;
	}

	void depth_search(int* best_score, Grid* best_grid, int gridNo) {
		if (this->score > *best_score) {
			this->debug();
			*best_score = this->score;
			*best_grid = *this;
		}
		if (gridNo == this->N2) return;

		for (; gridNo < this->N2; gridNo++) {
			if (this->score +
				(this->N - this->num['o']) * 2 +
				(this->N - this->num['x']) +
				(this->N + this->N - 1 - this->num['+']) < *best_score) break;
			if (this->score + (this->N2 - gridNo) * 2 < *best_score) break;

			int row = gridNo / this->N + 1;
			int col = gridNo % this->N + 1;
			auto model = this->get_cell(row, col);
			auto next_grid = *this;
			if (model == '+' || model == 'x') {
				if (this->is_legal('o', row, col)) {
					next_grid.set('o', row, col);
					next_grid.depth_search(best_score, best_grid, gridNo + 1);
				}
			}
			else if (model == '.') {
				if (this->is_legal('o', row, col)) {
					next_grid.set('o', row, col);
					next_grid.depth_search(best_score, best_grid, gridNo + 1);
				}
				if (this->is_legal('+', row, col)) {
					next_grid.set('+', row, col);
					next_grid.depth_search(best_score, best_grid, gridNo + 1);
				}
				if (this->is_legal('x', row, col)) {
					next_grid.set('x', row, col);
					next_grid.depth_search(best_score, best_grid, gridNo + 1);
				}
			}
		}
	}
};


class Solver {
public:
	Solver(ifstream& ifs, ofstream& ofs) {
		int N;
		int M;
		ifs >> N >> M;
		Grid grid = Grid(N);

		for (int ii = 0; ii < M; ii++) {
			char model;
			int row;
			int col;
			ifs >> model >> row >> col;
			grid.set(model, row, col);
		}

		int index_of_o_or_x = 1;
		for (int ii = 1; ii <= N; ii++) {
			if (grid.get_cell(1, ii) == 'x' || grid.get_cell(1, ii) == 'o') {
				index_of_o_or_x = ii;
			}
		}

		Grid best_grid = grid;

		// first row
		for (int ii = 1; ii <= N; ii++) {
			if (ii == index_of_o_or_x) {
				best_grid.set('o', 1, ii);
			}
			else {
				best_grid.set('+', 1, ii);
			}
		}

		// diagonal 
		for (int ii = 1; ii < index_of_o_or_x; ii++) {
			best_grid.set('x', ii + 1, ii);
		}
		for (int ii = index_of_o_or_x + 1; ii <= N; ii++) {
			best_grid.set('x', ii , ii);
		}

		// last row
		for (int ii = 2; ii < N; ii++) {
			best_grid.set('+', N, ii);
		}
		if (index_of_o_or_x == N && N > 2) {
			best_grid.set('o', N, N-1);
		}

		// count changed cell
		int num_change = 0;
		for (int row = 1; row <= N; row++) {
			for (int col = 1; col <= N; col++) {
				if (grid.get_cell(row, col) != best_grid.get_cell(row, col)) num_change++;
			}
		}

		// output
		ofs << best_grid.get_score() << " " << num_change << endl;
		for (int row = 1; row <= N; row++) {
			for (int col = 1; col <= N; col++) {
				if (grid.get_cell(row, col) != best_grid.get_cell(row, col)) {
					ofs << best_grid.get_cell(row, col) << " " << row << " " << col << endl;
				}
			}
		}
	}
};

void main(int argc, char* argv[]) {
	string fname_i = argv[1];
	string fname_o = fname_i.substr(0, fname_i.find_last_of(".")) + ".out";
	ifstream ifs(fname_i);
	ofstream ofs(fname_o);

	int T;
	ifs >> T;
	for (int No = 1; No <= T; No++) {
		ofs << "Case #" << No << ": ";
		cout << "Case #" << No << "...";
		Solver(ifs, ofs);
		cout << endl;
	}
}
