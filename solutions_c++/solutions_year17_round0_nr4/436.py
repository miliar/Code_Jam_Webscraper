#include <iostream>
#include <string>
#include <cstdio>
#include <ctype.h>
#include <limits.h>
#include <cmath>
#include <algorithm>
#include <utility>
#include <vector>
#include <unordered_set>
#include <unordered_map>
#include <array>
#include <queue>
using namespace std; 

#define gc getchar_unlocked
#define lli long long int
#define ld long double

class FastInput{
private:
	template <class T>
	inline static T nextInteger(){
		int c = gc();
		T x = 0;
		bool neg = 0;
		for (; ((c < 48 || c > 57) && c != '-'); c = gc());
		if (c == '-') {
			neg = 1;
			c = gc();
		}
		for (; c > 47 && c < 58 ; c = gc()) {
			x = (x << 1) + (x << 3) + c - 48;
		}
		if (neg)
			x = -x;
		return x;
	}
public:
	inline static int nextInt(){
		return nextInteger<int>();
	}

	inline static lli nextLong(){
		return nextInteger<lli>();
	}

	inline static string nextString(){
		string str = "";
		char c = gc();

		while (c >= 0 && c < 33)
			c = gc();

		while (!isspace(c) && c >= 0) {
			str += c;
			c = gc();
		}
		return str;
	}

	inline static string nextLine(){
		string str = "";
				char c = gc();

		while (c >= 0 && c < 33)
			c = gc();

		while (c != '\n' && c >= 0) {
			str += c;
			c = gc();
		}
		return str;
	}

	inline static ld nextDouble(){
		string str = nextString();
		ld res = {stold(str)};
		return res;
	}
};

struct pair_hash {
    template <class T1, class T2>
    std::size_t operator () (const std::pair<T1,T2> &p) const {
        auto h1 = std::hash<T1>{}(p.first);
        auto h2 = std::hash<T2>{}(p.second);

        // Mainly for demonstration purposes, i.e. works but is overly simple
        // In the real world, use sth. like boost.hash_combine
        return h1 ^ h2;  
    }
};

class Allow{
public:
	bool plus;
	bool cross;
	bool old;
	Allow(){
		plus = true;
		cross = true;
		old = true;
	}
	Allow(const Allow& allow){
		plus = allow.plus;
		cross = allow.cross;
		old = allow.old;
	}
	Allow get_combined(Allow allow){
		Allow new_allow = Allow();
		new_allow.plus = allow.plus && plus;
		new_allow.cross = allow.cross && cross;
		new_allow.old = allow.old && old;
		return new_allow;
	}
};

