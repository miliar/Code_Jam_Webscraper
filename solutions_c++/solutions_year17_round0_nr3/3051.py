#include <bits/stdc++.h>
using namespace std;
struct Interval {
    long long left, right, length;
    Interval() {
    }
    Interval(long long left,long long right,long long length) {
        this -> left = left;
        this -> right = right;
        this -> length = length;
    }
} interval;
bool cmp(Interval a,Interval b){
    if (a.length > b.length)return !true;
    if (a.length < b.length)return !false;
    return !a.left<=b.left;
}
int T;
long long N,K,l,r,m,len,freq,ans,sum=1;
map<long long int,long long int> stalls;
map<long long, long long>::iterator it;
int main()
{
    freopen("bath3.in","r",stdin);
    freopen("bath3.out","w",stdout);
    scanf("%i",&T);
    for (int i=0;i<T;i++) {
        scanf("%lld%lld",&N,&K);
        stalls.clear();
        stalls[N]=1;
        sum=1;
        while (1)
        {
            it=stalls.end();
            it--;
            len=it->first;
            freq=it->second;
            if (sum<=K && K<sum+freq) {
                ans = len-1;
                break;
            }
            sum+=freq;
            if (len==2) {
                stalls[1]+=freq;
            } else if (len > 2) {
                len--;
                stalls[len/2]+=freq;
                stalls[len-len/2]+=freq;
                len++;
            }
            stalls.erase(len);
        }
        //printf("%lld %lld %lld\n",l,r,m);
        printf("Case #%i: %lld %lld\n",i+1,ans-ans/2,ans/2);
    }
}
