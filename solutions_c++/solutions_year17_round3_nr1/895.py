#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <utility> //pair
#include <map>
#include <cstring>
#include <cmath>

using namespace std;

int main()
{
    cout.precision(40);
    int t, n, k;
    long long int r, h, rmax, currmax, currval;
    vector < pair< long long int, long long int> > p; //p(2rh, r^2)
    vector <long long int> q;
    cin >> t;
    //cout << M_PI << endl;

    for (int x=1;x<=t;x++) {
        cin >> n>>k;
        p.clear();
        for (int i=0;i<n;i++) {
            cin >> r >> h;
            p.push_back(make_pair(r*r, 2*r*h));
        }
        sort(p.begin(),p.end());
        currmax=0;

        for (int i=n-1;i>=k-1;i--) {
            currval=p[i].first+p[i].second;
            q.clear();
            for (int j=0;j<i;j++) q.push_back(p[j].second);
            sort (q.begin(),q.end());

            for (int j=i-1;j>=i-k+1;j--) currval+=q[j];
            if (currval>currmax) currmax=currval;
        }
        cout << "Case #" << x << ": " << (double)currmax * M_PI << endl;
    }
    return 0;
}

// PROG_NAME < X-small-practice.in > output.txt