Allow ** get_allow_matrix(int N, char ** matrix){
	int add_dif = N - 1;
	int add_sum = -2;
	Allow * row_check = new Allow[N + 1];
	Allow * col_check = new Allow[N + 1];
	Allow * dif_check = new Allow[2 * N - 1];
	Allow * sum_check = new Allow[2 * N - 1];
	int row_set[N + 1];
	int col_set[N + 1];
	int dif_set[2 * N - 1];
	int sum_set[2 * N - 1];
	for (int i = 0; i <= N; i ++){
		row_set[i] = 0;
		col_set[i] = 0;
	}
	for (int i = 0; i < 2 * N - 1; i ++){
		dif_set[i] = 0;
		sum_set[i] = 0;
	}
	for (int i = 1; i <= N; i ++){
		for (int j = 1; j <= N; j ++){
			if (matrix[i][j] == '+'){
				int dif = i - j;
				dif_check[dif + add_dif].plus = false;
				dif_check[dif + add_dif].old = false;
				dif_set[dif + add_dif] ++;
				int sum = i + j;
				sum_check[sum + add_sum].plus = false;
				sum_check[sum + add_sum].old = false;
				sum_set[sum + add_sum] ++;
			} else if (matrix[i][j] == 'x'){
				row_check[i].cross = false;
				col_check[j].cross = false;
				row_check[i].old = false;
				row_set[i] ++;
				col_check[j].old = false;
				col_set[j] ++;
			} else if (matrix[i][j] == 'o'){
				int dif = i - j;
				dif_check[dif + add_dif].plus = false;
				dif_set[dif + add_dif] ++;
				dif_check[dif + add_dif].old = false;
				int sum = i + j;
				sum_check[sum + add_sum].plus = false;
				sum_set[sum + add_sum] ++;
				sum_check[sum + add_sum].old = false;
				row_check[i].cross = false;
				row_set[i] ++;
				row_check[i].old = false;
				col_check[j].cross = false;
				col_set[j] ++;
				col_check[j].old = false;
			}
		}
	}
	Allow ** allow_matrix = new Allow*[N + 1];
	for (int i = 0; i <= N; i ++)
		allow_matrix[i] = new Allow[N + 1];
	for (int i = 1; i <= N; i ++)
		for (int j = 1; j <= N; j ++){
			int dif = i - j;
			Allow allow = Allow(dif_check[dif + add_dif]);
			int sum = i + j;
			allow = allow.get_combined(sum_check[sum + add_sum]);
			allow = allow.get_combined(row_check[i]);
			allow = allow.get_combined(col_check[j]);
			if (matrix[i][j] == 'o'){
				allow.cross = false;
				allow.plus = false;
				allow.old = false;
			} else if (matrix[i][j] != '.'){
				allow.cross = false;
				allow.plus = false;
				int dif = i - j;
				int sum = i + j;
				bool res = true;
				if (matrix[i][j] == '+'){
					if (dif_set[dif + add_dif] > 1) res = false;
					if (sum_set[sum + add_sum] > 1) res = false;
					if (row_set[i] > 0) res = false;
					if (col_set[j] > 0) res = false;
				} else if (matrix[i][j] == 'x'){
					if (row_set[i] > 1) res = false;
					if (col_set[j] > 1) res = false;
					if (dif_set[dif + add_dif] > 0) res = false;
					if (sum_set[sum + add_sum] > 0) res = false;
				}
				allow.old = res;
			}
			allow_matrix[i][j] = allow;
		}
	delete[] row_check;
	delete[] col_check;
	delete[] dif_check;
	delete[] sum_check;
	return allow_matrix;
}

