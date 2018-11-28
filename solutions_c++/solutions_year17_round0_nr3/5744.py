#include <bits/stdc++.h>
#define int long long
using namespace std;

const int N = 2000;
int t,test,n,k,i,a[N],pref[N],suff[N],last,pos,mn,mx,j;

//int
 main(){

    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);

    cin >> t;
    for(test = 1;test<=t;++test){
        cin >> n >> k;
        cout << "Case #"<<test<<": ";

        for(i = 1; i <= n; ++i)a[i] = 0;
        a[0] = a[n+1] = 1;

        for(i = 1; i <= k; ++i){
                last = 0;
            for(j = 0; j <= n + 1; ++j)
                if(a[j]) last = j; else
                    pref[j] = j - last;
            last = n + 1;
            for(j = n; j > 0; --j)
                if(a[j]) last = j; else suff[j] = last - j;

        pos = 0;
        mn = mx = 0;
        for(j = 1; j <= n; ++j)
        if(!a[j]){
            if(pos == 0 || (min(pref[j],suff[j]) > mn || (min(pref[j],suff[j]) == mn && max(pref[j],suff[j]) > mx))){
            mn = min(pref[j],suff[j]);
            mx = max(pref[j],suff[j]);
            pos = j;
        }
       }
        a[pos] = i;

    }
    cout << mx - 1<< ' ' << mn - 1<< '\n';
}
 }
