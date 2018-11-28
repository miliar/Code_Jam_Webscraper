#include <cstdio>
#include <cstdlib>
#include <cassert>
#include <iostream>
#include<math.h>
#include <string>
using namespace std;

int main() {
    int t,result=0;
    int l,r;
    //string n;
    long long n,tt;
    FILE *fin = freopen("/Users/kimmyongjoon/Desktop/problem/in", "r", stdin);
    assert( fin!=NULL );
    FILE *fout = freopen("/Users/kimmyongjoon/Desktop/problem/out", "w", stdout);
    cin>>t;
    for(int i=0;i<t;i++){
        cin>>n;
        tt=n;
        while(1){
            n=tt;
            while(1){
                if(n==0||n<10){
                    n=0;
                    break;
                }
                r=n%10;
                l=(n%100-r)/10;
                if(l>r){
                    break;;
                }
                n=n/10;
            }
            if(n==0){
                break;
            }else{
                tt--;
            }
        }
        cout<<"Case #"<<i+1<<": "<<tt<<endl;
    }
    exit(0);
    
}
