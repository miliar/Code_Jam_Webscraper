#include <iostream>
using namespace std;

long long findAns(long long n) {

    // finding length...
    long long l = 0, tmp = n, ans = 0;
    while(tmp) {
        l++;
        tmp/=10;
    }

    // converting to array...
    int arr[l];
    for(int i=0; i<l; i++) {
        arr[l-1-i] = n%10;
        n /= 10;
    }

    // converting to largest sorted number...
    int i = l-1;
    while(i > 0){
        if(arr[i] < arr[i-1]) {
            arr[i-1]--;
            int j = i;
            while(j < l && arr[j] != 9) {
                arr[j] = 9;
                j++;
            }
        }
        i--;
    }
    
    //printing..
    i = 0;
    while(arr[i] == 0) i++;
    while(i<l) {
        ans = ans*10 + arr[i];
        i++;
    }

    return ans;
}

int main() {
    int t;
    cin>>t;

    for(int i=1; i<=t; i++) {
        long long n;
        cin>>n;
        cout<<"Case #"<<i<<": "<<findAns(n);
        if(i < t) cout<<"\n";
    }
    return 0;
}