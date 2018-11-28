#include <bits/stdc++.h>
using namespace std;

typedef vector <int> vi;
typedef vector <vi> vii;
typedef pair <int, int> ii;
typedef long long ll;
typedef long double ld;

vi S, F, L, R;

void act(){
    for(int i=0; i<S.size(); i++){
        if(S[i]==1){
            L[i] = R[i] = 0;
        }
        else{
            for(int j=i+1; j<S.size(); j++){
                if(S[j]==1){
                   R[i] = j-i;
                   break;
                }
            }
            for(int j=i-1; j>=0; j--){
                if(S[j]==1){
                   L[i] = i-j;
                   break;
                }
            }
        }
    }
}

int chose(){
    int ma=0;
    for(int i=0; i<L.size(); i++){
        if(min(L[i], R[i]) > ma) ma = min(L[i], R[i]);
    }
  //  cout <<"*"<< ma << endl;

    vector <ii> MA;
    for(int i=0; i<L.size(); i++){
        if(min(L[i], R[i]) == ma){
            MA.push_back(make_pair(max(L[i], R[i]), i));
        }
    }
    ii m = *max_element(MA.begin(), MA.end());
    for(int i=0; i<MA.size(); i++){
        if(MA[i].first == m.first){
            return MA[i].second;
        }
    }
}


int main(){
    int numcas;
    cin >> numcas;
    for(int cas=1; cas<=numcas; cas++){
        int n, k;
        cin >> n >> k;
        S = vi(n, 0);
        F = vi(n, 1);
        R = L = vi (n);
        for(int i=0; i<L.size(); i++) L[i] = i+1;
        for(int i=0; i<R.size(); i++) R[i] = n-i;

        bool ex=0;
        int p=0;
        k--;
        while(k--){
          /*  for(int i=0; i<S.size(); i++) cout << S[i];
            cout << endl;
            for(int i=0; i<L.size(); i++) cout << L[i];
            cout << endl;
            for(int i=0; i<R.size(); i++) cout << R[i];
            cout << endl;*/
            if(S == F){
                ex=1;
                break;
            }

            p = chose();
            S[p] = 1;
            act();
        }
        p = chose();
        //S[p] = 1;
        //act();
        cout << "Case #" << cas << ": " << max(L[p], R[p])-1 << " " << min(L[p], R[p])-1 << endl;
    }
}
