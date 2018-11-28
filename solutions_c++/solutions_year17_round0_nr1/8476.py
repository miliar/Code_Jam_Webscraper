#include <iostream>
#include <list>
#include <map>
#include <sstream>
#include <string>
#include <vector>

using namespace std;

string flip (string s, int k, int pos)
{
    for (int i = pos; i < pos + k; ++i)
    {
        s[i] = (s[i] == '+') ? '-' : '+';
    }
    return s;
}

int main()
{
    string input = "5 ---+-++- 3 +++++ 4 -+-+- 4 -- 2 +- 2";
    stringstream ss(input);
    int t;
    ss >> t;
    for (int i = 1; i <= t; ++i)
    {
        string s;
        ss >> s;
        string goal(s.size(),'+');
        int k; 
        ss >> k;
        map<string, int> dists; // also our "haveseen" map 
        list<string> todo;
        todo.push_back(s);
        dists[s] = 0;
        bool goalAchieved = false;
        std::cout << "Case #" << i << ": ";
        while (!todo.empty() && !goalAchieved)
        {
            string actNode = todo.front();
            if (actNode == goal)
            {
                std::cout << dists[goal] << endl;
                goalAchieved = true;
            }
            else
            {
                for (int j = 0; j <= s.size() - k; ++j)
                {
                    string candidate = flip(actNode,k,j);
                    if (dists.find(candidate) == dists.end())
                    {
                        dists[candidate] = dists[actNode] + 1;
                        todo.push_back(candidate);       
                    }
                }
                if (!todo.empty())
                    todo.pop_front();
            }
        }
        if (!goalAchieved)
            std::cout << "IMPOSSIBLE" << endl;
    }
}