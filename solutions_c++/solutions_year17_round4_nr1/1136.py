//satyaki3794
#include <bits/stdc++.h>
#define ff first
#define ss second
#define pb push_back
#define MOD (1000000007LL)
#define LEFT(n) (2*(n))
#define RIGHT(n) (2*(n)+1)
 
using namespace std;
typedef long long ll;
typedef pair<int, int> ii;
typedef pair<int, ii> iii;

ll pwr(ll base, ll p, ll mod = MOD){
ll ans = 1;while(p){if(p&1)ans=(ans*base)%mod;base=(base*base)%mod;p/=2;}return ans;
}
 

ll gcd(ll a, ll b){
    if(b == 0)  return a;
    return gcd(b, a%b);
}


int cnt[7], arr[100005];

int main(){

    ios_base::sync_with_stdio(0);
    cin.tie(0);

    freopen("A-large.in", "r", stdin);
    freopen("output.txt", "w", stdout);

    int t, x = 1;
    cin>>t;
// t=1;
    while(t--){

        int n, p;
        cin>>n>>p;

        memset(cnt, 0, sizeof(cnt));
        for(int i=0;i<n;i++){
            int a;
            cin>>a;
            cnt[a%p]++;
        }

        if(p == 1){
            cout<<"Case #"<<x++<<": "<<n<<endl;
            continue;
        }
        if(p == 2){
            cout<<"Case #"<<x++<<": "<<cnt[0]+((cnt[1]+1)/2)<<endl;
            continue;
        }
        if(p == 3){
            int ans = cnt[0];
            int temp = min(cnt[1], cnt[2]);
            cnt[1] -= temp; cnt[2] -= temp;
            ans += temp;
            ans += ((cnt[1]+2)/3) + ((cnt[2]+2)/3);
            cout<<"Case #"<<x++<<": "<<ans<<endl;
            continue;
        }

        int ans = cnt[0] + cnt[2]/2;
        cnt[2] %= 2;
        int temp = min(cnt[1], cnt[3]);
        cnt[1] -= temp; cnt[3] -= temp; ans += temp;

        if(cnt[2] == 0){
            ans += (cnt[1]+3)/4 + (cnt[3]+3)/4;
            cout<<"Case #"<<x++<<": "<<ans<<endl;
        }
        else{

            int val = 1;
            if(cnt[1] > 0){
                val = 1;
            }
            else{
                val = 3;
            }

            int sz = cnt[1]+cnt[3]+1;
            int zzz = 0;
            for(int pos=1;pos<=sz;pos++){
                for(int i=1;i<=sz;i++)
                    arr[i] = val;
                arr[pos] = 2;
                int yolo = 0;
                for(int i=1;i<=sz;i++){
                    arr[i] += arr[i-1];
                    arr[i] %= p;
                    yolo += (arr[i-1] == 0);
                }
// cout<<pos<<" "<<sz<<" gives "<<yolo<<" "<<cnt[3]<<endl;
                zzz = max(zzz, yolo);
            }

            ans += zzz;
            cout<<"Case #"<<x++<<": "<<ans<<endl;
        }
    }

    return 0;
}










