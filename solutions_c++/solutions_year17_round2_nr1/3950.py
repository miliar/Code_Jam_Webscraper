#include <bits/stdc++.h>
using namespace std;



struct horse{
    horse(int k,int s):k(k),s(s){}
    int k;
    int s;
    void print(){
        cout<<"k="<<k<<endl;
        cout<<"s="<<s<<endl;
        cout<<endl;
    }
};
bool comp(horse a,horse b){
    return a.k<b.k;
}

int main() {
    freopen("inputA","r",stdin);
    freopen("outputA","w",stdout);
    int tests;
    cin>>tests;
    for (int T = 1; T <= tests; ++T) {
        int D,N;
        cin>>D>>N;
        float ans=0;

        int k,s;
        vector<horse> horses;
        for (int i = 0; i < N; ++i) {
            cin>>k>>s;
            horses.push_back(horse(k,s));
        }
        sort(horses.begin(),horses.end(),comp);
//        for (int i = 0; i < horses.size(); ++i) {
//            horses[i].print();
//        }
        float minTime=(D-horses[horses.size()-1].k)*1.0/(horses[horses.size()-1].s);
//        cout<<minTime<<endl;
        for (int i = horses.size()-2; i>=0; --i) {
            if(horses[i].s>horses[i+1].s){
                if((horses[i+1].k-horses[i].k)*1.0/(horses[i].s-horses[i+1].s)>minTime){
                    minTime=(D-horses[i].k)*1.0/(horses[i].s);
                }


//                minTime=min(minTime,
//                            (horses[i+1].k-horses[i].k)*1.0/(horses[i+1].s-horses[i].s));
            }else{
//                cout<<"AA";
                minTime=(D-horses[i].k)*1.0/(horses[i].s);
            }
        }
//        printf("%.6f\n",D*1.0/minTime);







       








//        cout<<"Case #"<<T<<": "<<endl;
        printf("Case #%d: %.6f\n",T,D*1.0/minTime);
    }
    fclose(stdin);
    fclose(stdout);
    return 0;
}
