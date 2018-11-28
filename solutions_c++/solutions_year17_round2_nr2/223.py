#include <iostream>
#include <cstdio>
#include <vector>
#include <algorithm>
#include <string>
using namespace std;

int N, R, O, Y, G, B, V;


char S[1024];

void blah(int n, const char* s) {
    for (int i=0; i<n; i++) printf("%s", s);
}

int main() {
    int T; cin>>T;
    for (int t=1; t<=T; t++) {
        cin>>N>>R>>O>>Y>>G>>B>>V;
        
        try {
           printf("Case #%d: ", t);
           vector<pair<int, char> > v(3);
           int ix;
           
           if (B==O && B>0)
                if (B+O==N) { blah(B, "BO"); goto here; }
                else throw 1;
           if (R==G && R>0)
                if (R+G==N) { blah(R, "RG"); goto here; }
                else throw 1;
           if (Y==V && Y>0)
                if (Y+V==N) { blah(Y, "YV"); goto here; }
                else throw 1;
                
            B-=O, R-=G, Y-=V;
            N-=2*O, N-=2*G, N-=2*V;
            if (B<0 || R<0 || Y<0) throw 1;
            if (B>N/2 || R>N/2 || Y>N/2) throw 1;
            fill(S, S+N, '.');
            S[N]=0;
            v[0].first=B, v[0].second='B';
            v[1].first=R, v[1].second='R';
            v[2].first=Y, v[2].second='Y';
            sort(v.begin(), v.end());
            ix=0;
            while (v[2].first > 0)
                S[ix] = v[2].second, ix+=2, v[2].first--;
            ix=N-1;
            while (v[1].first > 0) {
                if (S[ix]=='.') S[ix] = v[1].second, ix-=2, v[1].first--;
                else ix--;
            }
            ix=N-1;
            while (v[0].first > 0) {
                if (S[ix]=='.') S[ix] = v[0].second, ix-=2, v[0].first--;
                else ix--;
            }
            
            
            for (int i=0; i<N; i++) {
                printf("%c", S[i]);
                if (S[i]=='B' && O>0)
                    blah(O, "OB"), O=0;
                if (S[i]=='R' && G>0)
                    blah(G, "GR"), G=0;
                if (S[i]=='Y' && V>0)
                    blah(V, "VY"), V=0;
            }
here:
            printf("\n");
        }
        catch (...) {
            printf("IMPOSSIBLE\n");
        }
        
    }
    return 0;
}
