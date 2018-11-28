#include <iostream>
#include <algorithm>
using namespace std;
int tc,n,p;
long long r[50]; // [n]
long long q[50][50]; // [n][p]
int offset[50];
inline bool exceeded(){
    for(int i=0;i<n;++i){
        if(offset[i]==p)return true;
    }
    return false;
}
int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    cin>>tc;
    for(int ct=1;ct<=tc;++ct){
        cin>>n>>p;
        for(int i=0;i<n;++i){
            cin>>r[i];
            offset[i]=0;
        }
        for(int i=0;i<n;++i){
            for(int j=0;j<p;++j){
                cin>>q[i][j];
            }
            sort(&q[i][0],&q[i][p]);
        }
        int kits=0;
        while(!exceeded()){
            int min_el=-1,max_el=-1;
            for(int i=0;i<n;++i){
                if(min_el==-1||q[i][offset[i]]*r[min_el]<q[min_el][offset[min_el]]*r[i]){
                    min_el=i;
                }
                if(max_el==-1||q[i][offset[i]]*r[max_el]>q[max_el][offset[max_el]]*r[i]){
                    max_el=i;
                }
            }
            // TODO: long long
            if(q[min_el][offset[min_el]]*r[max_el]*11<q[max_el][offset[max_el]]*r[min_el]*9){
                ++offset[min_el];
                continue;
            }
            long long max_servings=(q[min_el][offset[min_el]]*10)/(r[min_el]*9);
            long long min_servings=(q[max_el][offset[max_el]]*10-1)/(r[max_el]*11)+1;
            if(min_servings>max_servings){
                ++offset[min_el];
                continue;
            }
            ++kits;
            for(int i=0;i<n;++i){
                ++offset[i];
            }
        }
        cout<<"Case #"<<ct<<": "<<kits<<endl;
    }
}
