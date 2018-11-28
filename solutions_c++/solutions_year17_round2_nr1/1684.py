#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
    ifstream fin;
    fin.open("A-large.in", ios::in);
    ofstream fout;
    fout.open("A-large_output.txt", ios::out);
    int t;
    fin >> t;
    for (int o = 1; o <= t; ++o)
    {
        fout << "Case #" << o << ": ";
        int d, n, loc, speed;
        double time, crit = 0;
        fin >> d >> n;
        vector <pair <int, int> > horse;
        while (n--)
        {
            fin >> loc >> speed;
            horse.push_back(pair<int, int> (loc, speed));
        }
        sort(horse.rbegin(), horse.rend());
        for (int i = 0; i < horse.size(); ++i)
        {
            loc = horse[i].first;
            speed = horse[i].second;
            time = (double) (d - loc) / (double) speed;
            if (time > crit)
                crit = time;
            //cout << "crit = " << crit << endl;
        }
        fout.setf(ios::fixed);
        fout.precision(6);
        fout << (double) d / crit << endl;
    }
}
