#include <iostream>
#include <vector>
#include <string>
#include <ostream>
#include <algorithm>
#include <iterator>
#include <array>
#include <set>
#include <cassert>
#include <iomanip>
#include <list>

using namespace std;

template <class T> 
std::ostream& operator<<(std::ostream& os, const vector<T>& X)
{
	for (const auto& x : X)
		os << x << " ";
	return os;
}

void AssignProbabilities(vector<double>& P, double U)
{
    sort(P.begin(), P.end());
    int n = P.size();
    P.push_back(1);
    for (int i = 0; i < n; ++i)
    {
        double diff = (P[i+1]-P[i]);
        double needed = diff*(i+1);
        double t = diff;
        if (needed > U)
            t = U/(i+1);
        for (int j = 0; j <= i; ++j)
        {
            P[j] += t;
        }
        U -= needed;
        if (U <= 0)
            break;
    }
    P.pop_back();
}

double CalculateWhenNeqK(const vector<double>& P)
{
    double t = 1;
    
    for (auto p : P)
        t *= p;
    
    return t;
}

int main() 
{
    cout << setprecision(10);
	long T;
	cin >> T;

	for (long t = 0; t < T; ++t)
	{
		cout << "Case #" << t+1 << ": ";
		int N, K;
        cin >> N >> K;
        double U;
        cin >> U;
        vector<double> P(N);
        for (auto& p : P)
        {
            cin >> p;
        }
//         cout << endl << " P= " << P << endl;
//         cout << "U = " << U << endl;
        AssignProbabilities(P,U);
//         cout << " after asignning, P= " << P << endl;
        cout << CalculateWhenNeqK(P) << endl;
//         cout << endl;
	}
	
	return 0;
}
