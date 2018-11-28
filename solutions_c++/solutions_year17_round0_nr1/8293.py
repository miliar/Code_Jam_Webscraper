#include <bits/stdc++.h>
using namespace std;

typedef vector <int> vi;
typedef vector <vi> vii;

vi LA,ITL;
vii I;
int s = 0;
vector <int> SOL;
bool us(string &A){
    for(int i=0; i<A.size(); i++){
        if(A[i]!='+') return false;
    }
    return true;
}
bool us2(vector <bool>& A){
    for(int i=0; i<A.size(); i++){
        if(A[i]==0) return false;
    }
    return true;
}

void rec(string& L, vector <bool>& IU, int ps){
  /*  cerr << "nueva rama" << endl;
    for(int i=0; i<L.size(); i++) cerr << L[i] << " ";
    cerr << endl << ps << endl;
    for(int i=0; i<IU.size(); i++) cerr << IU[i] << " ";*/

  //  if(us2(IU)) return;
    if(us(L)){
        s++;
        SOL.push_back(ps);
        return;
    }
    for(int i=0; i<I.size() and IU[i]==false; i++){
        IU[i] = true;
        for(int j=0; j<I[i].size(); j++){
            if(I[i][j] == 1){
                if(L[j] == '+') L[j] = '-';
                else if(L[j] == '-') L[j] = '+';
            }
        }

        rec(L, IU, ps+1);

        IU[i] = false;
        for(int j=0; j<I[i].size(); j++){
            if(I[i][j] == 1){
                if(L[j] == '+') L[j] = '-';
                else if(L[j] == '-') L[j] = '+';
            }
        }
    }
    return;
}

int main(){
    int t;
    cin >> t;
    for(int cas=1; cas<=t; cas++){
        s=0;
        int n;

        string st;
        cin >> st >> n;
        I = vii ();
        SOL = vi ();
        vector <bool> IU(st.size()-n+1, false);

        for(int i=0; i<st.size()-n+1; i++){
            vi A(st.size());
            for(int j=i; j<i+n; j++) A[j]=1;
            I.push_back(A);
        }

   /*     for(int i=0; i<I.size(); i++){
            for(int j=0; j<I[i].size(); j++) cout << I[i][j];
            cout << endl;

        } */

        rec(st, IU, 0);
        int so=0;
        if(s>0) so = *min_element(SOL.begin(), SOL.end());

        if(s>0) cout << "Case #" << cas << ": " << so << endl;
        else cout << "Case #" << cas << ": IMPOSSIBLE" << endl;
    }
}
