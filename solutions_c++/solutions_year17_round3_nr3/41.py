#include <bits/stdc++.h>
#define endl '\n'
#define double long double

using namespace std;

const int N = 64;
const int ITERATIONS = 5000;

int tests,current_case;
int n,k;
double u,p[N];
double ans;

void message(int current_case) {
    //cerr<<"Case "<<current_case<<" solved!"<<endl;
    fprintf(stderr, "Case %d solved!\n", current_case);
}

bool check(double v) {
    double sum=0.0;
    int i;
    for(i=1;i<=n;i++) if(p[i]<v) sum+=v-p[i];
    return (sum<=u);
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int i;
    double left,right,middle;

    tests=1;
    //scanf("%d", &tests);
    cin>>tests;
    for(current_case=1;current_case<=tests;current_case++) {
        cin>>n>>k;
        cin>>u;
        for(i=1;i<=n;i++) {
            cin>>p[i];
        }
        left=0.0;
        right=1.01;
        for(i=1;i<=ITERATIONS;i++) {
            middle=(left+right)/2.0;
            if(check(middle)) left=middle;
            else right=middle;
        }
        ans=1.0;
        for(i=1;i<=n;i++) p[i]=max(p[i],right),ans*=p[i];
        cout<<"Case #"<<current_case<<": "<<setprecision(10)<<fixed<<ans<<endl;

        MESSAGE:
        message(current_case);
    }

    return 0;
}
