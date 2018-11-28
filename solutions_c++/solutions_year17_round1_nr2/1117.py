#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
#include <cmath>
using namespace std ;
#define PB push_back
#define MP make_pair
typedef unsigned long long int llu;
typedef long long int ll;
typedef vector<int> VI;
typedef vector<VI> VVI;

// recursive search for alternating path: Hungarian method
bool FindMatch(int i, const VVI &w, VI &mr, VI &mc, VI &seen) {
  for (int j = 0; j < w[i].size(); j++) {
    if (w[i][j] && !seen[j]) {
      seen[j] = true;
      // if found unmatched column and found improvement path
      if (mc[j] < 0 || FindMatch(mc[j], w, mr, mc, seen)) {
        mr[i] = j;
        mc[j] = i;
        return true;
      }
    }
  }
  return false;
}

int BipartiteMatching(const VVI &w, VI &mr, VI &mc) {
  mr = VI(w.size(), -1);
  mc = VI(w[0].size(), -1);

  int ct = 0;
  for (int i = 0; i < w.size(); i++) { // try each row as a start
    VI seen(w[0].size());
    if (FindMatch(i, w, mr, mc, seen)) ct++;
  }
  return ct;
}

int main() {

    llu t;

    cin >> t;

    for (llu num = 1; num <= t; num++) {
        cout << "Case #"<<num<<": ";
        
        int n, p;
        int g[100], s[100][100], a[100][100], b[100][100];
        cin >> n >> p;

        if (n == 1) {
            int cnt = 0;
            cin >> g[0];
            for (int i = 0; i < p; i++) {
                cin >> s[i][0];
                
                //cout <<p <<" "<< g[0] << " " << s[i][0]<<endl; 
                bool yes = 0;
                if ((s[i][0]*10) %(11*g[0]) == 0)
                    yes = 1;
                if ((s[i][0]*10) %(9*g[0]) == 0)
                    yes = 1;

                int f1 = ceil(s[i][0]/(1.1*g[0]));
                f1 = max(f1, 1);
                int f2 = floor(s[i][0]/(0.9*g[0]));
                //cout << yes<< endl; 
                if (f1 <= f2) yes = 1;
                cnt += yes;
            }

            cout << cnt<<endl;
        } else {
            int cnt = 0;
            cin >> g[0] >> g[1];

            for (int j = 0; j < n; j++) {
            for (int i = 0; i < p; i++) {
                cin >>s[j][i];
                a[j][i] = ceil((s[j][i]*10)/(11.0*g[j]));
                b[j][i] = (s[j][i]*10)/(9*g[j]);
                a[j][i] = max(a[j][i], 1);

                //cout << "a " << a[j][i]<<endl;
 
                //cout << "b " << b[j][i]<<endl;

           }}

                VI x(p, 0), y(p, 0);
                VVI e(p, VI(p, 0));

               // cout << p << endl;
                //for (int l = 0; l < p; l++) 
                //    e[i] = VI(p, 0);
                //return 0;
                
                for (int l = 0; l < p; l++) {
                    for (int k = 0; k < p; k++) {
                    
                        if (max(a[0][l], a[1][k]) <= min(b[0][l], b[1][k]))
                            e[l][k]  = 1;
                        else
                            e[l][k] = 0;
                    }
                }

                for (int l = 0; l < p; l++) {
                    for (int k = 0; k < p; k++) {
                        //cout << e[l][k]<<" ";
             
                    }
                        ////cout << endl;
                }

            
                     
                            
            
                cout << BipartiteMatching(e, x, y) << endl;
            
                     
                            
            
        }
        
    }

}
