
#include <bits/stdc++.h>

using namespace std;


typedef long long int ll;
typedef long double ld;


# define PPI           3.14159265358979323846  /* pi */

int main(){
    cout.precision(8);

    int t;


    //cout << (3.14159265358979323846*200) << endl;

    cin >> t;




    for(int tt = 1;tt<=t;tt++){

        ll N,K;
        ld U;

        cin >> N >> K;
        cin >> U;

        vector <ld> v;

        for(int i=0;i<N;i++){
            ld p;
            cin >> p;

            v.push_back(p);
        }

        sort(v.begin(),v.end());

        for(int i=0;i<v.size()-1;i++){

            ld need = (v[i+1]-v[i])*((ld)(i+1));
            if(U >= need){
                U-=need;
                for(int j=0;j<=i;j++){
                    v[j] = v[i+1];
                }
            }
            else{
                ld plusi = U/(i+1);
                for(int j=0;j<=i;j++){
                    v[j] += plusi;
                }
                U=0;
                break;
            }

        }

        if(U > 0){
            ld plusi = U/N;
            for(int j=0;j<N;j++){
                v[j] += plusi;
            }
        }

        ld perf = 1;
        for(int i=0;i<N;i++){
            perf *= v[i];

        }

        if(perf > 1)
            perf = 1;

        cout << fixed << "Case #" << tt << ": " << perf << endl;

    }

    return 0;

}
