#include <cstdio>
#include <iostream>
#include <fstream>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <queue>
#include <numeric>
#include <utility>
#include <sstream>
#include <iomanip>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <string>
#define rep(i,n) for(int i=0;i<n;i++)

using namespace std;

int T;
int N;
int C, M;
vector<int> P, B;

vector< vector<int> > poss;

int main()
{
	std::string dir = "../../2/";
	fstream fin(dir + "B-small-attempt1.in", ifstream::in);
	fstream fout(dir + "B-small-attempt1.out", ofstream::out);

	fin >> T;
	for (int t = 1; t <= T; t++)
	{
		int y = 0, z = 0;
		
		fin >> N >> C >> M;
		P.resize(M);
		B.resize(M);
		rep(i, M)
			fin >> P[i] >> B[i];

		poss.resize(C);
		rep(i, poss.size())
			poss[i] = vector<int>(N, 0);

		rep(i, M)
			poss[B[i] - 1][P[i] - 1]++;

		if (C == 2) {
			int O0 = 0, O1 = 0;
			O0 = poss[0][0];
			O1 = poss[1][0];

			int N0 = 0, N1 = 0;
			rep(i, poss[0].size())
				N0 += poss[0][i];
			rep(i, poss[1].size())
				N1 += poss[1][i];

			y = max(N0, N1);
			z = 0;

			if (O0 + O1 > y) {
				y = O0 + O1;
				z = 0;
			}
			else {
				int cpos = 0;

				{
					int tind2 = 1;
					while (poss[0][0] > 0) {
						cpos++;
						while (tind2 < poss[1].size() && (poss[1][tind2] == 0 || poss[0][tind2] == 0))
							tind2++;

						if (tind2 == poss[1].size()) {
							tind2 = 1;
							while (tind2 < poss[1].size() && poss[1][tind2] == 0)
								tind2++;
						}

						poss[0][0]--;
						if (tind2 < poss[1].size())
							poss[1][tind2]--;
					}
				}

				{
					int tind1 = 1;
					while (poss[1][0] > 0) {
						cpos++;
						while (tind1 < poss[0].size() && (poss[0][tind1] == 0 || poss[1][tind1] == 0))
							tind1++;

						if (tind1 == poss[0].size()) {
							tind1 = 1;
							while (tind1 < poss[0].size() && poss[0][tind1] == 0)
								tind1++;
						}

						poss[1][0]--;
						if (tind1 < poss[0].size())
							poss[0][tind1]--;
					}
				}

				for (int tpos = 1; tpos < N; ++tpos) {
					{
						int tind2 = tpos + 1;
						bool fl = true;
						while (poss[0][tpos] > 0 && fl) {
							
							while (tind2 < poss[1].size() && (poss[1][tind2] == 0 || poss[0][tind2] == 0))
								tind2++;

							if (tind2 == poss[1].size()) {
								tind2 = tpos + 1;
								while (tind2 < poss[1].size() && poss[1][tind2] == 0)
									tind2++;
							}

							if (tind2 == poss[1].size()) {
								fl = false;
								break;
							}
							cpos++;
							poss[0][tpos]--;
							poss[1][tind2]--;
						}
					}

					{
						int tind1 = tpos + 1;
						bool fl = true;
						while (poss[1][tpos] > 0 && fl) {
							
							while (tind1 < poss[0].size() && (poss[0][tind1] == 0 || poss[1][tind1] == 0))
								tind1++;

							if (tind1 == poss[0].size()) {
								tind1 = tpos + 1;
								while (tind1 < poss[0].size() && poss[0][tind1] == 0)
									tind1++;
							}

							if (tind1 == poss[0].size()) {
								fl = false;
								break;
							}
							cpos++;
							poss[1][tpos]--;
							poss[0][tind1]--;
						}
					}

					cpos += max(poss[0][tpos], poss[1][tpos]);
					z    += min(poss[0][tpos], poss[1][tpos]);

					if ((poss[0][tpos] == 0 || poss[1][tpos] == 0) && (poss[0][tpos] + poss[1][tpos]) != 0)
						cout << "AAAA\n";

					poss[0][tpos] = poss[1][tpos] = 0;

					if (poss[0][tpos] != 0 && poss[1][tpos] != 0)
						break;
				}

				/*while (cpos < y) {

				}*/
				cout << cpos << " " << y << "\n";
			}


		}
		else
			cout << "Solution C>2 not ready yet!\n";


		fout << "Case #" << t << ": " << y << " " << z << "\n";
		cout << "Case #" << t << ": " << y << " " << z << "\n";
	}
	fin.close();
	fout.close();
	cout << "running time=" << clock() / (double)CLOCKS_PER_SEC;
	system("PAUSE");
	return 0;
}
