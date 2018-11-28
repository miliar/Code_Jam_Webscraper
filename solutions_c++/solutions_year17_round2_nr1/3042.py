#include<bits/stdc++.h>
using namespace std;
struct node {
    long long int start;
    long long int speed;
    bool operator< ( const node& other ) const
    {
          return start > other.start;
    }
};
void printoutput(long long int testcase,long double ans){
    cout<<fixed<<setprecision(6);
    cout<<"Case #"<<testcase<<": "<<ans<<"\n";
    return;
}
int main(){
    freopen("C:\\Users\\Dell\\Desktop\\codejam\\inp.in", "r", stdin);
	freopen("C:\\Users\\Dell\\Desktop\\codejam\\output.txt", "w", stdout);
    long long int t;
    cin>>t;
    for(long long int testcase = 1; testcase <= t; testcase++){
        long long int dest,horses;
        cin>>dest>>horses;
        struct node a[horses];
        for(long long int i = 0; i < horses; i++){
            cin>>a[i].start>>a[i].speed;
        }
        sort(a,a+horses);
        long double time = -1;
        for(long long int i = horses - 1; i >= 0; i--){
            if(a[i].start < dest){
                if(time < 0){
                    time = (long double)(dest - a[i].start) / a[i].speed;
                }
                else{
                    long double newtime = (long double)(dest - a[i].start) / a[i].speed;
                    if(newtime > time){
                        time = newtime;
                    }
                }
            }
        }
        long double ans;
        ans = (long double)dest / time;
        printoutput(testcase,ans);
    }
    return 0;
}
