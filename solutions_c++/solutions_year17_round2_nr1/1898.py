#include <bits/stdc++.h>

using namespace std;


int main(){
    freopen("output.out","w",stdout);
    freopen("input.in","r",stdin);
    int t;
    cin >> t;
    for(int i=0;i<t;i++)
    {
        double d;
        int n;
        cin >> d >> n;
        vector<double> tt(n);
        for(int j=0;j<n;j++)
        {
            int s,k;
            cin >> k >> s;
            tt[j]= (d-double(k))/double(s);
        }
        sort(tt.rbegin(),tt.rend());

        cout << "Case #"<< i+1<<": " << fixed<<setprecision(6)<< d/tt[0] << endl;
    }
    return 0;
}
