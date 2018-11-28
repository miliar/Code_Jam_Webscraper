#include<iostream>
#include<algorithm>
#include<vector>
#include<fstream>
#include<queue>


using namespace std;
ifstream f1("input.in”);
ofstream f2("output.out”);
int main(){
    int T,X;
f1>>T;
X=T;
while(T--){
    priority_queue<pair<int,pair<int,int> > >q;
        pair<int,pair<int,int> > Pair,Pair1,Pair2;
int valuer,N,P;
    f1>>N>>P;
    q.push(make_pair(N+1,make_pair(0,N+1)));
    for(int i=1;i<P;i++){
        Pair=q.top();
        q.pop();
        Pair1=make_pair(Pair.first/2,make_pair(Pair.second.first,Pair.second.first+Pair.first/2));
        Pair2=make_pair((Pair.first+1)/2,make_pair(Pair1.second.first,Pair1.second.first+(Pair.first+1)/2));
        q.push(Pair1);
        q.push(Pair2);
    }
    Pair1=q.top();
    valuer=(Pair1.second.first+Pair1.second.second)/2;
    f2<<"Case #"<<X-T<<": "<<max(valuer-1-Pair1.second.first,Pair1.second.second-valuer-1)<<" "<<min(valuer-1-Pair1.second.first,Pair1.second.second-valuer-1)<<endl;
}
}
