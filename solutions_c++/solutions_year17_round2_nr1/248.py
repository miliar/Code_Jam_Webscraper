#include <iostream>
#include <iomanip>
using namespace std;
int main(){
    int t;
    cin>>t;
    for (int j=0; j<t; ++j){
        int d, n;
        cin>>d>>n;
        double mt=0;
        for (int i=0; i<n; ++i){
            int k, s;
            cin>>k>>s;
            double ct = (double)(d-k)/s;
            if (ct>mt){mt=ct;}
        }
        cout<<"Case #"<<j+1<<": "<<fixed<<setprecision(6)<<d/mt<<endl;
    }
    return 0;
}
