
#include <bits/stdc++.h>

using namespace std;


typedef long long int ll;




int main(){




    int t;

    cin >> t;




    for(int tt = 1;tt<=t;tt++){


        int N,P;

        cin >> N >> P;


        int arr[105];
        int arrg[105];

        for(int i=0;i<N;i++){

            cin >> arr[i];

            arrg[i] = arr[i] % P;

        }


        int res = 0;


        int arro[5] = {0,0,0,0,0};

        for(int i=0;i<N;i++){

            arro[arrg[i]]++;

        }



        res += arro[0];

        for(int i=1;i<P;i++){

            int ost = P-i;

            int nowp = arro[i];
            int needp = arro[ost];

            res += min(nowp,needp);

            arro[i] -= min(nowp,needp);
            arro[ost] -= min(nowp,needp);
        }


        if(P == 1){
            //cout << "Case #" << tt << ": " << res << endl;

        }

        if(P == 2){
            res += ceil(((double)arro[1])/P);


        }

        if(P == 3){
            res += ceil(((double)arro[1])/P);
            res += ceil(((double)arro[2])/P);
        }

        if(P == 4){
            if(arro[2] > 0){
                res ++;

                if(arro[1] > 0){
                    arro[1] -= 2;
                    if(arro[1] > 0){
                        res += ceil(((double)arro[1])/P);
                    }
                }
                else{
                    arro[3] -= 2;

                    if(arro[3] > 0){
                        res += ceil(((double)arro[3])/P);
                    }
                }


            }
            else{
                if(arro[1] > 0){
                    res += ceil(((double)arro[1])/P);
                }
                if(arro[3] > 0){
                    res += ceil(((double)arro[3])/P);
                }
            }
        }

        cout << "Case #" << tt << ": " << res << endl;



    }

    return 0;

}
