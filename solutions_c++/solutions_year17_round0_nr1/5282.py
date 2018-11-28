#include <iostream>
#include <deque>
#include <string>
#include <algorithm>

using namespace std;

bool goal(string &str);
bool contains(deque<string> &q, string &str);
int max_con(string &str);
int num_plus(string &str);

int main()
{
    int t, k;
    string line;
    string str;

    cin >> t;

    for (int icase = 1; icase <= t; ++icase)
    {

        deque<string> open, closed;
        bool f_Nfound = true;

        cin >> str >> k;

        cout << "Case #" << icase << ": ";

        if(goal(str))
        {
            cout << 0 << endl;
            continue;
        }

        open.push_back(str);

        for(int steps = 1; open.empty() == false && f_Nfound; steps++)
        {
            deque<string> children;

            while(open.empty() == false && f_Nfound)
            {
                string str_parent = open.front();
                open.pop_front();
                closed.push_back(str_parent);

                for(int i = 0; i < str_parent.length() - k + 1 && f_Nfound; i++)
                {
                    string str_child = str_parent;
                    for(int j = 0; j < k; j++)
                    {
                        if(str_child[i+j] == '+')
                            str_child.replace(i+j,1,1,'-');
                        else
                            str_child.replace(i+j,1,1,'+');
                    }
                    if(goal(str_child))
                    {
                        cout << steps;
                        f_Nfound = false;
                    }
                    if(contains(open,str_child)==false &&
                       contains(closed,str_child)==false &&
                       (max_con(str_parent) < max_con(str_child) || num_plus(str_parent) < num_plus(str_child)))
                        children.push_back(str_child);
                }
            }

            while(children.empty() == false && f_Nfound)
            {
                open.push_back(children.front());
                children.pop_front();
            }
        }
        if(f_Nfound)
            cout << "IMPOSSIBLE";
        cout << endl;
    }

    return 0;
}

bool goal(string &str)
{
    for(string::iterator it = str.begin(); it != str.end(); it++)
    {
        if(*it == '-')
            return false;
    }
    return true;
}

bool contains(deque<string> &q, string &str)
{
    for(deque<string>::iterator it = q.begin(); it != q.end(); it++)
    {
        string rev(str);
        reverse(rev.begin(),rev.end());
        if(str.compare(*it) == 0 || rev.compare(*it) == 0)
            return true;

    }
    return false;
}

int max_con(string &str)
{
    char prev = str[0];
    int max = 1;
    for(int i = 1; i < str.length(); i++)
    {
        char cur = str[i];
        if(prev == cur)
            max++;
        else
            max = 0;
        prev = cur;
    }
    return max;
}

int num_plus(string &str)
{
    int count = 0;
    for(int i = 1; i < str.length(); i++)
        if(str[i] == '+')
            count ++;
    return count;
}



