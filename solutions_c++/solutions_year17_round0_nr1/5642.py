#include <iostream>
#include <queue>
#include <algorithm>
#include <string>
#include <map>

using namespace std;

string flip(string val, int index, int k)
{
    string res = val;
    for(int i = index; i < (index + k); i++)
    {
        if((int)res[i] == (int)'+')
            res[i] = '-';
        else
            res[i] = '+';
    }
    return res;
}
int search(string s, map<string,int> vals, int k, string targ)
{
    int size = s.size();
    queue< pair<string, int> > q;
    q.push(make_pair(s, 0));
    vals.insert(make_pair(s, 0));
    while(!q.empty())
    {
        pair<string , int> curr = q.front();
        q.pop();
        if((curr.first).compare(targ) == 0)
        {
           return curr.second; 
        }
        else
        {
          //  cout << " The current is " << curr.first << endl;
            for(int i = 0; i < (size - (k - 1)); i++)
            {
                string trial = flip(curr.first, i, k);
             //   cout << " The trial is " << trial << endl; 
                if(vals.find(trial) == vals.end())
                {
                    vals.insert(make_pair(trial, 0));
                    q.push(make_pair(trial, curr.second + 1));
                }
            }
        }
    }
    return -1;
}

int main()
{
    int t = 0;
    cin >> t;
    for(int i = 1; i < (t + 1); i++)
    {
        string s;
        int k;
        cin >> s >> k;
        map<string, int> vals;
        string targ = "";
        int size = s.size();
        for(int j = 0; j < size; j++)
        {
            targ += "+";
        }
        int res = search(s, vals, k, targ);
            
        cout << "Case #" << i << ": ";
        if(res >= 0)
            cout << res << endl;
         else
             cout << "IMPOSSIBLE" << endl;
    }
    return 0;
}
