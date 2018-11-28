#include<iostream>
#include<string>
#include<map>
#include<vector>
#include<stdlib.h>
#include<iomanip>
using namespace std;

int main(){
    int TT;
    cin>>TT;
    int n;
    long double d;
    long double p[2000];
    long double s[2000];
    long double a[2000];
    for(int T=1;T<=TT;++T){
        cin>>d>>n;
        for(int i=0;i<n;++i){
            cin>>p[i]>>s[i];
        }
        long double mi=-1;
        for(int i=0;i<n;++i){
            if(d-p[i]==0)
                continue;
            long double t=d/(d-p[i])*s[i];
            if(mi<0 || t<=mi){
                mi=t;
            }
        }

        cout<<fixed;
        cout<<"Case #"<<T<<": "<<setprecision(8)<<mi;
        cout<<endl;
        
    }
    return 0;
}




//map<int,int> mp;
//for(int i=0;i<10;++i){
//    mp.insert(make_pair(i,0));
//}
//for(auto it=mp.begin();it!=mp.end();++it){
//    cout<<it->first;
//}
