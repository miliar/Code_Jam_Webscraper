#include <bits/stdc++.h>
#define endl '\n'
#define double long double

using namespace std;

const double PI = 2*acos(0.0);
const int N = 1024;
const double INF = (1e18) + 7;

int tests,current_case;
int n,k;
pair < int, int > a[N];
bool used[N][N];
double state[N][N];
double ans;

void message(int current_case) {
    //cerr<<"Case "<<current_case<<" solved!"<<endl;
    fprintf(stderr, "Case %d solved!\n", current_case);
}

double recurse(int pos, int rem) {
    if(rem==0) return 0.0;
    if(pos>n) return -INF;
    if(used[pos][rem]) return state[pos][rem];
    double ans=recurse(pos+1,rem);
    ans=max(ans,recurse(pos+1,rem-1)+2.0*PI*a[pos].first*a[pos].second);
    used[pos][rem]=true;
    state[pos][rem]=ans;
    return ans;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int i;

    tests=1;
    //scanf("%d", &tests);
    cin>>tests;
    for(current_case=1;current_case<=tests;current_case++) {
        cin>>n>>k;
        for(i=1;i<=n;i++) {
            cin>>a[i].first>>a[i].second;
        }
        sort(a+1,a+1+n);
        reverse(a+1,a+1+n);
        memset(used,0,sizeof(used));
        ans=0;
        for(i=1;i<=n;i++) {
            ans=max(ans,recurse(i+1,k-1)+PI*a[i].first*a[i].first+2.0*PI*a[i].first*a[i].second);
        }
        cout<<"Case #"<<current_case<<": "<<setprecision(10)<<fixed<<ans<<endl;

        MESSAGE:
        message(current_case);
    }

    return 0;
}
