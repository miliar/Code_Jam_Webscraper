#include <bits/stdc++.h>
using namespace std;
int main (){
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    int z;
    cin >> z;
    for (int casess = 1; casess <= z; ++casess){
        int R,O,Y,G,B,V,N;
        cin >> N >> R >> O >> Y >> G >> B >> V;
        string a = "";
        int opt = 0;
        int pierwszy = 0;
        int poprzedni = 0;
        for (int i = 0; i < N; ++i){
             int os = 0;
             if (R > os && 1 != poprzedni){
                 os = R;
                 opt = 1;
             }
             if(B > os && 2 != poprzedni){
                os = B;
                opt = 2;
             }
             if(Y > os && 3 != poprzedni){
                os = Y;
                opt = 3;
             }
             if (opt != pierwszy && pierwszy != poprzedni){
             		if(1 == pierwszy)if (os == R)opt = 1;
             		
								if(2 == pierwszy)if (os == B)opt = 2;
             		
								if(3 == pierwszy)if (os == Y)opt = 3;
						 }
             if(opt == 1){
                a += "R";
                --R;
             }
             else if(opt == 2){
                a += "B";
                --B;
             }
             else if(opt == 3){
                a += "Y";
                --Y;
             }
             if (i == 0)pierwszy = opt;
             poprzedni = opt;
        }
        bool q = 1;
        if (a.length() != N) q = 0;
        if(q){
            for (int i = 0; i < N-1; ++i){
                if(a[i] == a[i+1]) q = 0;
            }
            //assert(q);
        }
        bool p = 0;
        if(q){
            if(a[N-1] == a[0]){ q = 0;
                p = 1;
            }
        }
        cout <<"Case #" << casess <<": ";
        if(q)cout <<a;
        else cout <<"IMPOSSIBLE";
        cout <<'\n';
    }
}
