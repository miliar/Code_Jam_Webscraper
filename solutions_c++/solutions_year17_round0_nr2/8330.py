#include <bits/stdc++.h>
using namespace std;

typedef vector <int> vi;
typedef vector <vi> vii;
typedef pair <int, int> ii;
typedef long long ll;
typedef long double ld;
vi ASD;
bool b=0;
vector <int> sum(const vector <int>& A, const vector <int>& B){
    vector <int> S(max(A.size(), B.size()), 0);
    int mellevo = 0;
    for(int i=0; i<S.size() or mellevo!=0; i++){
        if(i<A.size() and i<B.size()){
            S[i]= ((A[i]+B[i]+mellevo) % 10);
            mellevo = (A[i]+B[i]+mellevo)/10;
        }
        else if(i<A.size() and i>=B.size()){
            S[i] = (A[i] + mellevo)%10;
            mellevo = (A[i] + mellevo)/10;
        }
        else if(i>=A.size() and i<B.size()){
            S[i] = (B[i] + mellevo)%10;
            mellevo = (B[i] + mellevo)/10;
        }
        else{
            S.push_back(mellevo%10);
            mellevo = mellevo/10;
        }
    }
    return S;
}
vector <int> resta(const vector <int>& A, const vector <int>& B){
    vector <int> R(max(A.size(), B.size()));
        int mellevo = 0;
        for(int i=0; i<R.size() or mellevo!=0; i++){
            if(i<A.size() and i<B.size()){
                if(A[i] >= B[i] + mellevo){
                    R[i] = A[i] - B[i] - mellevo;
                    mellevo = 0;
                }
                else{
                    R[i] = 10 + A[i] - B[i] - mellevo;
                    mellevo = 1;
                }
            }
            else{
                if(A[i] >= mellevo){
                    R[i] = A[i] - mellevo;
                    mellevo = 0;
                }
                else{
                    R[i] = 10 + A[i] - mellevo;
                    mellevo = 1;
                }
            }
        }
    for(int i=R.size()-1; i>=0 and R[i]==0; i--){
        if(R[i]!=0) break;
        else R.pop_back();
    }
    return R;
}
bool is_tidy(vi N){
    for(int i=0; i<N.size()-1; i++){
        if(N[i] < N[i+1]) return false;
    }
    return true;
}
bool ma(const vector <int>& A, const vector <int>& B){
    if(A.size() > B.size()) return true;
    if(A.size() < B.size()) return false;
    if(A.size() == B.size()){
        for(int i=A.size()-1; i>=0; --i){
            if(A[i] < B[i]) return false;
            if(A[i] > B[i]) return true;
        }
        return true;
    }
}

void bac(vi& N, int i){
  //  for(int i=N.size()-1; i>=0; i--) cout << N[i];
  //  cout << endl;

    if(b) return;
   // if(i<0 or i>=N.size()) return;
    if(is_tidy(N)){
        b=1;
        for(int i=N.size()-1; i>=0; i--) cout << N[i];
        cout << endl;
        return;
    }

    if(N[i] >= N[i+1]){
        bac(N, i+1);
        return;
    }
    else{
        vi S;
        int a = N[i]+1;

        if(a/10!=0) S.push_back(a/10);
        S.push_back(a%10);

        while(S.size()-1 != i) S.push_back(0);
        reverse(S.begin(), S.end());

        N = resta(N, S);

        N[i+1]++;
        if(not ma(ASD, N)) N[i+1]--;
        bac(N, 0);

        return;
    }

}


int main(){
    int t;
    cin >> t;
    for(int cas=1; cas<=t; cas++){
        b=0;
        string a;
        cin >> a;
        vi N;
        for(int i=a.size()-1; i>=0; i--){
            N.push_back(a[i] - '0');
        }
        ASD = N;
        cout << "Case #" << cas << ": ";
        bac(N, 0);
    }
}
