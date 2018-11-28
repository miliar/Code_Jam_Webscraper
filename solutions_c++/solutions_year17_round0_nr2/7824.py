#include <vector>
#include <iostream>
#include <math.h>
#include <string>

using namespace std;

int main(){
    int t;
    long long int n;
    int l;
    vector<int> a;
    cin>>t;
    for(int q = 1; q<=t; q++){
        l = 0;
        cin>>n;
        a.clear();
        if(n>=1 && n<=9){
           cout<<"Case #"<<q<<": "<<n<<endl;
           continue; 
        }
        while(n){
            l++;
            a.push_back(n%10);
            n /= 10;
        }
        int k = l-1;
        bool u = 0;
        for(int i = l-2; i>=0; i--){
            k = i+1;
            if(a[i]<a[i+1]){
                u = 1;
                break;
            }
        }
        long long int p = 0;
        long long int m = 1;
        if(u){
        int j = k;
        for(int i = k+1; i<l; i++){
            if(a[i] != a[k]){
                break;
            }
            j++;
        }
        
            a[j] = a[j]-1;
            for(int i = j-1; i>=0; i--){
                a[i] = 9;
            }
        }
            for(int i = 0; i<l; i++){
                p += a[i]*m;
                m *= 10;
            }
        
        cout<<"Case #"<<q<<": "<<p<<endl;
    }
    return 0;
}