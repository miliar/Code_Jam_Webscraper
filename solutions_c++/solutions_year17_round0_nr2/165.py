#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
int tc;
long long n;
vector<int> str;
int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    cin>>tc;
    for(int ct=1;ct<=tc;++ct){
        cin>>n;
        str.clear();
        while(n>0ll){
            str.push_back(n%10ll);
            n/=10ll;
        }
        for(auto it=str.begin();it!=str.end();++it){
            if(it!=str.begin()&&(*it)>(*(it-1))){
                --(*it);
                for(auto it2=str.begin();it2!=it;++it2){
                    *it2=9;
                }
            }
        }
        cout<<"Case #"<<ct<<": ";
        //bool nonzero=false;
        for(auto it=str.crbegin();it!=str.crend();++it){
            if(/*nonzero||*/(*it)!=0){
                cout<<(char)('0'+(*it));
                //nonzero=true;
            }
        }
        cout<<endl;
    }
}

