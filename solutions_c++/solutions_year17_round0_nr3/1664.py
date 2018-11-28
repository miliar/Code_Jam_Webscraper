#include<iostream>
#include<vector>
#include<fstream>
#include<map>
#define ll long long

using namespace std;

int main(){
    ifstream in("C-large.in");
    ofstream out("C-large.out");

    ll t,n,k;
    in >> t;
    for(int h=0;h<t;++h){
        map<ll,ll> q;
        in >> n >> k;

        q.insert(make_pair(-n,1));
        ll l,r;
        while(k){
                l = (q.begin()->first+1)/2;
                if(q.begin()->first % 2 == 0){
                    r = l - 1;
                } else{
                    r = l;
                }

                if(k<= q.begin()->second){
                    break;
                }
                k-=q.begin()->second;
                q[l] += q.begin()->second;
                q[r] += q.begin()->second;
                q.erase(q.begin());

        }
        out <<"Case #"<<h+1<<": "<< -r<< " "<<-l<<endl;
    }
}
