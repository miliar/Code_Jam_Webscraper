#include <bits/stdc++.h>
using namespace std;
#define int long long
#define all(x) ((x).begin(), (x).end())
#define pb push_back

typedef pair<int, int> ii;
typedef long double LD;

void solve(int tn){ cout << "Case #" << tn << ": ";
   int n;
   cin >> n;
    int R, O, Y, G, B, V;
   cin >> R >> O >> Y >> G >> B >> V;

   if(R+Y+G+V == 0){
       if(O != B) cout << "IMPOSSIBLE";
       else for(int i = 0; i < O; i++) cout << "OB";
       cout << endl;
       return;
   }

   if(O+Y+B+V == 0){
       if(G != R) cout << "IMPOSSIBLE";
       else for(int i = 0; i < G; i++) cout << "GR";
       cout << endl;
       return;
   }

   if(R+O+G+B == 0){
       if(V != Y) cout << "IMPOSSIBLE";
       else for(int i = 0; i < V; i++) cout << "VY";
       cout << endl;
       return;
   }

   map<char, vector<string>> chains;

   if(O > 0){
       if(B < O+1){
           cout << "IMPOSSIBLE" << endl;
           return;
       }

       B -= O+1;
       string acc = "B";
       for(int i = 0; i < O; i++) acc += "OB";
       chains['B'].pb(acc);
   }
    for(int i = 0; i < B; i++) chains['B'].pb(string("B"));

   if(V > 0){
       if(Y < V+1){
           cout << "IMPOSSIBLE" << endl;
           return ;
       }

       Y -= V+1;
       string acc = "Y";
       for(int i = 0; i < V; i++) acc += "VY";
       chains['Y'].pb(acc);
   }
   for(int i = 0; i < Y; i++) chains['Y'].pb(string("Y"));

   if(G > 0){
       if(R < G+1){
           cout << "IMPOSSIBLE" << endl;
           return;
       }

       R -= G+1;
       string acc = "R";
       for(int i = 0; i < G; i++) acc += "GR";
       chains['R'].pb(acc);
   }

    for(int i = 0; i < R; i++) chains['R'].pb(string("R"));

    vector<pair<int, char>> v;
    v.pb({chains['R'].size(), 'R'});
    v.pb({chains['Y'].size(), 'Y'});
    v.pb({chains['B'].size(), 'B'});
    sort(v.begin(), v.end());

    string res;
    while(v[0].first > 0){
        res += v[0].second;
        res += v[1].second;
        res += v[2].second;
        v[0].first--;
        v[1].first--;
        v[2].first--;
    }

    while(v[1].first > 0){
        v[1].first--;
        v[2].first--;
        res += v[1].second;
        res += v[2].second;
    }

    while(v[2].first > 0){
        int j = -1;
        int m = res.size();
        for(int i = 0; i < m; i++){
            if(res[i] != v[2].second && res[(i+1)%m] != v[2].second)
                j = i;
        }

        if(j == -1){
            cout << "IMPOSSIBLE" << endl;
            return;
        }

        res.insert(res.begin()+j+1, v[2].second);
        v[2].first--;
    }


    for(char c : res){
        cout << chains[c].back();
        chains[c].pop_back();
    }

   cout << endl;
}

int32_t main(){
        int T;
    cin >> T;
    for(int i = 1; i <= T; i++)
        solve(i);
}
