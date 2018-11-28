#include<iostream>
#include<string>
#include<vector>
#include<map>
#include<unordered_map>
#include<set>
#include<algorithm>
#include<iomanip>

using namespace std;


int main(){

    int T;
    cin>>T;
    for (int t=0;t<T;t++){

    long long D;
    int N;
    cin>>D;
    cin>>N;
    unordered_map<long long,long long> horses;
    for (int i=0;i<N;i++){
        long long ki;
        long long si;
        cin>>ki;
        cin>>si;
        horses.emplace(ki,si);
    }
    double tSlowest= (D - horses.begin()->first)/horses.begin()->second;
    for (const auto &p : horses) {
            double ti = (D - p.first)/(double)p.second;
            if(ti>tSlowest){
                tSlowest =ti;
            }
    }
        cout<<"Case #"<<t+1<<": "<<setprecision (6) << fixed << D/tSlowest<<endl;
        }
    return 0;
}
