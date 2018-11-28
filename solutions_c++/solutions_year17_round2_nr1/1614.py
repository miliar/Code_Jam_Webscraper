#include <bits/stdc++.h>
using namespace std;


struct nodey{
    double dist;
    double speed;
};

int main() {
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int t;
    cin >> t;
    for(int pp=1;pp<=t;pp++){
        double d;
        int n;
        cin >> d >> n;
        nodey node[n];
        double tm=0.000000000;
        for(int i=0;i<n;i++){
            cin >> node[i].dist >> node[i].speed;
            double tt=(d-node[i].dist)/node[i].speed;
            tm=max(tm,tt);
        }
        double ans=d/tm;
        cout << "Case #" << pp << ": ";
        printf("%0.7lf\n",ans);
        
    }
    // your code goes here
    return 0;
}
