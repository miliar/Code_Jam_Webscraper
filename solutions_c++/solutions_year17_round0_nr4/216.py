#include <iostream>
#include <algorithm>
#include <unordered_set>
#include <vector>
#include <cassert>

struct BipartiteMatching {
	// vector version
	// need to resize E
	int N, M;
	std::vector< std::vector<int> > E;
	std::vector<int> mL;
	std::vector<int> mR;
	std::vector<bool> V;
	int dfs(int u){
		if (u<0) return 1;
		if (V[u]) return 0;
		V[u] = 1;
		for (int i=0;i<E[u].size();++i) 
			if (dfs(mR[E[u][i]])) { 
				mL[u]=E[u][i], mR[E[u][i]]=u;
				return 1;
			}
		return 0;
	}
	int explore(int u) {
		for (int i=0;i<N;++i) V[i]=0;
		return dfs(u);
	}
	int bpm(){
		int ret=0;
		mL.resize(N, -1);
		mR.resize(M, -1);
		V.resize(N, 0);
		for (int i=0;i<N;++i) mL[i]=-1;
		for (int i=0;i<M;++i) mR[i]=-1;
		for (int i=0;i<N;++i) if (mL[i]<0) ret += explore(i);
		return ret;
	}
};

std::pair<int, int> toDiagonal(int N, int i, int j) {
//  First
//	(N-1, 0) -> 0
//	(N-2, 0), (N-1, 1) -> 1
//	...
//	(0, 0), (1, 1), .. (N-1, N-1) -> N-1
//	(0, 1), (1, 2), .. (N-2, N-1) -> N
//	...
//	(0, N-1) -> 2*N-2
	int first, second;
	if (i > j) first = N - 1 - (i - j);
	else first = N - 1 + (j - i);

//  Second
//  (0, 0) -> 0
//  (1, 0) (0, 1) -> 1
//  ...
//  (N-1, 0), ..., (0, N-1) -> N-1
//  (N-1, 1), ..., (1, N-1) -> N-2
//  ...
//  (N-1, N-1) -> 2*N-2
	second = i + j;
	return {first, second};
}

std::pair<int, int> fromDiagonal(int N, int first, int second) {
	for (int i = 0 ; i < N ; ++i) {
		for (int j = 0 ; j < N ; ++j) {
			auto x = toDiagonal(N, i, j);
			if (x.first == first && x.second == second)
				return {i, j};
		}
	}
	assert(false);
	return {-1, -1};
}

struct Solver {
	int N;
	int value;
	std::unordered_set<int> row, col, dia1, dia2;
	std::vector<std::string> mat;
	Solver(int N) : N(N), value(0), mat(N) {
		for (auto & s : mat) {
			s.resize(N);
			std::fill(s.begin(), s.end(), '.');
		}
	}
	bool set(int i, int j, char t) {
		switch(t) {
			case '+':
			{
				auto ret = toDiagonal(N, i, j);
				if (dia1.count(ret.first) != 0 || dia2.count(ret.second) != 0)
					return false;
				dia1.emplace(ret.first);
				dia2.emplace(ret.second);
				assign(i, j, t);
				return true;
			}
			case 'x':
			{
				if (row.count(i) != 0 || col.count(j) != 0)
					return false;
				row.emplace(i);
				col.emplace(j);
				assign(i, j, t);
				return true;
			}
			case 'o':
			{

				auto ret = toDiagonal(N, i, j); 
				if (dia1.count(ret.first) != 0 || dia2.count(ret.second) != 0)
					return false;
				if (row.count(i) != 0 || col.count(j) != 0)
					return false;
				dia1.emplace(ret.first);
				dia2.emplace(ret.second);
				row.emplace(i);
				col.emplace(j);
				assign(i, j, t);
				return true;
			}
		}
		assert(false);
	}

	void assign(int i, int j, char t) {
		if (t == '.') return;
		char & target = mat[i][j];
		if (target == '.') {
			target = t;
			if (t == 'o') value += 2;
			else value += 1;
			return;
		}
		if (target == 'x' && t == '+' || target == '+' && t == 'x') {
			target = 'o';
			value += 1;
			return;
		}
		assert(false);
	}

	std::vector<std::tuple<char, int, int>> solve() {
		std::vector<std::string> prev = mat;
		{
			BipartiteMatching bm;
			bm.N = N, bm.M = N;
			bm.E.resize(N);
			for (size_t i = 0 ; i < N ; ++i) {
				if (row.count(i) != 0) continue;
				for (size_t j = 0 ; j < N ; ++j) {
					if (col.count(j) != 0) continue;
					bm.E[i].push_back(j);
				}
			}
			bm.bpm();
			for (size_t i = 0 ; i < N ; ++i) {
				if (bm.mL[i] == -1) continue;
				set(i, bm.mL[i], 'x');
			}
		}

		{
			BipartiteMatching bm;
			bm.N = 2*N-1, bm.M = 2*N-1;
			bm.E.resize(2*N-1);
			for (size_t i = 0 ; i < N ; ++i) {
				for (size_t j = 0 ; j < N ; ++j) {
					auto dia = toDiagonal(N, i, j);
					if (dia1.count(dia.first)) continue;
					if (dia2.count(dia.second)) continue;
					bm.E[dia.first].push_back(dia.second);
				}
			}
			bm.bpm();
			for (size_t i = 0 ; i < 2*N-1; ++i) {
				if (bm.mL[i] == -1) continue;
				auto x = fromDiagonal(N, i, bm.mL[i]);
				set(x.first, x.second, '+');
			}
		}

		std::vector<std::tuple<char, int, int>> diff;
		for (size_t i = 0 ; i < N ; ++i) {
			for (size_t j = 0 ; j < N ; ++j) { 
				if (mat[i][j] == prev[i][j]) continue;
				diff.emplace_back(mat[i][j], i+1, j+1);
			}
		}
		return diff;
	}
};

int main(int argc, const char *argv[])
{
	int T;
	int N, M;
	
	std::cin >> T;
	for (int tcase = 1 ; tcase <= T ; ++tcase) {
		std::cout << "Case #" << tcase << ": ";
		std::cin >> N >> M;
		Solver solver(N);
		for (int m = 0 ; m < M ; ++m) {
			char c;
			int i, j;
			std::cin >> c >> i >> j;
			const bool ret = solver.set(i-1, j-1, c);
			assert(ret);
		}
		auto diff = solver.solve();
		std::cout << solver.value << " " << diff.size() << std::endl;
		for (const auto & d : diff) 
			std::cout << std::get<0>(d) << " " << std::get<1>(d) << " " << std::get<2>(d) << std::endl;
	}
	return 0;
}
