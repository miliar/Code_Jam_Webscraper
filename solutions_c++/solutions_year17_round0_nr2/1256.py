/* Author : Jordhy Fernando */
#include<bits/stdc++.h>
#define ll long long
#define For(i,j,n) for(int i = j; i < n; i++)
#define EPS 1e-12

using namespace std;
typedef vector<int> vi;
typedef pair<int, int> ii;
typedef vector<ii> vii;

int main(){
	int T;
    cin >> T;
    for(int i = 1; i <= T; i++) {
        string N;
        cin >> N;
        int j = 1;
        while(j < N.length() && N[j] >= N[j - 1]){
            j++;
        }
        if(j < N.length()){
            N[j] = '9';
            for(int l = j + 1; l < N.length(); l++){
                N[l] = '9';
            }
            N[j - 1]--;
            int l = j - 2;
            while(l >= 0 && N[l + 1] < N[l]){
                N[l + 1] = '9';
                N[l]--;
                l--;
            }
        }
        cout << "Case #" << i << ": ";
        if(N[0] == '0'){
            for(int j = 1; j < N.length(); j++){
                cout << N[j];
            }
            cout << endl;
        }
        else{
            cout << N << endl;
        }

    }
	return 0;
}
