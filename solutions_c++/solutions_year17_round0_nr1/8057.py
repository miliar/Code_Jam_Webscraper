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

#define MAXN 10100

#define cin in
#define cout out

typedef pair<int,int> ii;
typedef vector<int> vi;
typedef vector<ii> vii;


vi fcount;
map <string,bool> vis;

bool check(string s){
    for(int i = 0; i < s.size(); i++){
        if(s[i] != '+') return false;
    }
    return true;
}

bool should(string s, int i, int k){
    //if(k == 2) return true;
    for(int j = i; j < i+k; j++){
        if(s[j] == s[j+1]) return true;
    }
    if(i > 0 && i+k+1 < s.size()){
        return s[i] != s[i-1] || s[i+k] != s[i+k+1];
    }
    else if(i == 0 && i+k+1 < s.size()){
        return s[i+k] != s[i+k+1];
    }
    return false;

}

string flip(string s, int i, int k){
    for(int j = i; j < i + k; j++){
        if(s[j] == '-') s[j] = '+';
        else s[j] = '-';
        fcount[j]++;
    }
    return s;
}

ii pm(string s, int i, int k){
    int sma = 0;
    int sme = 0;
    for(int j = i; j < i+k; j++){
        if(s[j] == '+') sma++;
        else sme++;
    }
    return mp(sma,sme);
}


int main(){
    ifstream in;
    ofstream out;
    in.open("input.in");
    out.open("out.txt");

    string s,aux;


    int t,k;
    cin >> t;
    int cs = 1;

    while(cs <= t){
        fcount.clear();
        vis.clear();
        int flips = 0;
        bool possible = true;
        cin >> s;

        aux = s;
        cin >> k;
        //cout << s <<" " << k << endl;
        fcount.insert(fcount.end(),s.size(),0);
        //while(!check(s) && possible){
            int bF = 0;
            int bP = 0;
            int bM = 0;
            for(int i = 0; i <= s.size() - k; i++){
                /*int l = should(s,i,k);
                cout << l << ">" << i << endl;
                if(should(s,i,k)){
                    int m = pm(s,i,k).se;
                    if(m > bM){
                        bF = i;
                        bM = m;
                    }
                    else if(m == bM && fcount[i] < fcount[bF]){
                        bF = i;
                        bM = m;
                    }
                    cout << m << "MMM" << endl;
                }
                */
                if(s[i] == '-'){
                    flips++;
                    s = flip(s,i,k);
                }
                //cout << s << "A" << endl;
            }
            //cout << bF << "<>" << k << endl;
            //s = flip(s,bF,k);
            //cout << s << "A" << endl;
            //if(vis[s]){
            if(!check(s)){
                possible = false;
            }/*
            else{
                flips++;
                vis[s] = true;
            }*/
        //}

        if(possible) cout << "Case #" << cs++ << ": " << flips << endl;
        else cout << "Case #" << cs++ << ": IMPOSSIBLE" << endl;
    }

    in.close();
    out.close();
    return 0;

}
