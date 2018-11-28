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
unsigned long long N;

vector<int> digits;

void ConstructDigits(unsigned long long NN) {
	vector<int> ret(0);
	while (NN > 0) {
		ret.push_back(NN % 10);
		NN /= 10;
	}
	reverse(ret.begin(), ret.end());
	digits = ret;
}

bool solve(int ind) {
	if (ind == digits.size())
		return true;

	if (ind > 0 && digits[ind] < digits[ind - 1])
		return false;

	bool fl = solve(ind + 1);
	if (fl) 
		return true;

	if (ind > 0 && digits[ind] - 1 < digits[ind - 1])
		return false;
	else {
		digits[ind] -= 1;
		for (int i = ind + 1; i < digits.size(); ++i)
			digits[i] = 9;
		return true;
	}
	return true;
}

unsigned long long NumberFromDigits() {
	unsigned long long ret = 0;
	for (int i = 0; i < digits.size(); ++i) {
		ret = 10 * ret + digits[i];
	}
	return ret;
}

int main()
{
		std::string dir = "../../qual/";
		fstream fin(dir + "B-large.in",ifstream::in);
    fstream fout(dir + "B-large.out",ofstream::out);
    fin >> T;
    for(int j=1;j<=T;j++)
    {
			fin >> N;

			ConstructDigits(N);

			solve(0);

			fout << "Case #" << j << ": " << NumberFromDigits() << "\n";
			cout << "Case #" << j << ": " << NumberFromDigits() << "\n";
    }
    fin.close();
    fout.close();
    cout << "running time=" << clock()/(double)CLOCKS_PER_SEC;
    system("PAUSE");
    return 0;
}
