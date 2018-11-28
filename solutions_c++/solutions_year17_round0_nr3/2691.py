#include <bits/stdc++.h>
#define ll long long
#define ull unsigned ll

using namespace std;
#define MAXN 150001
#define files(x) freopen((x+string(".dat")).c_str(), "r", stdin); //freopen((x+string(".sol")).c_str(), "w", stdout);



#define MAXN 1000001
#define input_file(x) freopen((x+string(".txt")).c_str(), "r", stdin);
#define output_file(x) freopen((x+string(".txt")).c_str(), "w", stdout);


void get_ans(unsigned ll x){

    cout<<x/2<<" "<<(x-1)/2;

}
void solve(){
    unsigned ll n,k, p, np, pval, npval, _p, _np, cnt, v1, v2, v3;
    cin>>n>>k;
    if (k==1)
        return (void) (get_ans(n));
    p = 1-n%2; np =  n%2;
    cnt = 1;
    if (n%2==0){
        pval = n;
        npval = pval - 1;
    }
     else{
        npval = n;
        pval = n -1;
     }
    while (k>cnt){
        _p = 0; _np = 0;
        v1 = (npval - 1)/2;
        v2 = pval/2;
        v3 = pval/2 - 1;

        _p = 2 * (v1%2 == 0) * np * (v1>0) + (v2%2==0) * p * (v2>0)+ (v3%2==0) * p * (v3>0);
        _np = 2 * (v1%2 == 1) * np * (v1>0) + (v2%2==1) * p * (v2>0) + (v3%2==1) * p * (v3>0);
        p = _p;
        np = _np;
        if (v2%2==0){
            pval = v2;
            npval = v3;
        }
        else {
            pval = v3;
            npval = v2;
        }
        k-=cnt;
        cnt<<=1;

    }

    if (pval> npval){
        if (k > p)
            get_ans(npval);
        else get_ans(pval);
    } else{
        if (k > np)
            get_ans(pval);
        else get_ans(npval);

    }




}

main () {
    ios_base::sync_with_stdio(0);
    cin.tie(NULL);
    input_file("input");
    output_file("output");

    int t;
    cin>>t;
    for (int i=0;i<t;i++){

        cout<<"Case #"<<i+1<<": ";
        solve();
         cout<<endl;
    }



}
