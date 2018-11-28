#include <bits/stdc++.h>
using namespace std;
#define ll long long
#define ull unsigned long long
#define si(X) scanf("%d", &(X))
#define sll(X) scanf("%lld",&(X))
#define INFL 0x3f3f3f3f3f3f3f3fLL
const int mod = 1e9+7;
ll gcd(ll a,ll b){
	if(b==0)
	return a;return gcd(b,a%b);
}
ll expo(ll base,ll pow){
    ll ans = 1;
    while(pow!=0){
        if(pow&1==1){
            ans = ans*base;
            ans = ans%mod;
        }
        base *= base;base%=mod;
        pow/=2;
    }return ans;
}
ll inv(ll x){
    return expo(x,mod-2);
}

double pi = 3.141592653589793238462643;
double error = 0.0000001;
int dx[8] = {1 , 0 , -1 , 0 , 1 , -1 , -1 , 1};    // last 4 diagonal
int dy[8] = {0 , 1 , 0 , -1 , 1 , 1 , -1 , -1};
/* -------Template ends here-------- */

const int M = 100001;
vector<int> vec[10];
char ans[11111];
map<int , int> mp;
int val[10];
int temp[10];
int n;

void make_g(){
    vec[1].push_back(4);
    vec[4].push_back(1);

    vec[1].push_back(5);
    vec[5].push_back(1);

    vec[1].push_back(3);
    vec[3].push_back(1);

    vec[5].push_back(2);
    vec[2].push_back(5);

    vec[5].push_back(3);
    vec[3].push_back(5);

    vec[3].push_back(6);
    vec[6].push_back(3);

    mp[1] = 'R';
    mp[2] = 'Y';
    mp[3] = 'B';
    mp[4] = 'G';
    mp[5] = 'B';
    mp[6] = 'V';
}


void init(){
    for(int i = 1 ; i <= 6 ; i++){
        temp[i] = val[i];
    }
}



int main(){
    freopen("input.txt", "rt", stdin);
    freopen("output.txt", "wt", stdout);

    int T;
    si(T);
    make_g();

    for(int alp = 1 ; alp <= T ; alp++){


        //int n;
        si(n);

        vector<pair<int , int> > vv;
        printf("Case #%d: " , alp);

        int c = 0;
       // cout<<"here"<<endl;
        for(int i = 1 ; i <= 6 ; i++){
            si(val[i]);
            if(val[i] > n/2){
                c++;
            }
            if(i == 1 || i == 3 || i == 5)
            vv.push_back(make_pair(val[i] , i));
        }
        //ans.clear();
        if(c){
            cout<<"IMPOSSIBLE\n";
            continue;
        }

        int keep = 0;
        val[0] = val[1];
        val[1] = val[3];
        val[2] = val[5];

        int ind = 0 , ma = 0;

        for(int i = 0 ; i < 3 ; i++){
            if(val[i] > ma){
                ma = val[i];
                ind = i;
            }
        }

        for(int i = 1 ; i <= n ; i++){
            ans[i] = 'o';
        }

        keep = ind;
        int prev;

        for(int i = 1 ; i <= n ; i++){
            if(ans[i] == 'o'){

                if(i == 1){
                    ans[i] = mp[keep + 1];
                    val[keep]--;
                    prev = keep;
                    continue;
                }
                int ma = 0;
                keep = 0;
                for(int j = 0 ; j < 3 ; j++){
                    if(val[j] > 0 && j != prev &&(val[j] > ma || (val[j] == ma && j == ind))){
                        keep = j;
                        ma = val[j];
                    }
                }
                ans[i] = mp[keep + 1];
                val[keep]--;
                prev = keep;
            }
        }

        for(int i = 1 ; i<=n ; i++){
                cout<<ans[i];
            }


        cout<<"\n";



    }


}
