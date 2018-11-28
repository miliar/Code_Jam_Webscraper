
#include <bits/stdc++.h>

using namespace std;


typedef long long int ll;




int main(){


    int t;

    cin >> t;




    for(int tt = 1;tt<=t;tt++){

        ll c,j;


        vector < vector<ll> > v;
        cin >> c >> j;


        for(int i=0;i<c+j;i++){

            ll l,k;

            cin >> l >> k;

            vector<ll> tv;

            tv.push_back(l);
            tv.push_back(k);
            if(i < c)
                tv.push_back(1);
            else
                tv.push_back(2);

            v.push_back(tv);

        }



        sort(v.begin(),v.end(),[](auto &left, auto &right){
            return left[0] < right[0];
        });


        int lastis = 0;
        int ck = 0;

        int wc=0,wj=0;
        int frc,frj;

        vector< int > cac,caj;

        for(auto i : v){



            if(i[2] == 1){
                wc += i[1]-i[0];
            }
            else{
                wj += i[1]-i[0];
            }

            frc = 720-wc;
            frj = 720-wj;



        }


        for(int i=0;i<c+j;i++){

            int nowc = v[i][2];

            if(nowc == lastis){
                if(nowc == 1)
                    cac.push_back(v[i][0] - v[i-1][1]);
                else
                    caj.push_back(v[i][0] - v[i-1][1]);
            }
            else{
                if(lastis != 0)
                ck++;
                lastis = nowc;
            }

        }

        int nowc = v[0][2];
        int li = v.size()-1;
        if(nowc == lastis){
            if(nowc == 1)
                cac.push_back( (1440 - v[li][1]) + v[0][0] );
            else
                caj.push_back( (1440 - v[li][1]) + v[0][0] );
        }
        else{
            ck++;
            lastis = nowc;
        }


        //cout << ck << " -tt" << endl;


        sort(cac.begin(),cac.end());
        sort(caj.begin(),caj.end());



        //for(auto i : cac){
            //cout << i << " - t" << endl;
        //}



        int kci = cac.size();
        int kji = caj.size();



        for(auto i : cac){
            if(i <= frc){
                frc -= i;
                kci--;
            }
            else{
                break;
            }
        }

        for(auto i : caj){
            if(i <= frj){
                frj -= i;
                kji--;
            }
            else{
                break;
            }
        }

        ck += (kci*2+kji*2);

        cout << "Case #" << tt << ": "<< ck << endl;
    }

    return 0;

}
