#include <bits/stdc++.h>

using namespace std;

int main()
{
    ifstream cin("A-large (3).in");
    ofstream cout("out.txt");
    int t ;
    cin >> t ;
    for(int tc=1 ; tc<=t ;tc++){
        int n , m ;
        cin >> n >> m ;
        vector<string> S;
        for(int i = 0  ; i <n; i++){
            string s ;
            cin >>s ;
            S.push_back(s);
        }
        set<char> used;
        for(int i = 0 ; i <n ; i++){
            for(int j = 0 ; j<m ; j++){

                if(S[i][j]=='?')continue;
                if(used.count(S[i][j]))continue;
                int a = j-1 ;
                used.insert(S[i][j]);
                while(a>=0 && S[i][a]=='?'){
                    S[i][a]=S[i][j];
                    a--;
                }
                a++;
                int b = j+1 ;
                while(b<m && S[i][b]=='?'){
                    S[i][b]=S[i][j];
                    b++;
                }
                b--;
                int c = i -1 ;
                bool ok = 1 ;
                while(c>=0 && ok){
                    for(int k = a ; k<= b ; k++){
                        if(S[c][k]!='?')ok=0;
                    }
                    if(ok)
                    for(int k = a ; k<= b ; k++){
                        S[c][k]=S[i][j];
                    }
                    c--;
                }

                int d = i + 1  ;
                ok = 1 ;
                while(d<n && ok){
                    for(int k = a ; k<= b ; k++){
                        if(S[d][k]!='?')ok=0;
                    }
                    if(ok)
                    for(int k = a ; k<= b ; k++){
                        S[d][k]=S[i][j];
                    }
                    d++;
                }
//cout << a << ' ' << b <<endl;
            }
        }
        cout << "Case #" << tc << ":\n";
        for(int i = 0 ; i<n ; i++)cout <<S[i]<<endl;
    }
    return 0;
}
