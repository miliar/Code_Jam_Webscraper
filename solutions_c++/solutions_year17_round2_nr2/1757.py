#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <fstream>
#include <cmath>
#include <queue>
#include <map>
#include <set>
#include <sstream>
#include <iomanip>


#define FOR(i, a, b) for(int i = a; i < b; i++)
#define FORD(i, a, b) for(int i = a; i > b; i--)



using namespace std;

int T, N, R, O, Y, G, B, V;

bool colsorter(pair<int, char> i, pair<int, char> j) {
    return (i.first > j.first);
}

vector<pair<int, char> > nbs;

int main()
{
    ifstream fin;
    fin.open("B-small-attempt2.in");
    ofstream fout;
    fout.open("B-small-attempt2-out.txt");

    fin >> T;

    FOR (i, 0, T) {
        fin >> N >> R >> O >> Y >> G >> B >> V;
        string arrangement = "";
        if ((R + Y < B) || (R + B < Y) || (B + Y < R)) {
            fout << "Case #" << i + 1 << ": IMPOSSIBLE" << endl;
        }
        else {
            pair<int, char> redp; redp.first = R; redp.second = 'R';
            pair<int, char> bluep; bluep.first = B; bluep.second = 'B';
            pair<int, char> yellowp; yellowp.first = Y; yellowp.second = 'Y';
            nbs.push_back(redp); nbs.push_back(yellowp); nbs.push_back(bluep);
            sort(nbs.begin(), nbs.end(), colsorter);

            while ((nbs[0].first > 0)) {
                if (nbs[0].second != arrangement[arrangement.size() - 1]) {
                    arrangement = arrangement + nbs[0].second;
                    nbs[0].first--;
                }
                else {
                    arrangement = arrangement + nbs[1].second;
                    nbs[1].first--;
                }
                sort(nbs.begin(), nbs.end(), colsorter);
            }
            if (arrangement[arrangement.size() - 1] == arrangement[0]) {
                char temp = arrangement[arrangement.size() - 1];
                arrangement[arrangement.size() - 1] = arrangement[arrangement.size() - 2];
                arrangement[arrangement.size() - 2] = temp;
            }
             fout << "Case #" << i + 1 << ": " << arrangement << endl;
        }
    }

    return 0;
}
