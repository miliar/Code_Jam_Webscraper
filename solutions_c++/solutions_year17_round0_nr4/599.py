#include <iostream>
#include <cstdlib>
#include <cstring>

using namespace std;

const int N_MAX = 100;
const int A_MAX = N_MAX * N_MAX;
const int A_LEN = A_MAX / 4 + 2;

char sym_to_num(const char& ch) {
	switch(ch) {
	case '+': return 1;
	case 'x': return 2;
	case 'o': return 3;
	}
	return -1;
}

const char num_to_sym[4] = {'.', '+', 'x', 'o'};

void print_mat(const char* mat, const int& nrow, const int& ncol) {
	int id, iu, iv;

	for(int j = 0; j < nrow; ++j){
		for(int k = 0; k < ncol; ++k){
			id = j * N_MAX + k;
			iu = id / 4;
			iv = id % 4 * 2;
			cout << (short)(mat[iu] >> iv & 3) << " ";
		}
		cout << endl;
	}
}

void lay(char* grid, char* mask, const int& n,
		const int& row, const int& col, const char& num) {
	int id = row * N_MAX + col;
	int iu = id / 4;
	int iv = id % 4 * 2;
	int jd, ju, jv, lb, ub;

	grid[iu] ^= (grid[iu] >> iv & 3 ^ num) << iv;
	if(num & 2) {
		for(int j = 0; j < n; ++j) {
			jd = row * N_MAX + j;
			ju = jd / 4;
			jv = jd % 4 * 2;
			mask[ju] &= ~(2 << jv);
			jd = j * N_MAX + col;
			ju = jd / 4;
			jv = jd % 4 * 2;
			mask[ju] &= ~(2 << jv);
		}
	}
	if(num & 1) {
		lb = 0;
		ub = n - 1;
		if(row + col > n - 1) lb = row + col - n + 1;
		if(row + col < n - 1) ub = row + col;
		for(int j = lb; j <= ub; ++j) {
			jd = j * N_MAX + row + col - j;
			ju = jd / 4;
			jv = jd % 4 * 2;
			mask[ju] &= ~(1 << jv);
		}
		lb = 0;
		ub = n - 1;
		if(row - col > 0) lb = row - col;
		if(row - col < 0) ub = row - col + n - 1;
		for(int j = lb; j <= ub; ++j) {
			jd = j * N_MAX + col - row + j;
			ju = jd / 4;
			jv = jd % 4 * 2;
			mask[ju] &= ~(1 << jv);
		}
	}
}

int solve_small(char* grid, char* mask, const int& n, const int& score) {
	int id, iu, iv;
	int score_res = score;

	// deploy x models
	for(int j = 0; j < n; ++j) {
		for(int k = 0; k < n; ++k) {
			id = j * N_MAX + k;
			iu = id / 4;
			iv = id % 4 * 2;
			if(mask[iu] >> iv & 2) {
				lay(grid, mask, n, j, k, grid[iu] >> iv & 3 | 2);
				++score_res;
			}
		}
	}

	// deploy + models
	for(int k = 0; k < n; ++k) {
		id = k;
		iu = id / 4;
		iv = id % 4 * 2;
		if(mask[iu] >> iv & 1) {
			lay(grid, mask, n, 0, k, grid[iu] >> iv & 3 | 1);
			++score_res;
		}
	}
	for(int k = 1; k < n - 1; ++k) {
		id = (n - 1) * N_MAX + k;
		iu = id / 4;
		iv = id % 4 * 2;
		if(mask[iu] >> iv & 1) {
			lay(grid, mask, n, n - 1, k, grid[iu] >> iv & 3 | 1);
			++score_res;
		}
	}
	return score_res;
}

int main(int argc, char* argv[]) {
	int T;

	cin >> T;
	for(int repeat = 1; repeat <= T; ++repeat) {
		int n, m;
		string mark;
		int x, y;
		char preset[A_MAX][3] = {0};

		cin >> n >> m;
		for(int ind = 0; ind < m; ++ind) {
			cin >> mark >> x >> y;
			preset[ind][0] = sym_to_num(mark.c_str()[0]);
			preset[ind][1] = x - 1;
			preset[ind][2] = y - 1;
		}
		cout << "Case #" << repeat << ": "; 

		char grid[A_LEN] = {0};
		char mask[A_LEN] = {0};
		int score = 0;

		memset(mask, -1, A_LEN);
		// cout << endl; print_mat(grid, n, n);
		// cout << endl; print_mat(mask, n, n);

		for(int ind = 0; ind < m; ++ind) {
			char* cmd = preset[ind];
			lay((char*)grid, (char*)mask, n, cmd[1], cmd[2], cmd[0]);
			if(cmd[0] == 3) {
				score += 2;
			} else ++score;
		}
		// cout << endl; print_mat(grid, n, n);
		// cout << endl; print_mat(mask, n, n);

		char grid_res[A_LEN];
		char mask_res[A_LEN];
		int score_res;

		memcpy(grid_res, grid, A_LEN);
		memcpy(mask_res, mask, A_LEN);
		score_res = solve_small(grid_res, mask_res, n, score);

		// compare result and original grid
		int id, iu, iv;
		int count_diff = 0;
		char oprset[A_MAX][3] = {0};
		char grid_res_j;

		for(char j = 0; j < n; ++j) {
			for(char k = 0; k < n; ++k) {
				id = j * N_MAX + k;
				iu = id / 4;
				iv = id % 4 * 2;
				grid_res_j = grid_res[iu] >> iv & 3;
				if(grid_res_j > (grid[iu] >> iv & 3)) {
					oprset[count_diff][0] = grid_res_j;
					oprset[count_diff][1] = j;
					oprset[count_diff][2] = k;
					++count_diff;
				}
			}
		}
		cout << score_res << " " << count_diff << endl;
		for(int ind = 0; ind < count_diff; ++ind) {
			cout << num_to_sym[oprset[ind][0]] << " "
					<< oprset[ind][1] + 1 << " "
					<< oprset[ind][2] + 1 << endl;
		}
		// cout << endl; print_mat(grid_res, n, n);
		// cout << endl; print_mat(mask_res, n, n);
	}
	return 0;
}