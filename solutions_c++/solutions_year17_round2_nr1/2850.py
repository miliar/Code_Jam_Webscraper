//
// Created by 강경완 on 2017. 4. 23..
//

#include <iostream>

using namespace std;

int main(){

    int T;

    cin >> T;

    for(int i=0; i< T; i++){

        int D, N;
        cin >> D >> N;
        //cout << D << " / " << N << endl;
        int data[1010][2];
        double min = -1;
        int minN = 99999999999;
        for(int k=0; k<N; k++){
            cin >> data[k][0] >> data[k][1];
            if(min < ((((double)D - (double)data[k][0]))/ (double)data[k][1])){
                min = (((double)D - (double)data[k][0])/(double)data[k][1]);
                //cout << min << endl;
            }
        }
        //cout << min << endl;

        printf("Case #%d: %.6lf\n",i+1,  (double)D /min);



    }

}