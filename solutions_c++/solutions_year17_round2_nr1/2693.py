#include <iostream>
#include<iomanip>
using namespace std;

int main() {
    freopen("/Users/qianzhi/Downloads/A-large.in.txt", "r", stdin);
    freopen("/Users/qianzhi/Desktop/A-large.out", "w", stdout);
    int t;
    cin>>t;  //case
    for(int i = 1; i<=t;i++){
        double d,n;
        cin>>d>>n;
        double tmax = 0;
        double time,k,s;
        for(int j = 0;j<n;j++){
            cin>>k>>s;
            time = (d - k)/ s;
            if(time > tmax)
                tmax = time;
        }
        double y;
        y = d / tmax;
        cout << "Case #"<< i<<": "<<fixed <<setprecision(6) <<y<<endl;
    }
}