int main(){
	int T = FastInput::nextInt();
	for (int t = 1; t <= T; t ++){
		int N = FastInput::nextInt();
		int add_dif = N - 1;
		int add_sum = -2;
		int M = FastInput::nextInt();
		char ** matrix = new char*[N + 1];
		char ** old_matrix = new char*[N + 1];
		for (int i = 1; i <= N; i ++){
			matrix[i] = new char[N + 1];
			old_matrix[i] = new char[N + 1];
		}
		for (int i = 1; i <= N; i ++)
			for (int j = 1; j <= N; j ++){
				matrix[i][j] = '.';
				old_matrix[i][j] = '.';
			}
		for (int i = 0; i < M; i ++){
			string c = FastInput::nextString();
			int R = FastInput::nextInt();
			int C = FastInput::nextInt();
			matrix[R][C] = c[0];
			old_matrix[R][C] = c[0];
		}
		//MASS ADD
		Allow ** allow_matrix = get_allow_matrix(N, matrix);
		int dif_set[2 * N - 1];
		int sum_set[2 * N - 1];
		for (int i = 0; i < 2 * N - 1; i ++){
			dif_set[i] = 0;
			sum_set[i] = 0;
		}
		for (int idx = 0; idx < (N + 1) / 2; idx ++){
			int row_below = N - idx;
			for (int j = 1; j <= N; j ++){
				int dif_idx = row_below - j + add_dif;
				int sum_idx = row_below + j + add_sum;
				if (matrix[row_below][j] == '.' && allow_matrix[row_below][j].plus && dif_set[dif_idx] == 0 && sum_set[sum_idx] == 0){
					matrix[row_below][j] = '+';
					dif_set[dif_idx] ++;
					sum_set[sum_idx] ++;
				}
			}
			int row_above = idx + 1;
			for (int j = 1; j <= N; j ++){
				int dif_idx = row_above - j + add_dif;
				int sum_idx = row_above + j + add_sum;
				if (matrix[row_above][j] == '.' && allow_matrix[row_above][j].plus && dif_set[dif_idx] == 0 && sum_set[sum_idx] == 0){
					matrix[row_above][j] = '+';
					dif_set[dif_idx] ++;
					sum_set[sum_idx] ++;
				}
			}
		}
		int row_set[N + 1];
		int col_set[N + 1];
		for (int i = 0; i <= N; i ++){
			row_set[i] = 0;
			col_set[i] = 0;
		}
		for (int i = 1; i <= N; i ++){
			for (int j = 1; j <= N; j ++){
				if (matrix[i][j] == '.' && allow_matrix[i][j].cross && row_set[i] == 0 && col_set[j] == 0){
					matrix[i][j] = 'x';
					row_set[i] ++;
					col_set[j] ++;
				}
			}
		}
		for (int i = 1; i <= N; i ++)
			delete[] allow_matrix[i];
		delete[] allow_matrix;
		//PLUS ADD
		allow_matrix = get_allow_matrix(N, matrix);
		unordered_map<pair<int, int>, int, pair_hash> map_score;
		int * dif_count = new int[2 * N - 1];
		int * sum_count = new int[2 * N - 1];
		for (int i = 0; i < 2 * N - 1; i ++){
			dif_count[i] = 0;
			sum_count[i] = 0;
		}
		for (int i = 1; i <= N; i ++)
			for (int j = 1; j <= N; j ++){
				if (allow_matrix[i][j].plus){
					dif_count[i - j + add_dif] ++;
					sum_count[i + j + add_sum] ++;
					map_score.insert({{i, j}, 0});
				}
			}
		while (true){
			int total = map_score.size();
			if (total == 0) break;
			for (auto& p : map_score){
				auto& pos = p.first;
				int row = pos.first, col = pos.second;
				int prohibit = 0;
				prohibit += (dif_count[row - col + add_dif] - 1);
				prohibit += (sum_count[row + col + add_sum] - 1);
				map_score[pos] = total - prohibit;
			}
			pair<int, int> max_pair;
			int max_score = -1;
			for (auto& p : map_score){
				if (max_score < p.second){
					max_score = p.second;
					max_pair = p.first;
				}
			}
			matrix[max_pair.first][max_pair.second] = '+';
			for (int i = 1; i <= N; i ++){
				int col_sum = max_pair.first + max_pair.second - i;
				int col_dif = i - max_pair.first + max_pair.second;
				if (map_score.count({i, col_sum})){
					dif_count[i - col_sum + add_dif] --;
					sum_count[i + col_sum + add_sum] --;
					map_score.erase({i, col_sum});
				}
				if (map_score.count({i, col_dif})){
					dif_count[i - col_dif + add_dif] --;
					sum_count[i + col_dif + add_sum] --;
					map_score.erase({i, col_dif});
				}
			}
		}
		delete[] dif_count;
		delete[] sum_count;
		for (int i = 1; i <= N; i ++)
			delete[] allow_matrix[i];
		delete[] allow_matrix;
		// CROSS ADD
		allow_matrix = get_allow_matrix(N, matrix);
		unordered_map<pair<int, int>, int, pair_hash> map2_score;
		int * row_count = new int[N + 1];
		int * col_count = new int[N + 1];
		for (int i = 0; i <= N; i ++){
			row_count[i] = 0;
			col_count[i] = 0;
		}
		for (int i = 1; i <= N; i ++)
			for (int j = 1; j <= N; j ++){
				if (allow_matrix[i][j].cross){
					row_count[i] ++;
					col_count[j] ++;
					map2_score.insert({{i, j}, 0});
				}
			}
		while (true){
			int total = map2_score.size();
			if (total == 0) break;
			for (auto& p : map2_score){
				auto& pos = p.first;
				int row = pos.first, col = pos.second;
				int prohibit = 0;
				prohibit += (row_count[row] - 1);
				prohibit += (col_count[col] - 1);
				map2_score[pos] = total - prohibit;
			}
			pair<int, int> max_pair;
			int max_score = -1;
			for (auto& p : map2_score){
				if (max_score < p.second){
					max_score = p.second;
					max_pair = p.first;
				}
			}
			matrix[max_pair.first][max_pair.second] = 'x';
			for (int i = 1; i <= N; i ++){
				if (map2_score.count({max_pair.first, i})){
					row_count[max_pair.first] --;
					col_count[i] --;
					map2_score.erase({max_pair.first, i});
				}
				if (map2_score.count({i, max_pair.second})){
					row_count[i] --;
					col_count[max_pair.second] --;
					map2_score.erase({i, max_pair.second});	
				}
			}
		}
		
		delete[] row_count;
		delete[] col_count;
		for (int i = 1; i <= N; i ++)
			delete[] allow_matrix[i];
		delete[] allow_matrix;
		// OLD ADD
		allow_matrix = get_allow_matrix(N, matrix);
		unordered_map<pair<int, int>, int, pair_hash> map3_score;
		row_count = new int[N + 1];
		col_count = new int[N + 1];
		for (int i = 0; i <= N; i ++){
			row_count[i] = 0;
			col_count[i] = 0;
		}
		dif_count = new int[2 * N - 1];
		sum_count = new int[2 * N - 1];
		for (int i = 0; i < 2 * N - 1; i ++){
			dif_count[i] = 0;
			sum_count[i] = 0;
		}
		for (int i = 1; i <= N; i ++)
			for (int j = 1; j <= N; j ++){
				if (allow_matrix[i][j].old){
					row_count[i] ++;
					col_count[j] ++;
					dif_count[i - j + add_dif] ++;
					sum_count[i + j + add_sum] ++;
					map3_score.insert({{i, j}, 0});
				}
			}
		while (true){
			int total = map3_score.size();
			if (total == 0) break;
			for (auto& p : map3_score){
				auto& pos = p.first;
				int row = pos.first, col = pos.second;
				int prohibit = 0;
				prohibit += (row_count[row] - 1);
				prohibit += (col_count[col] - 1);
				prohibit += (dif_count[row - col + add_dif] - 1);
				prohibit += (sum_count[row + col + add_sum] - 1);
				map3_score[pos] = total - prohibit;
			}
			pair<int, int> max_pair;
			int max_score = -1;
			for (auto& p : map3_score){
				if (max_score < p.second){
					max_score = p.second;
					max_pair = p.first;
				}
			}
			matrix[max_pair.first][max_pair.second] = 'o';
			for (int i = 1; i <= N; i ++){
				int col_sum = max_pair.first + max_pair.second - i;
				int col_dif = i - max_pair.first + max_pair.second;
				if (map3_score.count({max_pair.first, i})){
					row_count[max_pair.first] --;
					col_count[i] --;
					map3_score.erase({max_pair.first, i});
				}
				if (map3_score.count({i, max_pair.second})){
					row_count[i] --;
					col_count[max_pair.second] --;
					map3_score.erase({i, max_pair.second});	
				}
				if (map3_score.count({i, col_sum})){
					dif_count[i - col_sum + add_dif] --;
					sum_count[i + col_sum + add_sum] --;
					map_score.erase({i, col_sum});
				}
				if (map3_score.count({i, col_dif})){
					dif_count[i - col_dif + add_dif] --;
					sum_count[i + col_dif + add_sum] --;
					map_score.erase({i, col_dif});
				}
			}
		}
		delete[] row_count;
		delete[] col_count;
		delete[] dif_count;
		delete[] sum_count;
		int change_count = 0;
		int point = 0;
		for (int i = 1; i <= N; i ++)
			for (int j = 1; j <= N; j ++){
				if (old_matrix[i][j] != matrix[i][j])
					change_count ++;
				if (matrix[i][j] == 'o') point += 2;
				else if (matrix[i][j] != '.') point ++;
			}
		cout << "Case #" << t << ": " << point << " " << change_count << endl;
		for (int i = 1; i <= N; i ++)
			for (int j = 1; j <= N; j ++){
				if (old_matrix[i][j] != matrix[i][j]){
					cout << matrix[i][j] << " " << i << " " << j << endl;
				}
			}
		for (int i = 1; i <= N; i ++){
			delete[] matrix[i];
			delete[] old_matrix[i];
			delete[] allow_matrix[i];
		}
		delete[] matrix;
		delete[] old_matrix;
		delete[] allow_matrix;
	}
	return 0;
}