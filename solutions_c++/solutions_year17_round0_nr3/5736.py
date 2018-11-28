#include <bits/stdc++.h>
using namespace std;
typedef long long lln;
typedef pair<lln,lln> PII;

class Comp{
    public:
        bool operator () (PII A,PII B){
            if(A.first-A.second > B.first-B.second)
               return true;
            else if(A.first-A.second==B.first-B.second){
				if(A.first>B.first) return true;
				else return false;
			}
               
			else return false;
        }
};

void Solve();
int main(){
//    freopen("input.txt","r",stdin);
//    freopen("output.txt","w",stdout);
    int t; cin>>t;
    for(int i=1;i<=t;i++){
         cout<<"Case #"<<i<<": ";
         Solve();
    }
    return 0;
}

void Solve(){
    priority_queue<PII,vector<PII>,Comp> PQ;
    lln N,P; cin>>N>>P;
    PQ.push(make_pair(1,N+2));

    for(int i=1;i<P;i++){
        if(!PQ.empty()){
            PII Temp = PQ.top();
            PQ.pop();
            lln low = Temp.first;
            lln high = Temp.second;
            //  cout<<low<<" "<<high<<"\n";
            lln mid = low + (high-low)/2;
            PQ.push(make_pair(low,mid));
            PQ.push(make_pair(mid,high));
        }
    }

    PII T = PQ.top();
    lln low = T.first;
    lln high = T.second;
    lln mid = low + (high-low)/2;
    //  cout<<low<<" "<<high<<" "<<mid<<"\n";

    lln MAXX = INT_MIN;
    lln MIN = INT_MAX;
    MAXX = max(MAXX,max(abs(low-mid),abs(mid-high)));
    MIN = min(MIN,min(abs(low-mid),abs(mid-high)));
    cout<<MAXX-1<<" "<<MIN-1<<"\n";

    return;
}
