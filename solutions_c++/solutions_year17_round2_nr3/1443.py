#include <bits/stdc++.h>

using namespace std;
 
struct pt{
    int e, s;
    double t;
};

int main(){
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int T;
    cin >> T;
    cout.precision(22);
    for (int oo = 1; oo <= T; oo++){
        cout << "Case #" << oo << ": ";
        int n, q;
        cin >> n >> q;
        vector <double> e(n), s(n);
        vector <pt >  horses[n];
        for (int i=0; i<n; i++){
            horses[i].clear();
            cin >> e[i] >> s[i];
            pt tmp;
            tmp.e = e[i];
            tmp.s = s[i];
            tmp.t = 0;
            horses[i].push_back(tmp);
        }
        double a[101][101];
        for (int i = 0; i < n; i++)
            for (int j = 0; j < n; j++)
                cin >> a[i][j];

        double time[n];
        for (int i=0;i<n;i++)
            time[i] = 1000000000000000;

        time[0] = 0;

        for (int p = 0; p < 1; p++){
            int u, v;
            cin >> u >> v;
            for (int i = 0; i < n-1; i++)
                for (int j = 0; j < horses[i].size(); j++){
                    if (horses[i][j].t == 0)
                        horses[i][j].t += time[i];
                    double d = 0;
                    for (int k = i+1; k < n; k++){
                        d += a[k-1][k];
                        if (d <= horses[i][j].e){
                            pt tmp;
                            tmp.e = horses[i][j].e - d;
                            tmp.s = horses[i][j].s;
                            tmp.t = horses[i][j].t + d/horses[i][j].s;
                            horses[k].push_back(tmp);
                            time[k] = min(time[k], tmp.t);
                        }
                    }
                }
            cout << time[n-1] << endl;
        }

    }   
    return 0;
}
