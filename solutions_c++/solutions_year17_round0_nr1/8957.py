
/*  Chandan Kumar  */
/*  _   */

#include <bits/stdc++.h>
using namespace std;

#define X first
#define Y second
#define inf 1000000
#define mp make_pair
#define pb push_back
#define tc(t) int t; cin >> t; while(t--)
#define input freopen("input.txt", "r", stdin)
#define output freopen("output.txt", "w", stdout)
#define fast_io ios_base::sync_with_stdio(false);cin.tie(NULL)

typedef long long int ll;
typedef pair < ll, int > lip;
typedef pair < int, int > iip;
typedef set < int > :: iterator sit;
typedef vector < int > :: iterator vit;
typedef vector < iip > :: iterator viit;
typedef map < int, int > :: iterator mit;

const int MOD = 1e9+7;
const int MAX = 1e6+7;

char rev(char s){
    if(s == '-')
        return '+';
    else
        return '-';
}

int main()
{
    fast_io;
//    input;
//    output;
    int t, tc;
    cin >> tc;
    for(t=1; t<=tc; t++){
        string str;
        int k, i, j, count=0;
        bool flag = 1;
        cin >> str >> k;
        for(i=0; i<str.length(); i++){
            if(str[i] == '-'){
                if(i > str.length()-k){
                    flag = 0;
                    break;
                }
                count++;
                for(j=0; j<k; j++)
                    str[i+j] = rev(str[i+j]);
            }
        }
        if(flag)
            cout << "Case #" << t << ": " << count << endl;
        else
            cout << "Case #" << t << ": IMPOSSIBLE" << endl;
    }
    return 0;
}
