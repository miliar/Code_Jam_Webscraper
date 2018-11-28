#include<bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef pair<int, int> pi;

#define F first
#define S second
#define PB push_back
#define MP make_pair
#define REP(i,a,b) for(int i = a; i <= b ;i++)

int main()
{
    //freopen("A_small_in.txt","r",stdin);
    //freopen("A_small_out.txt","w",stdout);
    int n,k,l = 0;
    cin >> n;
    while(n--){
            int ans = 0;
        string s;
        cin >> s >> k;
        int sr = s.size();
        string g;
        cout << "Case #" << ++l << ": ";
        for(int i = 0 ; i < sr ; i++)
             g.push_back('+');
        if(s == g)
            cout << 0 << endl;
        else{
            for(int i = 0; i < sr and s != g ;i++){
                    int p = 0;
                if(s[i] == '-'){
                        if( sr - i < k ) break;
                    for(int j = i; p < k and j < sr;j++,p++){
                         if(s[j] == '-') s[j] = '+' ;
                         else s[j] = '-';
                    }
                    ans++;
                }
            }
           (s != g)? cout << "IMPOSSIBLE" << endl : cout << ans << endl;
        }

    }
    return 0;
}
