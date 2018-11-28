#include <cstdint>
#include <cstdlib>
#include <iostream>
#include <queue>
#include <vector>
#include <functional>
#include <utility>
#include <sstream>
#include <algorithm>
#include <set>

using namespace std;

void setRect(char n, int x, int y, vector<char>& v, int r, int c)
{
    int minX = x;
    int minY = y;
    int maxY = y;
    int maxX = x;
    
    for(int i = x+1; i < c; i++)
    {
        if(v[y * c + i] == '?')
            maxX = i;
        else
            break;
    }

    for(int i = x-1; i >= 0; i--)
    {
        if(v[y * c + i] == '?')
            minX = i;
        else
            break;
    }

    for(int i = y+1; i < r; i++)
    {
        bool free = true;;
        for(int j = minX; j <= maxX; j++)
        {
            if(v[i * c + j] != '?')
            {
                free = false;
                break;
            }
        }
        if(free)
            maxY = i;
        else
            break;
    }

    for(int i = y-1; i >= 0; i--)
    {
        bool free = true;;
        for(int j = minX; j <= maxX; j++)
        {
            if(v[i * c + j] != '?')
            {
                free = false;
                break;
            }
        }
        if(free)
            minY = i;
        else
            break;
    }

    for(int i = minY; i <= maxY; i++)
    {
        for(int j = minX; j <= maxX; j++)
        {
            v[i * c + j] = n;
        }
    }
}

string alphabetCake(vector<char> v, int r, int c)
{
    set<char> s;

    for(int i = 0; i < r; i++)
    {
        for(int j = 0; j < c; j++)
        {
            if(v[i * c + j] != '?' &&  s.find(v[i * c + j]) == s.end())
            {
                setRect(v[i * c + j], j, i, v, r, c);
                s.insert(v[i * c + j]);
            }
        }
    }

    stringstream ss;
    for(int i = 0; i < r; i++)
    {
        for(int j = 0; j < c; j++)
        {
            ss << v[i * c + j];
        }
        if(i != r-1)
            ss << endl;
    }

    return ss.str();
}

int main()
{
    int t; cin >> t;

    for(int i = 0; i < t; i++)
    {
        int r, c; cin >> r >> c;

        vector<char> v; v.resize(r*c);
        for(int j = 0; j < v.size(); j++)
        {
            cin >> v[j];
        }

        cout << "Case #" << (i + 1) << ": " << endl <<  alphabetCake(v, r, c) << endl;
    }
}
