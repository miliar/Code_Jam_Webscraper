#include <bits/stdc++.h>
#define fi first
#define se second
#define mp make_pair
#define pb push_back
#define endl "\n"
#define cv(c) (int)(c-'a')
#define db(x) cerr << #x << ": " << x << " "
#define db2(x, y) cerr << #x << ": " << x << " " << #y << ": " << y << " "
#define bn() cerr << endl
#define sep() cerr << "-------" << endl
#define inf 1000000002
#define linf 1000000000000000002

using namespace std;
typedef long long ll;
typedef long double ld;

int c[3];
int ind[3];
int n;
vector<char> res[4];
vector<char> rf;
vector<pair<int, char> > poenomeio;
bool cmp(int a, int b){
    return c[a] < c[b];
}
bool solve(int r, int b, int y){
    c[0] = r;
    c[1] = b;
    c[2] = y;
    int cnt = 0;
    for (int i = 0; i < 3; i++){
        ind[i] = i;
        cnt += (c[i] == 0);
    }
    if (n == 3 && cnt) return false;
    sort(ind, ind + 3, cmp);
    int maior = ind[2];
    int meio = ind[1];
    int menor = ind[0];
    char cmaior, cmeio, cmenor;
    if (maior == 0) cmaior = 'R';
    else if (maior == 1) cmaior = 'B';
    else cmaior = 'Y';

    if (meio == 0) cmeio = 'R';
    else if (meio == 1) cmeio = 'B';
    else cmeio = 'Y';

    if (menor == 0) cmenor = 'R';
    else if (menor == 1) cmenor = 'B';
    else cmenor = 'Y';
    if (c[menor] + c[meio] + 1 < c[maior]) return false;
    while (c[meio] > c[menor]){
        res[0].pb(cmaior);
        res[0].pb(cmeio);
        c[maior]--;
        c[meio]--;
    }
    while (c[maior] > c[meio] && c[meio]){
        res[0].pb(cmaior);
        res[0].pb(cmeio);
        res[0].pb(cmaior);
        res[0].pb(cmenor);
        c[maior] -= 2;
        c[meio] --;
        c[menor] --;
    }
    while (c[maior] && c[meio]){
        res[0].pb(cmaior);
        res[0].pb(cmeio);
        res[0].pb(cmenor);
        c[maior]--;
    }
    if (c[maior]){
        res[0].pb(cmaior);
    }
    return true;
}
int main(){
    ios::sync_with_stdio(false);
    freopen("B-small-attempt1.in", "r", stdin);
    freopen("out", "w", stdout);

    int te;
    cin >> te;
    int caso = 1;
    while (te--){
        int r, o, y, g, b, v;
        cin >> n >> r >> o >> y >> g >> b >> v;
        cout << "Case #" << caso << ": ";
        caso++;
        bool da = true;
        for (int i = 0; i < 4; i++){
            res[i].clear();
        }
        rf.clear();
        poenomeio.clear();
        for (int i = 0; i < o; i++){
            if (i == 0){
                if (!b){
                    da = false;
                    break;
                }
                res[1].pb('B');
                b--;
            }
            if (!b){
                int qtd = 0;
                for (int i = 0; i < 4; i++){
                    qtd += res[i].size();
                }
                if (n == qtd + 1){
                    res[1].pb('O');
                    break;
                }
                da = false;
                break;
            }
            res[1].pb('O');
            res[1].pb('B');
            b--;
        }
        if (da == false){
            cout << "IMPOSSIBLE" << endl;
            continue;
        }
        for (int i = 0; i < g; i++){
            if (i == 0){
                if (!r){
                    da = false;
                    break;
                }
                res[2].pb('R');
                r--;
            }
            if (!r){
                int qtd = 0;
                for (int i = 0; i < 4; i++){
                    qtd += res[i].size();
                }
                if (n == qtd + 1){
                    res[2].pb('G');
                    break;
                }
                da = false;
                break;
            }
            res[2].pb('G');
            res[2].pb('R');
            r--;
        }
        if (da == false){
            cout << "IMPOSSIBLE" << endl;
            continue;
        }
        for (int i = 0; i < v; i++){
            if (i == 0){
                if (!y){
                    da = false;
                    break;
                }
                res[3].pb('Y');
                y--;
            }
            if (!y){
                int qtd = 0;
                for (int i = 0; i < 4; i++){
                    qtd += res[i].size();
                }
                if (n == qtd + 1){
                    res[3].pb('V');
                    break;
                }
                da = false;
                break;
            }
            res[3].pb('V');
            res[3].pb('Y');
            y--;
        }
        if (da == false){
            cout << "IMPOSSIBLE" << endl;
            continue;
        }
        if (!solve(r, b, y)){
            cout << "IMPOSSIBLE" << endl;
            continue;
        }
        if (res[0].size()){
            for (int i = 0; i < res[0].size(); i++){
                rf.pb(res[0][i]);
            }
        }

        int ate = rf.size() - 1;

        bool nocomeco = true, nofinal = true;
        int ja = 0;
        if (rf[ate] == 'B'){
            if (res[2].size()){
                for (int i = 0; i < res[2].size(); i++){
                    rf.pb(res[2][i]);
                }
                ja |= (1 << 1);
            }
            else if (res[3].size()){
                for (int i = 0; i < res[3].size(); i++){
                    rf.pb(res[3][i]);
                }
                ja |= (1 << 2);
            }
            else{
                if (res[1].size()){
                    for (int i = 0; i < ate - 1; i++){
                        if ((rf[i] == 'R' || rf[i] == 'Y') && ((rf[i + 1] == 'R' || rf[i + 1] == 'Y'))){
                            poenomeio.pb(mp(i, 'B'));
                            nocomeco = false;
                            break;
                        }
                    }
                    if (nocomeco){
                        da = false;
                    }
                    for (int i = 0; i < res[1].size(); i++){
                        rf.pb(res[1][i]);
                    }
                    ja &= (1 << 0);
                }
            }
        }
        if (da == false){
            cout << "IMPOSSIBLE" << endl;
            continue;
        }
        if (rf[ate] == 'R'){
            if (res[3].size()){
                for (int i = 0; i < res[3].size(); i++){
                    rf.pb(res[3][i]);
                }
                ja |= (1 << 2);
            }
            else if (res[1].size()){
                for (int i = 0; i < res[1].size(); i++){
                    rf.pb(res[1][i]);
                }
                ja |= (1 << 0);
            }
            else{
                if (res[2].size()){
                    for (int i = 0; i < ate - 1; i++){
                        if ((rf[i] == 'B' || rf[i] == 'Y') && ((rf[i + 1] == 'B' || rf[i + 1] == 'Y'))){
                            poenomeio.pb(mp(i, 'R'));
                            nocomeco = false;
                        }
                    }
                    if (nocomeco){
                        da = false;
                    }
                    for (int i = 0; i < res[1].size(); i++){
                        rf.pb(res[2][i]);
                    }
                    ja |= (1 << 1);
                }
            }
        }
        if (da == false){
            cout << "IMPOSSIBLE" << endl;
            continue;
        }
        if (rf[ate] == 'Y'){
            if (res[1].size()){
                for (int i = 0; i < res[1].size(); i++){
                    rf.pb(res[1][i]);
                }
                ja |= (1 << 0);
            }
            else if (res[2].size()){
                for (int i = 0; i < res[2].size(); i++){
                    rf.pb(res[2][i]);
                }
                ja |= (1 << 1);
            }
            else{
                if (res[3].size()){
                    for (int i = 0; i < ate - 1; i++){
                        if ((rf[i] == 'B' || rf[i] == 'R') && ((rf[i + 1] == 'B' || rf[i + 1] == 'R'))){
                            poenomeio.pb(mp(i, 'Y'));
                            nocomeco = false;
                        }
                    }
                    if (nocomeco){
                        da = false;
                    }
                    for (int i = 0; i < res[1].size(); i++){
                        rf.pb(res[3][i]);
                    }
                    ja |= (1 << 2);
                }
            }
        }
        if (da == false){
            cout << "IMPOSSIBLE" << endl;
            continue;
        }

        if (rf[0] == 'B'){
            if (res[1].size()){
                if (!(ja & (1 << 0))){
                    for (int i = 0; i < res[1].size(); i++){
                        rf.pb(res[1][i]);
                    }
                    ja |= (1 << 0);
                }
            }
        }
        if (rf[0] == 'R'){
            if (res[2].size()){
                if (!(ja & (1 << 1))){
                    for (int i = 0; i < res[2].size(); i++){
                        rf.pb(res[2][i]);
                    }
                    ja |= (1 << 1);
                }
            }
        }
        if (rf[0] == 'Y'){
            if (res[3].size()){
                if (!(ja & (1 << 2))){
                    for (int i = 0; i < res[3].size(); i++){
                        rf.pb(res[3][i]);
                    }
                    ja |= (1 << 2);
                }
            }
        }
        for (int i = 0; i < 3; i++){
            if (!(ja & (1 << i)) && res[i + 1].size()){
                for (int j = 0; j < res[i + 1].size(); j++){
                    rf.pb(res[i + 1][j]);
                }
            }
        }
        if (rf[rf.size() - 1] == rf[0]){
            if (rf[0] == 'B'){
                for (int i = 0; i < rf.size() - 1; i++){
                    if ((rf[i] == 'Y' || rf[i] == 'R') && ((rf[i + 1] == 'Y' || rf[i + 1] == 'R'))){
                        if (poenomeio.size() > 0 && poenomeio[0].fi == i) continue;
                        poenomeio.pb(mp(i, 'B'));
                        nofinal = false;
                    }
                }
                if (nofinal) da = false;
            }
            if (rf[0] == 'R'){
                for (int i = 0; i < rf.size() - 1; i++){
                    if ((rf[i] == 'Y' || rf[i] == 'B') && ((rf[i + 1] == 'Y' || rf[i + 1] == 'B'))){
                        if (poenomeio.size() > 0 && poenomeio[0].fi == i) continue;
                        cout << i << endl;
                        poenomeio.pb(mp(i, 'R'));
                        nofinal = false;
                    }
                }
                if (nofinal) da = false;
            }
            if (rf[0] == 'Y'){
                for (int i = 0; i < rf.size() - 1; i++){
                    if ((rf[i] == 'B' || rf[i] == 'R') && ((rf[i + 1] == 'B' || rf[i + 1] == 'R'))){
                        if (poenomeio.size() > 0 && poenomeio[0].fi == i) continue;
                        poenomeio.pb(mp(i, 'Y'));
                        nofinal = false;
                    }
                }
                if (nofinal) da = false;
            }
        }
        if (da == false){
            cout << "IMPOSSIBLE" << endl;
            continue;
        }
        for (int i = 0; i < rf.size(); i++){
            if (i != ate && i != rf.size() - 1){
                cout << rf[i];
            }
            else if (i == ate){
                if (nocomeco)
                    cout << rf[i];
            }
            else if (i == rf.size() - 1){
                if (nofinal) cout << rf[i];
            }
            for (int j = 0; j < poenomeio.size(); j++){
                if (poenomeio[j].fi == i){
                    cout << poenomeio[j].se;
                }
            }
        }cout << endl;
    }
    return 0;
}

