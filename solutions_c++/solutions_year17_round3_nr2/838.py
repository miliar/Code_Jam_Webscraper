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

struct Interval
{
    Interval(int a, int b, int o) : A(a), B(b), owner(o) {}
    int Length() const { return B - A; }
    int owner;
    int A;
    int B;
};

int Minimo(vector<Interval>& W, int o)
{
    int result = 0;
    
    bool abierto = false;
    int empiezo = 0;
    int termino = 0;
    for (int i = 0; i < W.size(); ++i)
    {
        Interval X = W[i];
        
        if (abierto)
        {
            if (o == X.owner)
            {
                termino = X.B;
            }
            else
            {
                result += termino-empiezo;
                abierto = false;
            }
        } else
        {
            if (o == X.owner)
            {
                empiezo = X.A;
                termino = X.B;
                abierto = true;
            }
        }
//         cout << "o = " << o << " and X.owner = " << X.owner << " and result so far = " << result << endl;

    }
    
    if (W.back().owner == o && W[0].owner == o && abierto)
    {
        result += 24*60 + W[0].A - empiezo;
    }
//     cout << "regresando result = " << result << endl;
    return result;
}

vector<int> IntervalosVacios(const vector<Interval>& W, int o)
{
    vector<int> result;
    for (int i = 0; i+1 < W.size(); ++i)
    {
        int j = i+1;
        Interval X = W[i];
        Interval Y = W[j];
        if (X.owner == o && Y.owner == o)
        {
            result.push_back(Y.A-X.B);
        }
    }
    
    Interval X = W.back();
    Interval Y = W.front();
    if (X.owner == o && Y.owner == o)
    {
        result.push_back(24*60+Y.A-X.B);
    }
    
    return result;
}

int Solve(vector<Interval>& W)
{
    sort(W.begin(), W.end(), [](const Interval& A, const Interval& B)
    {
        return A.A < B.A;
    });
    
    int numcambios = 0;
    
    for (int i = 0; i < W.size(); ++i)
    {
        int j = i+1;
        if (j == W.size())
            j = 0;
        Interval X = W[i];
        Interval Y = W[j];
        if (X.owner != Y.owner)
            numcambios += 1;
    }
    
//     cout << endl << "Numcambios de a fuerzas = " << numcambios << endl;
    
    int maxC = 24*60-Minimo(W,0);
    int maxJ = 24*60-Minimo(W,1);
    
//     cout << "Max que puede ser maxC = " << maxC << endl;
//     cout << "Max que puede ser maxJ = " << maxJ << endl;
    
    if (maxC > 720 && maxJ > 720)
        return numcambios;
    
    if (maxC < 720)
    {
        auto P = IntervalosVacios(W,0); //posiblemente 1
        sort(P.begin(), P.end(), [](int a, int b) { return b < a; }); // ordeno de mayor a menor longitud
        
        for (auto p : P)
        {
            maxC += p;
            numcambios += 2;
            if (maxC >= 720)
                return numcambios;
        }
        
    } else
    {
        auto P = IntervalosVacios(W,1); 
        sort(P.begin(), P.end(), [](int a, int b) { return b < a; });
        
        for (auto p : P)
        {
            maxJ += p;
            numcambios += 2;
            if (maxJ >= 720)
                return numcambios;
        }
    }
    
    assert(false);
    
    return numcambios;
}

int main() 
{
    cout << setprecision(20);
	long T;
	cin >> T;

	for (long t = 0; t < T; ++t)
	{
		cout << "Case #" << t+1 << ": ";
		int AC, AJ;
        cin >> AC >> AJ;
        vector<Interval> W;
        W.reserve(AC+AJ);
        
        for (int i = 0; i < AC; ++i)
        {
            int C,D;
            cin >> C >> D;
            W.push_back(Interval(C,D,0));
        }
        
        for (int i = 0; i < AJ; ++i)
        {
            int C,D;
            cin >> C >> D;
            W.push_back(Interval(C,D,1));
        }
        
        cout << Solve(W) << endl;
        
	}
	
	return 0;
}
