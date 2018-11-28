#include<bits/stdc++.h>

using namespace std;

#define int long long

#define f first
#define s second

int32_t main(){
    ios_base::sync_with_stdio(0);
    ifstream fin("inputC.txt");
    ofstream fout("outputC.txt");
    #define cin fin
    #define cout fout
    int t;
    cin >> t;
//    cout << t << endl;
    for(int i = 0; i < t; ++i){
        int n, k;
        cin >> n >> k;
        cout << "Case #" << i+1 << ": ";
//        fout << "Case #" << i+1 << ": ";
        map<int, int> m;
        m[-n] = 1;
        while(!m.empty()){
            pair<int, int> p = *m.begin();
            m.erase(m.begin());
            if(k > p.s){
                k -= p.s;
                m[-(((-p.f)-1)/2)] += p.s;
                m[-((-p.f)/2)] += p.s;
            }
            else{
                cout << (-p.f)/2 << ' ' << ((-p.f)-1)/2 << endl;
//                fout << (-p.f)/2 << ' ' << ((-p.f)-1)/2 << endl;
                break;
            }
        }
    }
}
