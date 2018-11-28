
#include <bits/stdc++.h>

using namespace std;


typedef long long int ll;




ll karr[2];

int main(){

    int t;
    cin >> t;
    for(int tt = 1;tt<=t;tt++){

        ll n,k;

        cin >> n >> k;


        int c = 0;
        ll cn = 0;
        ll ca = 1;

        while(cn < k){
            c++;
            cn+=ca;
            ca*=2;
        }



        karr[0] = 0;
        karr[1] = 0;

        ll cc = c-1;
        ll ck = 0;


        //cout << cc << endl;

        map <ll,ll> m, mn;
        m[n] = 1;

        cn = 0;
        ca = 1;

        ll nn = n;

        while(cc){

            nn = (nn-1)/2;

            mn.clear();
            for(auto i : m){

                if(mn.count( (i.first-1)/2 ))
                    mn[(i.first-1)/2] += i.second;
                else
                    mn[(i.first-1)/2] = i.second;

                if( mn.count( ceil( (i.first-1) / ((double)2) ) ) )
                    mn[ceil( (i.first-1) / ((double)2) )] += i.second;
                else
                    mn[ceil( (i.first-1) / ((double)2) )] = i.second;


            }
            m = mn;
            cn += ca;
            ca *= 2;
            cc--;
        }

        //nn = (nn-1)/2;


        ll te = 0;
        for(auto i : m){
            //cout << i.first << " " << i.second << "WTF" << endl;
            if(i.first == nn+1)
                te = i.second;
        }
        /*if(m.count(nn+1)){
            te = m[nn+1].second;
        }*/

        k -= cn;

        //cout << k << "WSS" << endl;

        ll resn = 0;

        if(te >= k)
            resn = nn+1;
        else
            resn = nn;

        //cout << resn << "WTAWATAT" << endl;

        cout << "Case #" << tt << ": " << ceil((resn-1)/((double)2)) << " " << ((resn-1)/2) << endl;


    }

    return 0;

}
