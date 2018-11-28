#pragma GCC optimize "Ofast,omit-frame-pointer,inline"
#include <bits/stdc++.h>
using namespace std;

int n,D;

class Horse{
    public:

    int start;
    int speed;
    Horse(int x,int y){
        start = x;
        speed = y;
    }
    bool operator < (const Horse &other){
        return this->start < other.start;
    }
};

vector<Horse> horses;

int main(){
    ios::sync_with_stdio(false);
    freopen("gcj1input.in","r",stdin);
    freopen("output1.txt","w",stdout);
    int t,i,x,s,c=1;
    double slowestHorseTime;
    cin>>t;
    while(t--){
        horses.clear();
    	cin>>D>>n;
    	for(i=0;i<n;i++){
            cin>>x>>s;
            horses.push_back(Horse(x,s));
        }
        sort(horses.begin(),horses.end());

        // for(i=0;i<n;i++){
        //     cout<<horses[i].start<<" "<<horses[i].speed<<" ";
        // }
        // cout<<endl;

        slowestHorseTime = ((double)D-horses[n-1].start)/horses[n-1].speed;
        // cout<<slowestHorseTime<<" ";
        for(i=n-2;i>=0;i--){
            slowestHorseTime =  max( (double)(D-horses[i].start)/(double)horses[i].speed, (double)slowestHorseTime);
            // cout<<slowestHorseTime<<" ";                
        }
        // cout<<endl;
    	cout<<"Case #"<<c++<<": "<<std::fixed<<std::setprecision(12)<<D/slowestHorseTime<<endl;
    }
	return 0;
}