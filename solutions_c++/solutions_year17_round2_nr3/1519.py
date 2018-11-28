#include <iostream>
#include <vector>
#include <iomanip>
template<class T>
void InitialiseVector(std::vector<T>& vec, int N)
{
	vec.clear();
	vec.reserve(N);
}

struct PonyExpress
{
	int N, Q;
	std::vector<int> E;
	std::vector<int> S;
	std::vector<std::pair<int, int>> queries;
	std::vector<std::vector<int>> D;
	std::vector<std::vector<double>> best;

	void Read()
	{
		std::cin >> N >> Q;
		InitialiseVector(E, N);
		InitialiseVector(S, N);
		for (auto i = 0; i < N; ++i)
		{
			int a,b;
			std::cin >> a >> b;
			E.push_back(a);
			S.push_back(b);
		}
		InitialiseVector(D, N);
		for (int i = 0; i < N; ++i)
		{
			std::vector<int> line;
			line.reserve(N);
			for (int j = 0; j < N; ++j)
			{
				int d;
				std::cin >> d;
				line.push_back(d);
			}
			D.push_back(line);
		}
		// Floyd-Warshall the distances
		for (int k = 0; k < N; ++k)
			for (int i = 0; i < N; ++i)
				for (int j = 0; j < N; ++j)
				{
					if (D[i][k] > 0 && D[k][j] > 0 && ( D[i][j] < 0 || D[i][j] > (D[i][k] + D[k][j])))
					{
						D[i][j] = D[i][k] + D[k][j];
					}
				}
		InitialiseVector(best, N);

		for (int i = 0; i < N; ++i)
		{
			std::vector<double> line_best;
		
			line_best.reserve(N);

			for (int j = 0; j < N; ++j)
			{
				if (D[i][j] > 0 && E[i] >= D[i][j])
				{
					line_best.push_back(double(D[i][j]) / double(S[i]));

				}
				else
				{
					line_best.push_back(-1.0);

				}
			}
			best.push_back(line_best);

		}
		InitialiseVector(queries, Q);
		for (int i = 0; i < Q; ++ i)
		{
			int u,v;
			std::cin >> u >> v;
			queries.emplace_back(u,v);
		}

	// Floyd-Warshall the best
		for (int k = 0; k < N; ++k)
			for (int i = 0; i < N; ++i)
				for (int j = 0; j < N; ++j)
				{
					const auto possibleNew = best[i][k] + best[k][j];
					if (best[i][k] > 0.0 && best[k][j] > 0.0 && (best[i][j] > possibleNew || best[i][j] < 0.0))
					{
						best[i][j] = possibleNew;
					}
				}
	}
	void Solve(int caseNum)
	{
		std::cout << "Case #" << caseNum << ": ";
		for (const auto uv : queries)
		{
			int u, v;
			std::tie(u,v) = uv;
			std::cout << best[u-1][v-1] << " ";
		}
		std::cout << "\n";
	}
};

int main()
{
	PonyExpress pe;
	int T;
	std::cin >> T;
	std::cout << std::fixed;
    std::cout << std::setprecision(7);
	for (int t = 1; t <= T; ++t)
	{
		pe.Read();
		pe.Solve(t);
	}
	return 0;
}