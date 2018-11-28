#include<vector>
#include<iostream>
#include<set>
#include<map>
#include<unordered_map>
#include<string.h>
#include<algorithm>
#include<stdlib.h>
#include<queue>
#include<cmath>
#include<unordered_set>
#include<numeric>
using namespace std;

typedef long long ll;

#define FOR(i,n) for(int i=0;i<n;i++)
#define out(a) for(auto i:a)cout<<i<<" ";
#define outl(a) for(auto i:a)cout<<i<<endl;

//ll n,m,k;
string str,s1,s2;

int gcd(int a, int b){
    if(b==0)return a;
    return gcd(b,a%b);
}



int main(){
    freopen("/Users/shitian/Desktop/gcj/gcj/B-small-attempt0.in","r",stdin);
    freopen("/Users/shitian/Desktop/gcj/gcj/B-small-attempt0.txt","w",stdout);
    int tcase;
    cin>>tcase;
    for(int tc=1;tc<=tcase;tc++){
        cout<<"Case #"<<tc<<": ";
        
        int n, r, o, y, g, b, v;
        cin>>n>>r>>o>>y>>g>>b>>v;
        string vec;
        if(r){
            vec.push_back('R');
            r--;
        }
        else if(y){
            vec.push_back('Y');
            y--;
        }
        else if(b){
            vec.push_back('B');
            b--;
        }
        bool ok=true;
        while(r>0||o>0||y>0||g>0||b>0||v>0){
            if(vec.back()=='R'){
                if(b>y){
                    vec.push_back('B');
                    b--;
                } else if(y>0){
                    vec.push_back('Y');
                    y--;
                } else {
                    ok=false;
                    break;
                }
            }else if(vec.back()=='B'){
                if(r>y){
                    vec.push_back('R');
                    r--;
                } else if(y>0){
                    vec.push_back('Y');
                    y--;
                } else {
                    ok=false;
                    break;
                }
            }else if(vec.back()=='Y'){
                if(b>r){
                    vec.push_back('B');
                    b--;
                } else if(r>0){
                    vec.push_back('R');
                    r--;
                } else {
                    ok=false;
                    break;
                }
            }
        }
        if(ok){
            if(vec.front()==vec.back()){
                ok=false;
            }
        }
        if(!ok){
            cout<<"Impossible"<<endl;
        } else {
            cout<<vec<<endl;
        }
    }
    
    return 0;
}
