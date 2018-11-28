#include <iostream>
#include <algorithm>
#include <cmath>
#include <vector>
#include <set>
#include <iomanip>


using namespace std;

typedef long long int lli;


double solve(vector<lli> & K, vector<lli>& S, lli D){

    lli N = K.size();

    double best_speed = 0;


    for(int i=0; i<N; i++){

        double t = ((double)(D-K[i]))/((double)(S[i]));

        double speed = (double)D/t;

        if( i == 0) best_speed = speed;
        else {

            best_speed = min(best_speed, speed);
        }
    }

    return best_speed;


}


void try_sequential(){
    int T;
    cin>>T;
    //lli N,K;

    for(int c=1; c<=T; c++){

        lli D, N;

        cin>>D>>N;

        vector<lli> K(N), S(N);

        for(int i=0; i<N; i++){

            lli tmpK, tmpS;

            cin>>tmpK>>tmpS;

            K[i] = tmpK;

            S[i] = tmpS;
        }



        //std::cout << std::fixed;
        //std::cout << std::setprecision(6);
        cout<<"Case #"<<c<<": "<< std::fixed<<std::setprecision(6)<<solve(K, S, D)<<endl;

    }
}

int main(int argc, char *argv[])
{
    try_sequential();
    return 0;
}
