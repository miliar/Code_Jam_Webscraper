/*|In The Name Of Allah|*/

//your input- file : RECin.txt
//your output file : RECot.txt

#include <bits/stdc++.h>

using namespace std;

int K , cnt = 1e9 , n;
string org;

void flip(int from){
     int tm = K;
     while(tm--){
        org[from] = (org[from] == '+') ? '-' : '+';
        from++;
     }
}

int get(){
    int c = 0;
    for(int i = 0; i < n; i++)
        c += (org[i] == '+');
    return c;
}

bool vis[11];

void mini(int cmt){
    if(get() == n){
         cnt = min(cnt , cmt);
    } else {
         for(int i = 0; i + K - 1 < n; i++){
             if(org[i] == '+' && !vis[i]){
                 flip(i);
                 vis[i] = true;
                 mini(cmt + 1);
                 vis[i] = false;
                 flip(i);
             } else if(!vis[i]) {
                 flip(i);
                 vis[i] = true;
                 mini(cmt + 1);
                 vis[i] = false;
                 flip(i);
             }
         }
    }
}

int T;

int main(){
    freopen("A-small-attempt0.in" , "r" , stdin);
    freopen("ot.txt" , "w" , stdout);
    cin >> T;
    for(int i = 1; i <= T; i++){
        cin >> org >> K;
        n = org.size();
        mini(0);
        cout << "Case #" << i << ": ";
        if(cnt == 1e9)
            cout << "IMPOSSIBLE\n";
        else
            cout << cnt << endl;
        cnt = 1e9;
    }
    return 0;
}
