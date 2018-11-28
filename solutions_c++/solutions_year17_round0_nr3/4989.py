#include <stdio.h>
#include <string.h>
#include <iostream>
#include <queue>

using namespace std;

/* Template Begins */

#define FOR(i,N) FORR(i, 0, N)
#define FORR(i,a,b) FOTR(i, a, b, 1)
#define FOTR(i,a,b,c) for(int i=(a);i<(b);i+=(c))
#define FOREACH(it, x) for(__typeof__((x).begin()) it=(x).begin();it!=(x).end();it++)
#define MEM(a,x) memset(a,x,sizeof(a))
#define BCHK(a,x) (((a)>>(x))&1)
#define BSET(a,x) ((a)|(1<<(x)))
#define BCLR(a,x) ((a)&(~(1<<(x))))
#define BTGL(a,x) ((a)^(1<<(x)))
#define FMT(...) (sprintf(CRTBUFF, __VA_ARGS__)?CRTBUFF:0)
#define read() freopen("input.txt","r",stdin)
#define write() freopen("output.txt","w",stdout)
#define cpp_io() {ios_base::sync_with_stdio(false);cin.tie(NULL);}
#define BUFFSIZE 30000
#define INF 1000000000
#define MOD 1000000007
#define MAX 2000000
#define pb push_back
#define mkpr make_pair
#define pii pair<int, int>
typedef long long ll;

char CRTBUFF[BUFFSIZE];

#define dbg(args...) {cout<<"-->";debugger::call(#args,args);cout<<"\n";}
struct debugger{
    static void call(const char* it){}
    template<typename T, typename ... aT>
    static void call(const char* it, T a, aT... rest){
        string b;
        for(;*it&&*it!=',';++it) if(*it!=' ')b+=*it;
        cout<<b<<"="<<a<<" ";
        call(++it, rest...);
    }
};

/* Template Ends */

struct Item{
    int idx, t;
    int x, y;
    int mn, mx, len;
    Item(){}
    Item(int t, int idx, int x, int y){
        this->idx=idx, this->t=t;
        this->x= x, this->y=y;
        mn=min(idx-x-1, y-idx-1), mx=max(idx-x-1, y-idx-1);
    }
    bool operator<(const Item& B) const{
        if(mn==B.mn)
            return mx<B.mx;
        return mn<B.mn;
    }
};

int D[MAX+10];
int V[MAX+10][2];

int main()
{
    read();
    write();
    cpp_io();
    int TC;
    cin >> TC;
    FORR(cs, 1, TC+1){
        MEM(D, 0);
        int N, K;
        cin >> N >> K;
        priority_queue<Item> pq;
        int ax, ay;
        FORR(i, 1, N+1) V[i][0]=0, V[i][1]=N+1;
        FORR(i, 1, N+1) pq.push(Item(0, i, V[i][0], V[i][1]));
        for(int i=0; i<K;){
            Item u=pq.top();
            pq.pop();
            while(D[u.idx]>u.t){
                pq.push(Item(D[u.idx], u.idx, V[u.idx][0], V[u.idx][1]));
                u=pq.top();
                pq.pop();
            }
            ax=u.mx, ay=u.mn;
            for(int k=u.x; k<=u.y; k++){
                D[k]=i+1;
                V[k][k<u.idx]=u.idx;
            }
//            for(int k=u.x; k<u.idx; k++){
//                V[k][1]=u.idx;
//            }
//            for(int k=u.idx; k<u.y; k++){
//                V[k][0]=u.idx;
//            }
            i++;
        }
        cout << FMT("Case #%d: %d %d\n", cs, ax, ay);
    }

    return 0;
}
