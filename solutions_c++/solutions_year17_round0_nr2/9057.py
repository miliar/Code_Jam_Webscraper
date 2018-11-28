#include <iostream>
#include <vector>
#include <math.h>
#include <stdio.h>

using namespace std;

int main()
{
    freopen("in.in","r",stdin);
    freopen("out","w",stdout);
    int t;
    cin>>t;
    long long N;
    long long arr[t];
    long long res[t];
    for(int i = 0; i < t; i ++) {
        cin>>arr[i];
    }
    for(int n = 0; n < t; n ++){
        N = arr[n];
        long long k=N;
        int cnt = 0;
        while(k > 0) {
            cnt ++;
            k /= 10;
        }
        int v[cnt];
        k = N;
        for(int i = 0; i < cnt; i ++) {
            v[i] = k%10;
            k /= 10;
        }
        int flag = 1;
        int l = -1;
        for(int i = 1; i < cnt; i ++) {
            if(v[i] > v[i-1]){
                v[i] --;
                for(int j = i - 1; j >= 0; j --) {
                    v[j] = 9;
                }
            }
        }
        long long sum = 0;
        for(int i = 0; i < cnt; i ++) {
            sum += v[i] * powl(10.0,i);
        }
        res[n] = sum;
    }
    for(int i = 0; i < t; i ++) {
        cout<<"case #"<<i + 1<<": "<<res[i]<<endl;
    }

    return 0;
}
