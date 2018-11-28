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
    int t, n, k, j;
    double u, currp, deficit, finalp, ans;
    vector <double> p;
    cin >> t;

    for (int x=1;x<=t;x++) {
        cin >> n >> k;
        cin >> u;
        p.clear();
        for (int i=0;i<n;i++) { cin >> currp; p.push_back(currp); }
        sort(p.begin(),p.end());

        deficit=0;
        for (int i=0;i<n-1;i++) deficit+=(p[n-1]-p[i]);
        if (u>=deficit) {
            finalp=p[n-1]+(u-deficit)/(double)n;
            ans=1;
            for (int i=0;i<n;i++) ans*=finalp;
        } else {
            currp=0;
            for (j=0;j<n;j++) {
                currp+=((p[j+1]-p[j])*(j+1));
                if (currp>=u) break;
            }
            finalp=p[j+1]-(currp-u)/(double)(j+1);
            ans=1;
            for (int i=0;i<=j;i++) ans*=finalp;
            for (int i=j+1;i<n;i++) ans*=p[i];
        }
        cout.precision(40);
        cout << "Case #" << x << ": " << ans << endl;
    }
    return 0;
}

// PROG_NAME < X-small-practice.in > output.txt
