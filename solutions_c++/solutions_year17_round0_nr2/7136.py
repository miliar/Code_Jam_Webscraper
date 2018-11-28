#include <cmath>  
#include <iostream>
using namespace std;

long long int n;
long long int test(long long int p){
    long long int a = p%10,m = p; 
    p = p/10;
    long long int st = a,i = 0;
    while(p > 0){
        if((p%10) <= a){
            a = p%10;
            p = p/10;
            i++;
        } 
        else{
            long long int po = pow(10,i+1);
            st = m%po;
            n = n-st-1;
            return 0;
        }
    } 
    return 1;
}
int main(){
    int ts;
    cin>>ts;
    int i = 1,flag = 0;
    while(i <= ts){
        cin>>n;
        flag = 0;
        while(n){
            if(test(n))
                flag = 1;
            if(flag == 1)
                break;
        }
        cout<<"Case #"<<i<<": "<<n<<"\n"; i++; 
    }
}