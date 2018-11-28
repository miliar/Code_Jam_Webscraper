#include <bits/stdc++.h>

using namespace std;
int r[10];
int dp[101][101][101][4];
int n , p ;
int solve(int one , int two , int three ,int last  ){
    if(!(one+two+three)) return 0;
    int &ret = dp[one][two][three][last];
    if(ret!=-1)return ret ;
    if(last == 0 ) ret = 1 ;
    else ret = 0 ;
    int add = 0 ;
    if(one) add = max(add , solve(one-1 , two , three, (last+1)%p));
    if(two) add = max(add , solve(one , two-1 , three, (last+2)%p));
    if(three) add = max(add , solve(one , two , three-1, (last+3)%p));

    ret += add;
    return ret;
}

int main()
{
    ifstream cin("A-large.in.txt");
    ofstream cout("a.txt");
    int t;
    cin >> t;
    for(int tc = 1 ;tc<= t ; tc++){
        cin >> n >> p ;
        memset(r,0 , sizeof r);
        for(int i =  0; i< n ; i++){
            int a ;
            cin >> a ;
            r[a%p]++;
        }
        memset(dp , -1 ,sizeof dp);
        int ans = r[0] ;
        ans += solve(r[1],r[2],r[3],0);
        cout << "Case #"<<tc << ": " <<ans<<endl;
    }
    return 0;
}
