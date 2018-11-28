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


#define ri(X) scanf("%d",&X)
#define rii(X,Y) scanf("%d %d",&X,&Y)
#define rf(X) scanf("%lf",&X)
#define rff(X,Y) scanf("%lf %lf",&X,&Y)
#define mp(X,Y) make_pair(X,Y)
#define pii pair<int,int>
#define FOR(i,j) for(int i=0;i<j;i++)
#define FORC(i,j,c) for(int i=0;i<j;i+=c)

using namespace std;

    
int T;
long long N;
long long f[20];

void calc(){
    f[0] = 1;
    for(int i = 1; i< 19; i++) {
        f[i] = f[i-1] * 10LL;
    }
}

bool is_tidy(long long n){
    long long last_dig = 10;
    FOR(i,19){
        long long tmp = n;
        tmp -= tmp%f[i];
        tmp /= f[i];
        long long d = tmp%10LL;
        if (d > last_dig) return false;
        last_dig = d;
    }
    return true;
}

long long last_tidy(){
    long long best = -1LL;
    if (is_tidy(N)) return N;

    FOR(i,19){
        long long tmp = N; 
        tmp -= tmp%f[i];
        tmp /= f[i];
        tmp--;
        tmp *= f[i];
        tmp += f[i]-1;
        if(tmp <= N && is_tidy(tmp) && best < tmp) best = tmp;
    }

    return best;
}

int main(){
    calc();
    cin >> T;
    FOR(i,T){
       cin >> N; 
       cout << "Case #" << i+1 << ": " << last_tidy() << endl;
    }

	return 0;
}
