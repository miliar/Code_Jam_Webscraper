#include<bits/stdc++.h>
using namespace std;
int main()
{
    ifstream cin("input.in");
    ofstream cout("output.out");
    ios::sync_with_stdio(0);cin.tie(0);
    long T,t=1;
    cin>>T;
    while(t<=T){
        long N,A,B,C,X;
        vector<pair<long,char> >V;
        cin>>N>>A>>X>>B>>X>>C>>X;
        V.push_back(make_pair(A,'R'));
        V.push_back(make_pair(B,'Y'));
        V.push_back(make_pair(C,'B'));
        sort(V.begin(),V.end());
        if(V[2].first>V[1].first+V[0].first)
            cout<<"Case #"<<t<<": IMPOSSIBLE\n";
        else{
            cout<<"Case #"<<t<<": ";
            long K=V[0].first+V[1].first-V[2].first;
            //cout<<K<<" ";
            V[0].first-=K;
            V[1].first-=K;
            V[2].first-=K;
            while(K--)
                cout<<V[2].second<<V[1].second<<V[0].second;
            sort(V.begin(),V.end());
            K=V[0].first;
            //cout<<K<<" ";
            V[0].first-=K;
            //V[1].first-=K;
            V[2].first-=K;
            while(K--){
                cout<<V[2].second<<V[0].second;
            }
            //sort(V.begin(),V.end());
            K=V[1].first;
            //cout<<K<<" ";
            V[0].first-=K;
            V[1].first-=K;
            V[2].first-=K;
            while(K--){
                cout<<V[2].second<<V[1].second;
            }
            cout<<"\n";
        }
        t++;
    }
}