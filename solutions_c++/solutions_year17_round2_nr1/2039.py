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
    int t, d, n, k, s;
    double currdest;
    vector <pair<double,double> > h;
    double veloc, currmaxveloc, maxveloc, maxtime, currtime;

    cin >> t;
    cout.precision(17);
    for (int x=1;x<=t;x++) {
        h.clear();
        cin >> d >> n;
        for (int i=0;i<n;i++) {
            cin >> k >> s;
            h.push_back(make_pair(k,s));
            sort(h.begin(),h.end());
        }
        sort(h.begin(),h.end()); //sort by ki;

        maxveloc=-1;
        for (int i=n-1; i>=0; i--) {
            maxtime=0;
            if (i==n-1) currdest=d;
            else currdest=h[i+1].first;
            //cout << "flag" <<i << endl;
            for (int j=0; j<=i; j++) {
                currtime=double(currdest-h[j].first)/double(h[j].second);
                //cout << h[j].first << " " << h[j].second << " " << currtime << endl;
                if (currtime>maxtime) maxtime=currtime;
            }
            //cout << "maxtime=" << maxtime << endl;
            currmaxveloc=double(currdest)/maxtime;
            //cout << "currmaxveloc=" << currmaxveloc << endl;
            if (i==n-1) maxveloc=currmaxveloc;
            else if (currmaxveloc<maxveloc) maxveloc=currmaxveloc;
        }
        cout << "Case #" << x << ": " << maxveloc << endl;
    }
    return 0;
}

// PROG_NAME < X-small-practice.in > output.txt

/*--
Assume Annie will catch
--*/
