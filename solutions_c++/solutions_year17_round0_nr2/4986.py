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
ll t , n;
string s;
int a[20];
int main(){

	freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    cin >> t;
	for(int test = 1 ; test <= t ; test++){
        cin >> s;
        memset(a,0,sizeof(a));
        for(int i = 0 ; i <= s.size() ; i++){
            a[i+1] = s[i] - '0';
        }
        int l = 1 , r = 1;
        int pos = -1;
        for(int i = 1 ; i <= s.size() ; i++){
            if(a[i] > a[i-1]){
                l = i;
            }
            else if(a[i]==a[i-1]){
                continue;
            }
            else{
                pos = l;
                break;
            }
        }
        if(pos==-1){
            cout << "Case #" << test << ": ";
            for(int i = 1 ; i <= s.size() ; i++)cout << a[i];
            cout << endl;
            continue;
        }
        a[pos] = a[pos] - 1;
        for(int i = pos + 1 ; i <= s.size() ; i++)a[i] = 9;
        l = 1;
        while(a[l]==0)l++;
        cout << "Case #" << test << ": ";
        for(int i = l ; i <= s.size() ; i++)cout << a[i];
        cout << endl;

    }
    return 0;
}