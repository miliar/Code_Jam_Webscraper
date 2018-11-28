#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<set>
#include<map>
#include<vector>
#include<utility>
#include<queue>
#include<stack>
#include<string>
#include<cmath>

#define ri(X) scanf("%d",&X)
#define rii(X,Y) scanf("%d %d",&X,&Y)
#define rf(X) scanf("%lf",&X)
#define rff(X,Y) scanf("%lf %lf",&X,&Y)
#define mp(X,Y) make_pair(X,Y)
#define pii pair<int,int>
#define FOR(i,j) for(int i=0;i<j;i++)
#define FORC(i,j,c) for(int i=0;i<j;i+=c)

const double pi = acos(-1);

using namespace std;
int T;
vector<pair<long long, long long> > v;
priority_queue<long long> q;
int K,N;
int main(){
    cin >> T;
    FOR(t,T){
        long long max_area = 0LL;
        cout << "Case #" << t + 1 << ": ";
        cin >> N >> K;
        v.clear(); v.resize(N);
        FOR(i,N){
            cin >> v[i].first >> v[i].second;
        }
        sort(v.begin(), v.end());
        for(int j = K-1; j<N;j++) {
            long long new_area = (v[j].first * v[j].first) + 2LL * v[j].first * v[j].second;
            while(!q.empty()) q.pop();
            for(int k = 0;k<j;k++){
                q.push(2LL * v[k].second * v[k].first);

            }
            int cnt = K-1;
            while(cnt){
                long long add = q.top();
                q.pop();
                new_area += add; 
                cnt--;
            }
            max_area = max(max_area, new_area);
        }
        printf("%.9lf\n", max_area * pi);
        
    }


	return 0;
}
