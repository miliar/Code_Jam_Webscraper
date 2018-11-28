
#pragma comment(linker,"/STACK:16777216")
#pragma  warning ( disable: 4786)
#include<iostream>
#include<cstring>
#include<cstdio>
#include<vector>
#include<map>
#include<set>
#include<string>
#include<cmath>
#include<cstdlib>
#include<cctype>
#include<algorithm>
#include<queue>
#include<sstream>
#include<stack>
#include<list>
#include <bitset>
#include<iomanip>
#include <fstream>
#include<ctime>

using namespace std;

#define max(x,y) ((x)>(y)?(x):(y))
#define min(x,y) ((x)<(y)?(x):(y))

#define MX 1000000

#define forl(i,a,b) for ( i = a; i < b; i++)
#define fore(i,a,b) for ( i = a; i <= b; i++)
#define forrev(i,a,b) for ( i = a; i >= b; i--)
#define pb push_back
typedef long long  LL;
#define in(a,b,c) ((a) <= (b) && (b) <= (c))
#define ms(a,b) memset((a),(b),sizeof(a))

#define all(v) (v).begin(),(v).end()
#define pb push_back
#define ull unsigned long long int
typedef vector<int> vi;
typedef pair<int,int> pii;
typedef vector<pii> vpii;

string to_string(long long x) { stringstream ss; ss << x; return ss.str(); }
long long to_int(const string &s) { stringstream ss; ss << s; long long x; ss >> x; return x; }

#define MAX 100005

bool tidy(ull a){
    int prev = a%10;
    a = a/10;
    while(a){
        int t = a%10;
        if(t>prev)
            return false;
        a = a/10;
        prev = t;
    }
    return true;
}
ull general(string s, int digits){
    int pos=-1;
    ull ans2=0;
    int i;
    forl(i,0,digits-1){
        if(s[i]>s[i+1]){
            pos= i;
            break;
        }
    }
    int pos2=pos;
    while(pos2 >= 0 && s[pos2] == s[pos])
    {
        pos2--;
    }
    if(pos2==-1)
        pos2=0;
    else
        pos2++;
    forl(i,0,pos2){
        ans2 = ans2*10 + (s[i]-'0');
    }
    for(i=pos2;i<=pos;i++){
        ans2 = ans2*10 + ((s[i]-'0')-1);
    }

    forl(i,pos+1,digits){
        ans2 = ans2*10 + 9;
    }
    return ans2;
}
int main(void)
{
    freopen("B-small-attempt2.in", "r", stdin);
    freopen("2.txt", "w", stdout);
    int t;
    cin >> t;
    ull N;
    ull ans;
    int i,j,k;
    getchar();
    int ca=1;
    ull one=1;
    while(t--){
        cin >> N;
        ull ind;
        ull ans1,ans2;
        ans2=0;
        /*for(ind=N;ind>=1;ind--){
            if(tidy(ind)){
                cout << ind << endl;
                ans1 = ind;
                break;
            }
        }*/
        cout <<"Case #" << ca++ << ": ";
        if(tidy(N)){
            cout << N << endl;
            ans2=N;
            /*if(ans1 != ans2){
                cout << "mismatch\n";
            }
            continue;*/
            continue;
        }
        int msd;
        int digits=0;
        ull a = N;
        string s = "";
        vector<int> v;
        while(a){
            msd = a%10;
            a /= 10;
            s = s + char('0'+msd);
            v.pb(msd);
            digits++;
        }
        sort(all(v));
        vector<int> v1;
        v1.pb(v[0]);
        forl(i,1,v.size()){
            if(v[i] != v[i-1]){
                v1.pb(v[i]);
            }
        }
        v = v1;
        ull ans=0;
        if(v.size() == 2){
           ull tmp=0;
            if(msd==1 && v[0] == 0){
                forl(i,0,digits-1){
                    tmp = tmp*10 + 9;
                }
            }
            ans = tmp;
            tmp = 0;
            if(msd > 1){
                tmp = tmp*10 + (msd-1);
                forl(i,0,digits-1){
                    tmp = tmp*10 + 9;
                }
                ans = max(ans,tmp);
            }
        }

        reverse(s.begin(),s.end());
        ans = max(ans, general(s,digits));
        cout << ans;
        cout << endl;

    }
    return 0;
}
