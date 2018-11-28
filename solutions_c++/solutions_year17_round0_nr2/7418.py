#include <bits/stdc++.h>
using namespace std;

#define read() freopen("B-large.in","r",stdin)
#define INF ((1<<29)-1)
#define EPS (1e-9)
#define PI (2*acos(0.0))
#define ll long long
#define ull unsigned ll
#define SIZE ((ll)1e6)+10
#define testcase ll T;cin>>T;for(int t=1;t<=T;t++)
#define printcase() cout<<"Case "<<t<<":\n"
#define pb push_back
#define PAR_SIZE 1000000+10
#define BFS_GRID 1010
#define NL() cout << endl
#define FOR(itt,n) for(int itt=0;itt<n;++itt)
#define FOR1(itt,n) for(int itt=1;itt<=n;++itt)
#define MAX_PRIME 1000010



int main()
{
    #ifdef pinanzo
        read();
        freopen("output.txt","w",stdout);
    #endif // pinanzo
    //ios_base::sync_with_stdio(0);
    //cin.tie(NULL);
    //cout.tie(NULL);

    int T;
    double m, n, b;
    string s, temp, leftOfCursor, rightOfCursor, finalString;
    scanf("%d", &T);
    for(int t=1; t<=T; ++t){
        cin >> s;
        if(s!="0"){
            for(int i=s.size()-1; i>0; --i){
                //cout << s[i-1] << ' ' << s[i] << endl;
                if(s[i]<s[i-1]){
                    int j=i;
                    while(j<s.size()){
                        s[j]='9';
                        ++j;
                    }
                    if(s[i-1]!='0'){
                        s[i-1]--;
                        //cout << s[i-1] << " i - 1" << endl;
                    }
                    else{
                        j=i-1;
                        while(s[j]=='0'&&j>0){
                            s[j]='9';
                            --j;
                        }
                        s[j]--;
                    }
                }

            }
            int i=0;
            while(s[i]=='0'&&i<s.size())++i;
            cout << "Case #" << t << ": ";
            while(i<s.size()){
                cout << s[i];
                i++;
            }
            cout << endl;
        }
        else {
            cout << "Case #" << t << ": 0" << endl;
        }
    }


    return 0;
}

/// 13259
