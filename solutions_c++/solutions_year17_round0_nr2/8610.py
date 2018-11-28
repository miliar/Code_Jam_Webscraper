//
// Created by 강경완 on 2017. 4. 8..
//

#include <math.h>
#include "iostream"

using namespace std;

unsigned long long checkOrderNum(unsigned long long n);

int main() {

    int N;
    cin >> N;

    for (int i = 0; i < N; i++) {
        unsigned long long num;
        cin >> num;
//        for(unsigned long long j=num; j != 0; j--){

        cout << "Case #" << i+1 << ": " << checkOrderNum(num) << endl;
//                break;
//            }
        // cout << j << endl;
    }
}


unsigned long long checkOrderNum(unsigned long long v) {
    unsigned long long result;
    while(true) {
        unsigned long long value = v;
        int min = 10;
        int cnt = 0;
        do {
            //cout << "value " << value << "     min " << min << "   / value % 10 : " << value %10 << endl;
            if (cnt == 0 && value % 10 == 0) {
                v = v - 1;
                break;
            } else if (min < value % 10) {
              //  cout << v - v % 10 << "       CnT : " << cnt<< "    / " << (v %  (unsigned long long)pow(10, cnt)) <<endl;
//            if(value % 10 == 0)
                //  return checkOrderNum(v - pow(10, cnt));

                v = (v -(v %  (unsigned long long)pow(10, cnt)));
                //break;
            }

            min = value % 10;
            value /= 10;
            cnt++;
        } while (value > 0);
        if(result == v)
            break;
        result = v;
        //cout << "New Check : " << result << endl;
    }
    return v;
}