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
#include <numeric>
#include <utility>
#include <sstream>
#include <iomanip>
#include <cmath>
#include <cstdlib>
#include <ctime>
#define rep(i,n) for(int i=0;i<n;i++)

using namespace std;

int T;
int K;
string S;

int main()
{
		std::string dir = "../../qual/";
		fstream fin(dir + "A-large.in",ifstream::in);
    fstream fout(dir + "A-large.out",ofstream::out);
    fin >> T;
    for(int j=1;j<=T;j++)
    {
				fin >> S >> K;
				int ret = 0;
				for (int i = 0; i < S.size() - K + 1; ++i) {
					if (S[i] == '-') {
						ret++;
						for (int j = i; j < i + K; ++j) {
							if (S[j] == '-')
								S[j] = '+';
							else
								S[j] = '-';
						}
					}
				}
				bool fl = true;
				for (int i = S.size() - K; i < S.size(); ++i) {
					if (S[i] == '-')
						fl = false;
				}
				if (!fl) {
					fout << "Case #" << j << ": " << "IMPOSSIBLE" << "\n";
					cout << "Case #" << j << ": " << "IMPOSSIBLE" << "\n";
				}
				else {
					fout << "Case #" << j << ": " << ret << "\n";
					cout << "Case #" << j << ": " << ret << "\n";
				}
    }
    fin.close();
    fout.close();
    cout << "running time=" << clock()/(double)CLOCKS_PER_SEC;
    system("PAUSE");
    return 0;
}
