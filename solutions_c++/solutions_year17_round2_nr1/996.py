#include <iostream>
#include<vector>
#include<algorithm>
#include<fstream>

using namespace std;

bool Compare(pair<double,double> x,pair<double,double> y){
return x.first<y.first;
}


int main()
{
 //   ifstream fin("in.txt");
    ofstream fout("out.txt");
int T;
cin>>T;
int N;double D;
for(int i=0;i<T;i++){

    cin>>D>>N;
    vector<pair<double,double> > Ni;
    double a,b;
    for(int x=0;x<N;x++){
        cin>>a>>b;
        Ni.push_back({D-a,b});
    }
    sort(Ni.begin(),Ni.end(),Compare);
    double last_time=0;
    for(int x=0;x<N;x++){
        last_time=max(Ni[x].first/Ni[x].second,last_time);
    }
    //cout<<D<<" "<<last_time<<endl;
    double sth=D/last_time;
    fout.precision(6);
    fout<<fixed<<"Case #"<<i+1<<": "<<sth<<endl;
}
}
