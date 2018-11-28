#include<bits/stdc++.h>

using namespace std;

#define sd(a) scanf("%d", &a)
#define sd2(a,b) scanf("%d %d", &a, &b)
#define sd3(a,b,c) scanf("%d %d %d", &a, &b, &c)
#define sd4(a,b,c,d) scanf("%d %d %d %d", &a, &b, &c, &d)
#define sll(a) scanf("%lld", &a)
#define sll2(a,b) scanf("%lld %lld", &a, &b)
#define sll3(a,b,c) scanf("%lld %lld %lld", &a, &b, &c)
#define sll4(a,b,c,d) scanf("%lld %lld %lld %lld", &a, &b, &c, &d)
#define sc(a) scanf("%c", &a)
#define slf(a) scanf("%lf", &a)
#define slf2(a,b) scanf("%lf %lf", &a, &b)
#define slf3(a,b,c) scanf("%lf %lf %lf", &a, &b, &c)
#define slf4(a,b,c,d) scanf("%lf %lf %lf %lf", &a, &b, &c, &d)

#define FORN(i,n) for(int i = 0; i < n; i++)
#define all(v) v.begin(), v.end()
#define in(a,b) ( (b).find(a) != (b).end())
#define pb push_back
#define mp make_pair
#define fi first
#define se second

#define BUFF ios::sync_with_stdio(false);

#define MAXR 30
#define MAXC 30

#define cin in
#define cout out

typedef pair<int,int> ii;
typedef vector<int> vi;
typedef vector<ii> vii;

vii horses;

int main(){
    ifstream in;
    ofstream out;
    in.open("A-large.in");
    out.open("out.txt");


    int tst;
    cin >> tst;
    int cs = 1;

    while(cs <= tst){
        horses.clear();
        double vel, d, t;
        int n;
        cin >> d >> n;
        double h,v, hi, vi;
        for(int i = 0; i < n; i++){
            cin >> hi >> vi;
            horses.pb(mp(hi,vi));
        }
        t = 0;
        for(int i = 0; i < horses.size(); i++){
            hi = horses[i].fi;
            vi = horses[i].se;

            t = max(t,(d - hi)/(vi));

        }

        vel = (d)/t;
        cout << fixed;
        cout << "Case #" << cs++ << ": "<< setprecision(7) << vel << endl;

    }

    in.close();
    out.close();
    return 0;

}
