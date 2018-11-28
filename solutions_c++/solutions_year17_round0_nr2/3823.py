#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <string>
#include <cstring>
using namespace std;

int main(){
    int n;
    string input;
    long long int length;
    int a[10000];
    bool find,flag;
    int c_counter = 0;
    int bit;

    cin >> n;
    for (int i = 0; i < n; i++) {
        c_counter++;
        cin >> input;
        length = input.length();
        for (int j = 0; j < length; j++) {
            a[j] = input[j] - '0';
            // cout <<a[j]<<" ";
        }
        find = false;
        bit = 0;
        while (!find) {
            flag = 0;
            if ( a[bit] == 0 ) bit++;
            for (int k = length-1; k>=bit+1; k--) {
                if ( a[k-1] > a[k] ) {
                    flag = 1;
                    a[k-1]--;
                    for (int j = k; j < length; j++)
                        a[j] = 9;
                }
            }
            if ( !flag ) find = true;
            // if ( flag )
            // a[length-1]--;
            // for (int k = length-1; k>=1; k--) {
            //     if ( a[k] < 0 ) {
            //         a[k] = a[k] + 10;
            //         a[k-1]--;
            //       }
            // }
            // cout<<endl;
            // for (int j = bit+1; j < length; j++)
            //     cout<<a[j];
            // cout<<endl;
      }


    cout<<"Case #"<<c_counter<<": ";
    for (int j = bit; j < length; j++)
        cout<<a[j];
    cout<<endl;
    }
}
