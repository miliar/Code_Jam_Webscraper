#include <iostream>
#include <cstring>
#include <cmath>

using namespace std;

bool check(long long k){
    long long lastDigit = 9;
    while (k > 0){
        long long l = k % 10;
        if (lastDigit < l)
            return false;
        k /= 10;
        lastDigit = l;
    }
    return true;
}

int main(){
    int n;
    cin>>n;
    long long number[100];
    for (int i = 0; i < n; i++){
        long long k;
        cin>>k;
        while(!check(k)){
            int length = 0;
            long long k2 = k;
            while (k2 > 0){
                number[length++] = k2 % 10;
                k2 /= 10;
            }
            bool flag = true;
            long long mn = 0;
            for (int j = length-1; j > 0; j--){
                if (flag){
                    if (number[j] > number[j-1]){

                        flag = false;
                        mn = (long long)round(pow(10, j));
                        number[j-1] = 9;
                    }
                }
                else{
                    number[j-1] = 9;

                }
            }
            k2 = 0;
            for (int j= 0; j< length; j++){
                k2 += number[j]* (long long)round(pow(10, j));
            }
            k = k2 - mn;
        }
        cout<<"Case #"<<i+1<<": "<<k<<endl;
    }
}
