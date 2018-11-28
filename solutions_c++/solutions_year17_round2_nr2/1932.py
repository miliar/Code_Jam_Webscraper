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
const string X = "ROYGBV";

template <class T> 
std::ostream& operator<<(std::ostream& os, const vector<T>& X)
{
	for (const auto& x : X)
		os << x << " ";
	return os;
}

struct Path
{
    Path(int r, int o, int y, int  g, int b, int v) :
    R(r), O(o), Y(y), G(g), B(b), V(v) {}
    
    bool is_valid() const
    {
        for (auto x : X)
        {
            if (num(x) < 0)
                return false;
        }
        return true;
    }
    
    bool finished() const
    {
        for (char x : X)
            if (num(x) > 0)
                return false;
        
        return valid_edge(m_stalls.back(), m_stalls.front());
    }
    
    void add(char t)
    {
        if (t == 'R')
        {
            m_stalls.push_back('R');
            --R;
            return;
        }
        
        if (t == 'Y')
        {
            m_stalls.push_back('Y');
            --Y;
            return;
        }
        
        if (t == 'B')
        {
            m_stalls.push_back('B');
            --B;
            return;
        }
        
        if (t == 'O')
        {
            m_stalls.push_back('O');
            --O;
            if (!finished())
            {
                m_stalls.push_back('B');
                --B;
            }
            return;
        }
        
        if (t == 'G')
        {
            m_stalls.push_back('G');
            --G;
            if (!finished())
            {
                m_stalls.push_back('R');
                --R;
            }
            return;
        }
        
        if (t == 'V')
        {
            m_stalls.push_back('V');
            --V;
            if (!finished())
            {
                m_stalls.push_back('Y');
                --Y;
            }
            return;
        }
    }
    
    bool valid_edge(char u, char v) const
    {
        if (u == v)
            return false;
        
        if (u == 'R')
            return v == 'B' || v == 'G' || v == 'Y';
        
        if (u == 'B')
            return (v == 'R' || v == 'O' || v == 'Y');
        
        if (u == 'Y')
            return (v == 'R' || v == 'V' || v == 'B');
        
        
        if (u == 'G')
            return (v == 'R');
        if (u == 'O')
            return (v == 'B');
        if (u == 'V')
            return v == 'Y';
        assert(false);
        return false;
    }
    
    int num(char t) const
    {
        if (t == 'R')
        {
            return R;
        }
        
        if (t == 'Y')
        {
            return Y;
        }
        
        if (t == 'B')
        {
            return B;
        }
        
        if (t == 'O')
        {
            return O;
        }
        
        if (t == 'G')
        {
            
            return G;
        }
        
        if (t == 'V')
        {
            return V;
        }
        assert(false);
        return 0;
    }
    
    bool can_add(char u) const
    {
        if (m_stalls.empty())
            return num(u) > 0;
        
        char t = m_stalls.back();
        
        if (!valid_edge(u,t))
            return false;
        if (num(u) == 0)
            return false;
        
        
        if (t == 'O')
        {
            return B > 0;
        }
        
        if (t == 'G')
        {
            return R > 0;
        }
        
        if (t == 'V')
        {
            return Y > 0;
        }
        
        return true;
    }
    
    
    
    vector<Path> Neighbors() const;
    
    int R;
    int O;
    int Y;
    int G;
    int B;
    int V;
    string m_stalls;
};

vector<Path> Path::Neighbors() const
{
    vector<Path> hola;
    const string X = "ROYGBV";

    if (m_stalls.empty())
    {
        Path P = *this;
        for (auto x : X)
        {
            if (num(x) > 0)
            {
                Path P = *this;
                P.add(x);
                hola.push_back(P);
                return hola;
            }
        }
        
    }
    
    for (auto x : X)
    {
        if (can_add(x))
        {
            Path B = *this;
            B.add(x);
            hola.emplace_back(std::move(B));
        }
    }
    
    return hola;
    
}

void Solve(int N,int R,int O,int Y,int G,int B,int V)
{
    vector<Path> frontier;
    frontier.emplace_back(R,O,Y,G,B,V);
    while (!frontier.empty())
    {
//         cout << "frontier.size() == " << frontier.size() << endl;
        auto P = frontier.back();
//         cout << "P = " << P.m_stalls << endl;
        frontier.pop_back();
        if (P.finished())
        {
            cout << P.m_stalls << endl;
            return;
        }
        
        if (!P.is_valid())
            continue;
        
        for (auto& x : P.Neighbors())
        {
            frontier.push_back(x);
        }
        
    }
    cout << "IMPOSSIBLE" << endl;
    return;
}

void SolveSmall(int R, int Y, int B)
{
    string U;
    if (R > Y)
    {
        while (R > 0 && Y > 0)
        {
            U.push_back('R');
            U.push_back('Y');
            --R;
            --Y;
        }
    } else
    {
        while (R > 0 && Y > 0)
        {
            U.push_back('Y');
            U.push_back('R');
            --R;
            --Y;
        }
    }
    
    
    
    while (Y > 0)
    {
        U.push_back('Y');
        --Y;
    }
    
    while (R > 0)
    {
        U.push_back('R');
        --R;
    }
    
    if (B > U.size())
    {
        cout << "IMPOSSIBLE" << endl;
        return;
    }
    
    string V;
    while (B > 0)
    {
        V.push_back('B');
        V.push_back(U.back());
        U.pop_back();
        --B;
    }
    
    while (!U.empty())
    {
        V.push_back(U.back());
        U.pop_back();
    }
    for (int i = 0; i < V.size(); ++i)
    {
        int j = i+1;
        if (j == V.size())
            j = 0;
        if (V[i] == V[j])
        {
            cout << "IMPOSSIBLE" << endl;
            return;
        }
    }
    cout << V << endl;
}

int main() 
{
	long T;
	cin >> T;
    cout << setprecision(10);

	for (long t = 0; t < T; ++t)
	{
		cout << "Case #" << t+1 << ": ";
		long N,R,O,Y,G,B,V;
        cin >> N >> R >> O >> Y >> G >> B >> V;
        SolveSmall(R,Y,B);
//         Solve(N,R,O,Y,G,B,V);
        
	}
	
	return 0;
}
