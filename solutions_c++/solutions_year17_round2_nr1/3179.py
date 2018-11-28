#include<bits/stdc++.h>
using namespace std;


int D,N,K,S;

int main(){
    freopen("A-large.in","r",stdin);
    freopen("out.txt","w",stdout);

    int T;

    cin >> T;


    for(int k = 0; k < T; k++){

        cin >> D >> N;

        double mT = DBL_MIN;

        for(int l = 0; l < N; l++){
            cin >> K >> S;

            double tt = (D-K)/(double)S;

            mT = max(tt,mT);

        }

        double res = (double)D / mT;

        printf("Case #%d: %0.7f\n",k+1,res);

        //cout << "Case #" << k+1 << endl;
    }




}
