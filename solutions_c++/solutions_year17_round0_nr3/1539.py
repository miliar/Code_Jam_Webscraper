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
long long N, K;
int main(){
    cin >> T;
    FOR(i,T){
        cout <<"Case #" << i+1 <<": ";
        cin >> N >> K;
        long long h = 0;
        while((1LL << (h+1)) - 1 < K ) h++;
        long long tmp = N;
        long long th = h;
        long long get = K - (1LL<<h) + 1;
        while(th){
            tmp>>=1;
            th--;
        }
        long long t1 =tmp * (1LL<<h) + ((1LL<< h) -1); 
        long long t2 =((1LL<<(h+1LL)) - 1) ; 
        if(t1 > t2 ) tmp--;
        
        t1 =tmp * (1LL<<h) + ((1LL<< h) -1); 
        long long gr = N - t1;
        if( gr >= get ){
            cout << (tmp+1)/2 << " " << tmp/2 << endl;
        } else cout << tmp/2 << " " << (tmp-1)/2 << endl;
    }

	return 0;
}
