#include <bits/stdc++.h>
using namespace std;
#define ll long long
#define pii pair<int,int>
#define pll pair<ll,ll>
#define mp make_pair
#define ff first
#define ss second
#define pb push_back
#define pf pop_front
#define IOS ios::sync_with_stdio(false)
string s;
int k , t , a[1005];
int main(){

    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    cin >> t;
    for(int test = 1 ; test <= t ; test++){
        cin >> s >> k;
        memset(a,0,sizeof(a));
        for(int i = 0 ; i < s.size() ; i++){
            if(s[i]=='+')a[i+1]=1;
        }
        int cnt = 0;
        int l = 1;
        while(l<=s.size()-k+1){
            if(a[l]){
                l++;
            }
            else{
                for(int i = l ; i <= l + k - 1 && i <= s.size(); i++){
                    a[i]^=1;
                }
                cnt++;
                l++;
            }
        }
        bool check = true;
        for(int i = 1 ; i <= s.size() ; i++){
            if(a[i])continue;
            else{
                check = false;
            }
        }
        if(!check){
            cout << "Case #" << test << ": IMPOSSIBLE" << endl; 
        }
        else{
            cout << "Case #" << test << ": " << cnt << endl;
        }
    }
    return 0;
}