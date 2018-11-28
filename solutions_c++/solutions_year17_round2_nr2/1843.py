#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <string.h>
#include <math.h>
#include <utility>

using namespace std;

int main()
{
    int t, n, r, o, y, g, b, v, counter, cutpoint, i;
    char stables[1000];
    vector < pair <int, char> > colors;

    cin >> t;
    for (int x=1;x<=t;x++) {
        cin >> n;
        cin >> r >> o >> y >> g >> b >> v;
        cout << "Case #" << x << ": ";
        colors.clear();
        colors.push_back(make_pair(r, 'R'));
        colors.push_back(make_pair(y, 'Y'));
        colors.push_back(make_pair(b, 'B'));
        sort(colors.begin(),colors.end());
        if (colors[2].first>floor(n/2)) {
            cout << "IMPOSSIBLE" << endl;
            continue;
        }
        //for (i=0;i<3;i++) cout << colors[i].first << " " << colors[i].second << endl;
        counter=n;
        cutpoint=n-(2*colors[2].first-1);
        for (i=0;i<cutpoint;i+=2) {
            stables[i]=colors[1].second;
            colors[1].first--;
            counter--;
        }
        for (i=1;i<cutpoint;i+=2) {
            stables[i]=colors[0].second;
            colors[0].first--;
            counter--;
        }
        for (i=cutpoint;i<n;i+=2) {
            stables[i]=colors[2].second;
            colors[2].first--;
            counter--;
        }
        i=cutpoint+1;
        while (colors[0].first>0) {
            stables[i]=colors[0].second;
            colors[0].first--;
            counter--;
            i+=2;
        }
        while (colors[1].first>0) {
            stables[i]=colors[1].second;
            colors[1].first--;
            counter--;
            i+=2;
        }
        for (i=0;i<n;i++) {
            cout << stables[i];
        }
        cout << endl;
    }
    return 0;
}

// PROG_NAME < X-small-practice.in > output.txt
