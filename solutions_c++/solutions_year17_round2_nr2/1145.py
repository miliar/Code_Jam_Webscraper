#include <bits/stdc++.h>
#define prev fjioweajiof
#define x1 fjweoifakewop
#define y1 zfewfjwieofajoi
#define ld long double
#define ll long long
#define int long long
using namespace std;

const int nmax = 100010;
const int inf = 100000000;

int t, n, r, o, y, g, b, v;
string vs, ans;
bool stop = 0;
map< vector<int> , int> M;
void dfs(char letter, int len, int r, int g, int b){
    if (r<0 || g<0 || b<0) return;
    //vector<int> svv;
    //svv.push_back(r);
    //svv.push_back(g);
    //svv.push_back(b);
   // if (M.count(svv)) return;
  //  M[svv]++;

    //cout << len << endl;
    vs.push_back(letter);
    cout << vs << " --> " << r << endl;
    if (vs.size()==n) {
        if (vs[n-1]!=vs[0]){
            if (ans=="") ans = vs;
            stop=1;
        }
        return;
    }
    if (letter=='R'){
        //dfs('O', len+1, r, o-1, y, g, b, v);
        //dfs('Y', len+1, r, o, y-1, g, b);
        dfs('G', len+1, r, g-1, b);
        dfs('B', len+1, r, g, b-1);
        //dfs('V', len+1, r, o, y, g, b, v-1);
    } else
    if (letter=='G'){
        dfs('R', len+1, r-1,g, b);
        //dfs('O', len+1, r, o-1, y, g, b);
        //dfs('Y', len+1, r, o, y-1, g, b, v);
        //dfs('B', len+1, r, o, y, g, b-1, v);
    } else
    if (letter=='B'){
        dfs('R', len+1, r-1, g, b);
        //dfs('O', len+1, r, g, b);
        //dfs('Y', len+1, r,  g, b);
        //dfs('G', len+1, r, o, y, g-1, b, v);
        //dfs('V', len+1, r, o, y, g, b, v-1);
    }

    vs.erase(vs.begin()+vs.size()-1);
}

main(){
freopen("input.txt","r",stdin);
//freopen("output.txt","w",stdout);

cin >> t;
int sv = t;
while (t--){
    cin >> n >> r >> o >> y >> g >> b >> v;
M.clear();
    vector<string> ans2;
    ans2.clear();
    stop=0;
    ans="";
    vs.clear();
    dfs('R', 1, r-1, g, b);
    ans2.push_back(ans);



    stop=0;
    ans="";

    vs.clear();
    M.clear();
    dfs('G', 1, r, g-1, b);
    ans2.push_back(ans);


    stop=0;
    ans="";

    vs.clear();
    M.clear();
    dfs('B', 1, r, g, b-1);
    ans2.push_back(ans);

    stop=0;
    ans="";


    sort(ans2.begin(), ans2.end());
    ans = ans2[ans2.size()-1];

    cout << "Case #" << sv - t << ": " << (ans=="" ? "IMPOSSIBLE" : ans) << endl;

    //break;
}



return 0;
}
