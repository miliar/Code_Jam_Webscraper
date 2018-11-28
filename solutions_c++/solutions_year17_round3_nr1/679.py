#include<iostream>
#include<algorithm>
#include<cstdio>
using namespace std;
#define M_PI 3.14159265358979323846
pair<long long,long long> p[1001];
int main(){
    freopen("A-large.in","r",stdin);
    freopen("Aout.txt","w",stdout);
    int cas,q;
    cin>>cas;
    for(q=1;q<=cas;q++){
        int N,K;
        cin>>N>>K;
        for(int i=0; i < N; i++)cin>>p[i].first>>p[i].second;

        sort(p,p+N,[](const pair<long long,long long> &A, const pair<long long,long long> &B){
             return (A.first*A.second < B.first*B.second || (A.first*A.second == B.first*B.second && A.first < B.first));});
        long long sol = -1;

        for(int i=0; i < N; i++){
            int cnt = 1;
            long long tmp = (long long)p[i].first*(p[i].first + p[i].second*2);
            for(int j = N-1; j >=0 && cnt < K; j--){
                if(i!=j && p[j].first <= p[i].first){
                    tmp += (long long)p[j].first*p[j].second*2;
                    cnt++;
                }
            }
            if(cnt == K && tmp > sol)sol = tmp;
        }
        printf("Case #%d: %.10Lf\n",q,(long double)sol*M_PI);
    }
    return 0;
}
