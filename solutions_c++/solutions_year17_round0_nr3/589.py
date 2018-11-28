#include<bits/stdc++.h>
#define P(x,y) make_pair(x,y)
using namespace std;
typedef long long ll;
long long T , Tn , arr[100];
ll freq[100][100][2];
struct state{
    long long prefix , one , off;
    state(){}
    state(long long prefix , long long one , long long off):prefix(prefix) , one(one) , off(off){}
};
set < state > S;
bool operator < (const state&A , const state&B){
    if(A.prefix + A.one < B.prefix + B.one) return A.prefix + A.one < B.prefix + B.one;
    if(A.prefix != B.prefix) return A.prefix < B.prefix;
    return A.off > B.off;
}
void relax(long long prefix , long long ones , long long off , ll JD){
    if(freq[prefix][ones][off] == 0) S.insert(state(prefix , ones , off));
    freq[prefix][ones][off] += JD;
}
void fetch(long long L , long long O , long long flag){
    long long ret = 0;
    for(long long j = 1 ; j < L ; j++)
        ret *= 2 , ret += arr[j];
    ret *= 2;
    if(!flag) ret += arr[L];
    while(O--) ret *= 2 , ++ret;
    if(ret % 2) cout<<ret/2<<' '<<ret/2<<endl;
    else cout<<ret/2<<' '<<ret/2-1<<endl;
}
//set < state > S;
int main(){
   // freopen("in.in","r",stdin);
 //   freopen("codejam.out","w",stdout);
    cin>>T;
    while(T--){
        ll N , K;
        cin>>N>>K;
        printf("Case #%lld: ",++Tn);
        long long tt = 0;
        while(N > 0){
            arr[++tt] = N % 2;
            N /= 2;
        }
        memset(freq , 0 , sizeof(freq));
        N = tt;
        reverse(arr+1 , arr+1+N);
        freq[N][0][0] = 1;
        S.clear();
        S.insert(state(N , 0 , 0));
        while(!S.empty()){
            auto cur = *--S.end(); S.erase(--S.end());
            long long prefix = cur.prefix , off = cur.off , ones = cur.one;
            ll jd = freq[prefix][ones][off];
      //      cout<<prefix<<' '<<off<<' '<<ones<<' '<<jd<<endl;

            if(jd >= K){
                fetch(prefix , ones , off);
                break;
            }
            K -= jd;
            if(ones){
                relax(prefix , ones - 1 , off , jd * 2);
                continue;
            }
            if(prefix == 1) continue;
            if(arr[prefix] == 1 && !off){
                relax(prefix - 1 , 0 , 0 , jd * 2);
                continue;
            }
            relax(prefix - 1 , 0 , 0 , jd);
            long long nones = 0;
            long long nprefix = prefix - 1;
            while(arr[nprefix] == 0) nprefix-- , nones++;
            relax(nprefix , nones , 1 , jd);
        }
    }
}

