
#include <bits/stdc++.h>

using namespace std;


typedef long long int ll;
typedef long double ld;


# define PPI           3.14159265358979323846  /* pi */

int main(){
    cout.precision(25);

    int t;


    //cout << (3.14159265358979323846*200) << endl;

    cin >> t;




    for(int tt = 1;tt<=t;tt++){

        ll N,K;

        cin >> N >> K;

        vector< pair<ld,int> > v;

        ll arr[10000];

        ll maxr = 0;
        ll maxh = 0;
        ll maxi = 0;
        for(int i=0;i<N;i++){

            ll r,h;

            cin >> r >> h;

            if(r > maxr){
                maxr = r;
                maxi = i;
                maxh = h;
            }

            ld sq = 2*PPI*(double)r*(double)h;

            //cout << sq << " test " <<endl;

            arr[i] = r;

            v.push_back(make_pair(sq,i));





            //M_PI

        }

        sort(v.begin(),v.end(),[](auto &left, auto &right) {
            return left.first > right.first;
        });


        ld sump = 0;
        ld sumpa = 0;
        ll lmr = 0;
        int wasmax = 0;
        for(int i=0;i<K;i++){
            sump += v[i].first;
            if(arr[v[i].second] > lmr)
                lmr = arr[v[i].second];
            if(v[i].second == maxi)
                wasmax = 1;
        }
        sump += PPI*lmr*lmr;

        sumpa = sump;

        if(!wasmax){
            sumpa = 0;
            for(int i=0;i<K-1;i++){
                sumpa += v[i].first;
            }

            sumpa += 2*PPI*maxr*maxh;
            sumpa += PPI*maxr*maxr;
        }

        cout << "Case #"<<tt<<": "<<(max(sump,sumpa)) << endl;


    }

    return 0;

}
