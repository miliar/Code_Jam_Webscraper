#include<bits/stdc++.h>
#define needforspeed ios::sync_with_stdio(0);cin.tie(0);
#define scan(x) do{while((x=getchar())<'0'); for(x-='0'; '0'<=(_=getchar()); x=(x<<3)+(x<<1)+_-'0');}while(0)
char _;
#define endl '\n'
#define pb push_back
#define mp make_pair
#define mp3(a,b,c) make_pair(a,make_pair(b,c))
#define mp4(a,b,c,d) make_pair(make_pair(a,b),make_pair(c,d))
#define trace1(a) cout << (a) << endl;
#define trace2(a,b) cout << (a)  << " " << (b) << endl;
#define trace3(a,b,c) cout << (a)  << " " << (b) << " " << (c) << endl;
#define trace4(a,b,c,d) cout << (a)  << " " << (b) << " " << (c) <<  " " << (d) << endl;
#define trace5(a,b,c,d,e) cout << (a)  << " " << (b) << " " << (c) <<  " " << (d) <<  " " << (e) << endl;
#define ms(a,b) memset( (a), (b), sizeof(a))
#define all(x) (x).begin(),(x).end()
#define len(x) (int)(x).size()
#define xx first
#define yy second
#define ll long long
#define pii pair<int,int>
#define pll pair<ll,ll>
#define MAXN (int)1e3+5
#define inf 0x3f3f3f3f
#define nullptr 0
#define db 0
using namespace std;

int T,N,K,D;
double hours[MAXN];

int main(){
    cin >> T;
    for(int t = 1;t <= T;t++){
        cin >> D >> N;
        vector< pair<int,int> >horses;
        for(int i = 0;i < N;i++){
            int k,s;
            cin >> k >> s;
            horses.pb(mp(k, s));
        }
        sort(all(horses));
        for(int i = N-1;i >= 0;i--){
            hours[i] = (double)(D-horses[i].xx)/horses[i].yy;
        }
        for(int i = N-2;i >=0;i--){
            // merge horses times to finish
            if(hours[i] < hours[i+1]){
                hours[i] = hours[i+1];
            }
        }
        double ans = D/hours[0];
        cout << "Case #" << t << ": ";
        printf("%.6lf\n", ans);
    }
    return 0;
}
