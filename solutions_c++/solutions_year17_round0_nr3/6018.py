#include <cstdio>
#include <cstdlib>
#include <cassert>
#include <iostream>
#include<math.h>
#include <string>
#include<vector>
#include<queue>
int cal_min(int n){
    return (n-1)/2;
}
int cal_max(int n){
    return n/2;
}
using namespace std;

int main() {
    vector<int> v;
    int t,n,k,k_min=0,k_max=0,cur;
    FILE *fin = freopen("/Users/kimmyongjoon/Desktop/problem/in", "r", stdin);
    assert( fin!=NULL );
    FILE *fout = freopen("/Users/kimmyongjoon/Desktop/problem/out", "w", stdout);
    cin>>t;
    for(int i=0;i<t;i++){
        cin>>n>>k;
        v.clear();
        v.push_back(n);
        make_heap(v.begin(), v.end());
        for(int kk=0;kk<k;kk++){
            k_max=cal_max(v.front());
            k_min=cal_min(v.front());
            pop_heap(v.begin(), v.end());
            v.pop_back();
            if(k_min!=0){
                v.push_back(k_min);
                push_heap(v.begin(), v.end());
            }
            if(k_max!=0){
                v.push_back(k_max);
                push_heap(v.begin(), v.end());
            }
        }
        cout<<"Case #"<<i+1<<": "<<k_max<<" "<<k_min<<endl;
    }
    exit(0);
    
}
