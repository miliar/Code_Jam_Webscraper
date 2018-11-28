#include <cstdio>
#include <cstdlib>
#include <cassert>
#include <iostream>
#include<math.h>
#include <string>
#include<vector>
#include<queue>
using namespace std;
int choice_max_index(string in,int n){
    int max_num=0;
    int max_pos=0;
    int cur_num=0;
    for(int i=0;i<in.size()+1-n;i++){
        cur_num=0;
        for(int ii=0;ii<n;ii++){
            if(in.at(i+ii)=='-'){
                cur_num++;
            }
        }
        if(cur_num>max_num){
            max_num=cur_num;
            max_pos=i;
        }
    }
    return max_pos;
};
bool check(string n){
    for(int i=0;i<n.size();i++){
        if(n.at(i)=='-'){
            return false;
        }
    }
    return true;
};
string flip(string in,int pos,int n){
    for(int i=0;i<n;i++){
        if(in.at(pos+i)=='-'){
            in.replace(pos+i, 1, string("+"));
        }else{
            in.replace(pos+i, 1, string("-"));
        }
    }
    return in;
}
int main() {
    vector<long long> v;
    int t,n,time,pos;
    string in;
    FILE *fin = freopen("/Users/kimmyongjoon/Desktop/problem/in", "r", stdin);
    assert( fin!=NULL );
    FILE *fout = freopen("/Users/kimmyongjoon/Desktop/problem/out", "w", stdout);
    cin>>t;
    for(int i=0;i<t;i++){
        cin>>in>>n;
        time=0;
        for(int j=0;j<in.size()-n+1;j++){
            if(in.at(j)=='-'){
                in=flip(in,j,n);
                time++;
            }
        }
        cout<<"Case #"<<i+1<<": ";
        if(!check(in)){
            cout<<"IMPOSSIBLE"<<endl;
        }else{
            cout<<time<<endl;
        }
        
    }
    exit(0);
    
}
