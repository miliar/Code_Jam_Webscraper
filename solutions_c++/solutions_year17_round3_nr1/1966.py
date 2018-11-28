#include <bits/stdc++.h>
using namespace std;


struct pancake{
    long long r;
    long long h;
};
istream& operator>>(istream& stream,pancake& p){
    stream>>p.r>>p.h;
    return stream;
}
ostream& operator<<(ostream& stream,const pancake& p){
    stream<<p.r<<" "<<p.h<<endl;
    return stream;
}
//2pir * h
bool comp(pancake p1,pancake p2){
    return p1.h*p1.r>p2.h*p2.r;
}
bool comp2(pancake p1,pancake p2){
    return p1.r>p2.r;
}

int main() {
    freopen("inputA","r",stdin);
    freopen("outputA","w",stdout);
    int tests;
    cin>>tests;
    for (int T = 1; T <= tests; ++T) {
        int n,k;
        cin>>n>>k;
        vector<pancake> v;
        pancake p;
        for (int i = 0; i < n; ++i) {
            cin>>p;
            v.push_back(p);
        }
        sort(v.begin(),v.end(),comp);
//        for (int i = 0; i < v.size(); ++i) {
//            cout<<v[i];
//        }




        long long maxR =0;

        for (int i = 0; i < k; ++i) {
            if(v[i].r>=maxR){
                maxR=v[i].r;
            }
        }
//        for (int i = 0; i < k; ++i) {
//            cout<<v[i];
//        }
//        cout<<endl;

        for (int i = k; i < v.size(); ++i) {
            if(v[i].r>maxR&&2*v[i].r*v[i].h+(v[i].r*v[i].r-maxR*maxR)>2*v[k-1].r*v[k-1].h){
                v[k-1]=v[i];
                maxR=v[i].r;
            }
        }
//        for (int i = 0; i < k; ++i) {
//            cout<<v[i];
//        }
//        cout<<endl;

        long long ans=maxR*maxR;
        for (int i = 0; i < k; ++i) {
            ans+=2*v[i].r*v[i].h;
        }













        printf("Case #%d: %.10f\n",T,double(ans*1.*M_PI));
//        cout<<"Case #"<<T<<": "<<endl;
    }
    fclose(stdin);
    fclose(stdout);
    return 0;
}
