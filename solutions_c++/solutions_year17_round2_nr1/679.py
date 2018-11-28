#include <bits/stdc++.h>
using namespace std;
const int maxn = 2333;
double k[maxn],d[maxn];
int T,n;
long long D,K;
int main(){
    freopen("out.txt","w",stdout); 
    std::cin>>T;
    int _case = 0;
    while(T--){
        cin>>D>>n;
        for(int i=1;i<=n;i++){
            scanf("%lf%lf",&d[i],&k[i]);
        }
        double speed=D*k[1]/(D-d[1]);
        for(int i=1;i<=n;i++){
            speed=min(speed,D*k[i]/(D-d[i]));
        }
        cout<<"Case #"<<++_case<<": ";
        printf("%.6lf\n",speed);
        
    }
    return 0;
}
