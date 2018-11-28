#include<bits/stdc++.h>
using namespace std;
/*int binary(double v){
    double vel[1005];
    double tot = d/v;
    for(int i=0;i<n;i++){
        vel[i] = ((d - vec[i].first)*v)/d;
    }
    int flag = 1;
    for(int i=0;i<n;i++){
        if(vel[i] > vec[i].second)
            flag = -1;
        for(int j=i+1;j<n;j++){
            double temp = (vec[j].first - vec[i].first)/(vel[i]-vel[j]);
            if(temp < tot && temp >= 0)
                flag = = -1;
        }
    }
    return flag;
}*/
int main(){
    int t,test;
    cin >> t;
    test = 1;
    while(t--){
        
        vector<pair<double,double> > vec;
        double d;
        int n;
        cin >> d >> n;
        for(int i=0;i<n;i++){
            double k,s;
            cin >> k >> s;
            vec.push_back(make_pair(k,s));
        }
        vec.push_back(make_pair(0,(1e18)+10));

        sort(vec.begin(),vec.end());
 //       cout << vec[0].second - 1e18 << endl;
        double curr = vec[n].second;
        for(int i=n-1;i>=0;i--){
            if(vec[i].second <= curr)
                curr =vec[i].second;
            else{
                curr = ((d-vec[i].first)*curr)/(d-vec[i+1].first);
                if(curr > vec[i].second)
                    curr = vec[i].second;
            }
        }
        printf("Case #%d: %.6lf\n",test,curr);
        test++;
    }
    return 0;
}
