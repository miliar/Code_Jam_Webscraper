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

struct Cylinder
{
    double H,R;
};

constexpr double pi = 3.14159265358979323846;

double Solve(const vector<Cylinder>& A, long K)
{
    double mejorarea = 0;
    for (int i = 0; i < A.size(); ++i)
    {
        Cylinder base = A[i];
        double areabase = pi*base.R*base.R;
        double areaaltura = pi*base.H*base.R*2;
        vector<Cylinder> Bah;
        
        for (int j = 0; j < A.size(); ++j)
        {
            if (j == i)
                continue;
            Cylinder X = A[j];
            if (X.R <= base.R)
                Bah.push_back(X);
        }
        sort(Bah.begin(), Bah.end(), [](const Cylinder& X, const Cylinder& Y)
        {
            return X.R*X.H > Y.R*Y.H;
        });
        
        if (Bah.size() < K-1)
            continue;
        
        for (int j = 0; j+1 < K; ++j)
        {
            Cylinder X = Bah[j];
            areaaltura += 2*X.H*X.R*pi;
        }
        double area = areaaltura + areabase;
        if (area > mejorarea)
            mejorarea = area;
    }
    return mejorarea;
}

int main() 
{
    cout << setprecision(20);
	long T;
	cin >> T;

	for (long t = 0; t < T; ++t)
	{
		cout << "Case #" << t+1 << ": ";
		long N,K;
        cin >> N >> K;
        vector<Cylinder> A(N);
        for (int i = 0; i < N; ++i)
        {
            cin >> A[i].R >> A[i].H;
        }
        
        cout << Solve(A, K) << endl;
        
	}
	
	return 0;
}
