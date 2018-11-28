#include<cstdio>
#include<iostream>
#include<algorithm>
#include<cstring>
#include<vector>
#include<stack>
#include<map>
#include<queue>
#include<set>
//#inlcude<iomanip>

using namespace std;
//int m[6];
//int ma[6];
//long long getans(long long N){
//   
//    return ans;
//}
int AN = 60;
int a[60]={4,8,8,8,8,8,7,8,14,5,2,13,8,5,7,3,AN,6,7,8,13,5,2,12,8,5,7,3,AN,6,1,7,10,11,5,9,10,5,11,9,5,8,8,26,6};
int main()
{
    freopen ("/Users/Victor/Desktop/myfile.txt","w",stdout);
    freopen ("/Users/Victor/Desktop/A-large.in","r",stdin);
    int n;
    cin >> n;
    for (int i = 0; i<n; i++) {
        int D,N;
        cin >> D >> N;
        double tmax = 0;
        for (int j = 0; j<N; j++) {
            int k,s;
            cin >> k >> s;
            double t = (D-k) *1.0 / s;
            if (t > tmax) {
                tmax  = t;
            }
            
        }
//        cout << tmax <<endl;<<fixed<<setprecision(8)
//        cout.precision(8);
        printf("Case #%d: %.8lf\n",i+1,D * 1.0/ tmax);
//        cout << "Case #"<<i+1<<": "<<D * 1.0/ tmax<<endl;
    }
    return 0;
}

