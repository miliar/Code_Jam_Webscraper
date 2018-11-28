#include<iostream>
#include<vector>
using namespace std;

long long tidy(long long n){
    int j=0;
    vector<int> a(20);
    while(n>0){
        a[j++]=n%10;
        n/=10;
    }
    --j;
    for(int i=j;i>0;i--){
        if(a[i]>a[i-1]){
           while(a[i]==a[i+1])
                i++;
            --a[i];
            --i;
            while(i>=0){
                a[i]=9;
                i--;
            }
        }
    }
    n=0;
    for(int i=j;i>=0;i--){
        n=n*10+a[i];
    }
    return n;
}

int main(){
    int test;
    cin >> test;
    for(int i=1;i<=test;i++){
        long long n;
        cin >> n;
        cout << "Case #"<<i<<": "<<tidy(n) << endl;
    }
    return 0;
}
