#include <bits/stdc++.h>
using namespace std;

#define pb push_back
#define nl printf("\n")
#define ll long long int
#define pii pair<int, int>
#define vii vector< pair<int, int> >
#define print_in_file() freopen("out.txt", "w", stdout)
#define mp make_pair
#define all(v) (v).begin(), (v).end()
#define print_vector(v) for(int i=0; i<(v).size(); i++) cout<<(v)[i]<<' '; cout<<endl
#define print_arr(a, i) for(int j=0; j<(i); j++) cout<<(a)[j]<<' '; cout<<endl
#define lcm(a, b) ((a)*(b))/gcd((a), (b))
#define SWAP(a, b) (a) ^= (b); (b) ^= (a); (a) ^= (b)
#define abs(a,b) ((a>b) ? a-b : b-a)
#define ul unsigned long long int

int main ()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int cs; cin>>cs;
    for(int t=1; t<=cs; t++) {
        set<pair<int, pair<int, int> > > s;
        int n, k;
        cin>>n>>k;
        printf("Case #%d: ", t);
        //dfjhksuyuyuyuyuyuyuyuyuyuyuyuyuygbikzlb
        s.insert({-n, {0, n+1}});
        //sdjkgbyuisegklbfyuseziigbd
        for(int i=1; i<k; i++) {
            auto top=*(s.begin());
            //sdjbgaibegwydvbkdvbgsdvgsdbv
            s.erase(s.begin());
            int left=top.second.first;
            //sbuysevfgievbgyevggvbyg
            int right=top.second.second;
            //sdjkbgsklrvgyrgbvgksf
            int mid=(left+right)/2;
            s.insert({-(mid-left-1), {left, mid}});
            s.insert({-(right-mid-1), {mid, right}});
        }
        auto top=*(s.begin());
        //dubirgbfdljvbhdffdh
        int left=top.second.first;
        int right=top.second.second;
        int mid=(left+right)/2;
        int l=mid-left-1;
        int r=right-mid-1;
        printf("%d %d\n", max(l, r), min(l, r));
    }
    return 0;
}
