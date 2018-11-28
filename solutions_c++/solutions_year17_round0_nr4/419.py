#include <iostream>
#include <vector>
#include <ostream>
#include <algorithm>
#include <iterator>
#include <array>
#include <cmath>
#include <list>
#include <cassert>

using namespace std;

template <class T> 
std::ostream& operator<<(std::ostream& os, const vector<T>& rhs)
{
	for (const auto& x : rhs)
		os << x << ' ';
	return os;
}

template <class T> 
std::ostream& operator<<(std::ostream& os, const vector<vector<T>>& rhs)
{
	for (const auto& x : rhs)
		os << x << endl;
	return os;
}

struct Pieza
{
	Pieza(char tt, int xx, int yy) : t(tt), x(xx), y(yy) {}
	char t;
	int x;
	int y;
};

std::ostream& operator<<(std::ostream& os, const Pieza& A)
{
	
	os << A.t << ' ' << A.x+1 << ' ' << A.y+1;
	return os;
}

struct Point
{
	Point(int xx, int yy) : x(xx), y(yy) {}
	int x;
	int y;
};

using Row = vector<int>;
using Matrix = vector<Row>;

void SolvePluses(Matrix& A)
{
	int n = A.size();
	for (int y = 0; y < n; ++y)
	{
		if (A[0][y] == 0)
		{
			A[0][y] = 1;
		}
	}
// 	cout << "finished with first row" << endl;
	for (int y = 1; y+1 < n; ++y)
	{	
		if (A[n-1][y] == 0)
		{
			A[n-1][y] = 1;
		}
	}
// 		cout << "finished with last row" << endl;

}

int numones(const Matrix& B)
{
	int result = 0;
	int n = B.size();
	for (int x = 0; x < n; ++x)
	{
		for (int y = 0; y < n; ++y)
		{
			result += B[x][y];
		}
	}
	return result;
}

void SolveTimes(Matrix& B)
{
	int n = B.size();
	vector<bool> occupiedcols(n,0);
	vector<bool> occupiedrows(n,0);
// 	cout << "sf1" << endl;

	for (int x = 0; x < n; ++x)
	{
		for (int y = 0; y < n; ++y)
		{
			if (B[x][y] == 1)
			{
				occupiedrows[x] = 1;
				occupiedcols[y] = 1;
			}
		}
	}
// 	cout << "sf2" << endl;
	int x = 0;
	int y = 0;
// 	cout << endl << "For n = " << n << endl;
// 	cout << "occupied rows: " << occupiedrows << endl;
// 	cout << "occupied cols: " << occupiedcols << endl;
	
	while (true)
	{
		while (x < n && occupiedrows[x])
			++x;
		while (y < n && occupiedcols[y])
			++y;
		if (x == n || y == n)
			break;
		occupiedrows[x] = 1;
		occupiedcols[y] = 1;
		B[x][y] = 1;
	}
	
// 	assert(numones(B) == n);
// 	cout << "sf3" << endl;

}

vector<Pieza> combine(Matrix& CP, Matrix& CT, Matrix& P, Matrix& T)
{
	int n = CP.size();
	vector<Pieza> result;
	for (int x = 0; x < n; ++x)
	{
		for (int y = 0; y < n; ++y)
		{
			int a = 0;
			if (P[x][y] != CP[x][y])
			{
				a += 1;
			}
			
			if (T[x][y] != CT[x][y])
			{
				a += 2;
			}
			
			if (a == 3 || (a != 0 && T[x][y] == P[x][y]) )
				result.emplace_back('o',x,y);
			else if (a == 1)
				result.emplace_back('+',x,y);
			else if (a == 2)
				result.emplace_back('x',x,y);
			
		}
	}
	return result;
}

int main() 
{
	int T;
	cin >> T;
	for (int i = 0; i < T; ++i)
	{
		cout << "Case #" << i+1 << ": ";
		int n,m;
		cin >> n >> m;
		Matrix Pluses(n,Row(n,0));
		Matrix Times(n,Row(n,0));
		for (int i = 0; i < m; ++i)
		{
// 			cout << "starting = " << i << endl;
			char t;
			cin >> t;
			
			int x,y;
			cin >> x >> y;
			--x;
			--y;
			
			if (t == '+' || t == 'o')
				Pluses[x][y] = 1;
			if (t == 'x' || t == 'o')
				Times[x][y] = 1;
// 			cout << "ending = " << i << endl;
		}
		

		auto copyP = Pluses;
		auto copyT = Times;
		
		SolvePluses(Pluses);
		SolveTimes(Times);
	
		auto Piezas = combine(copyP, copyT, Pluses, Times);
		
		
		
		int points = 3*n-2;
		if (n == 1)
			points = 2;
		
		cout << points << ' ' << Piezas.size() << endl;
		for (const auto& p : Piezas)
			cout << p << endl;
		
	}
	return 0;
}
