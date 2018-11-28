#include <bits/stdc++.h>

using namespace std;

typedef vector<int> vi;
typedef vector<vi> vvi;

int main(){
    int T, N, A, AC, C, BC, B, AB;
    cin >> T;
    map<string, char> M;
    M["A"] = 'R';
    M["B"] = 'B';
    M["C"] = 'Y';
    M["AB"] = 'V';
    M["BC"] = 'G';
    M["AC"] = 'O';
    for(int t = 1; t <= T; t++){
        cin >> N >> A >> AC >> C >> BC >> B >> AB;
                // R  // O //  Y // G  // B // V
        bool imp2 = false;
        if(A > N/2 || B > N/2 || C > N/2) imp2 = true;
        char S[N];
        for(int i = 0; i < N; i++) S[i] = '.';
        bool imp = false;
        int i = 0;
        while (AB > 0 && i + 1 < N) {
            S[i] = M["C"];
            S[i+1] = M["AB"];
            C--; AB--;
            i += 2;
        }
        if(i + 1 == N) imp = true;

        if(i < N && i > 0 && S[i-1] == M["AB"]) {
            S[i] = M["C"];
            C--;
            i++;
        }

        if(C < 0) imp = true;

        while(AC > 0 && i + 1 < N) {
            S[i] = M["B"];
            S[i+1] = M["AC"];
            B--; AC--;
            i += 2;
        }
        if(i == N && S[N-1] == M["AC"] && S[0] != M["B"]) imp = true;
        if(i < N && i > 0 && S[i-1] == M["AC"]) {
            S[i] = M["B"];
            B--;
            i++;
        }
        if(B < 0) imp = true;

        while(BC > 0 && i + 1 < N) {
            S[i] = M["A"];
            S[i+1] = M["BC"];
            A--; BC--;
            i += 2;
        }
        if(i == N && S[N-1] == M["BC"] && S[0] != M["A"]) imp = true;

        if(i < N && i > 0 && S[i-1] == M["BC"]){
            S[i] = M["A"];
            A--;
            i++;
        }
        if(A < 0) imp = true;
        map<char, int> x;
        x[M["A"]] = A;
        x[M["B"]] = B;
        x[M["C"]] = C;


        if(i > 0) {

            while(x[S[i-1]] > 0 && i + 1 < N) {

                S[i + 1] = S[i - 1];
                x[S[i-1]]--;
                i += 2;
            }
            if(S[0] == S[N-1]) imp = true;
            else if(S[0] == S[i-1]) {

                if(x[M["A"]] > 0) S[N-1] = M["A"];
                if(x[M["B"]] > 0) S[N-1] = M["B"];
                if(x[M["C"]] > 0) S[N-1] = M["C"];
                i = N-3;
                if(S[i] != '.') i--;
                while(x[S[N-1]] > 0 && i >= 0) {
                    if(S[i] != '.') i--;
                    if(i >= 0) {S[i] = S[N-1]; x[S[N-1]]--;}
                    i -= 2;
                }
                if(x[S[N-1]] > 0) imp = true;
            }

            else {
                i = N-2;
                if(S[i] != '.') i--;
                while(x[S[0]] > 0 && i >= 0) {
                    if(S[i] != '.') i--;
                    if(i >= 0) {S[i] = S[0]; x[S[0]]--;}
                    i -= 2;
                }
                if(x[S[0]] > 0) imp = true;
            }

            for(int i = 0; i < N; i++) if(S[i] == '.') {
                if(x[M["A"]] > 0) S[i] = M["A"];
                if(x[M["B"]] > 0) S[i] = M["B"];
                if(x[M["C"]] > 0) S[i] = M["C"];
            }
            for(int i = 0; i + 1 < N; i++) if(S[i] == S[i+1]) imp = true;
            if(S[0] == S[N-1]) imp = true;
        }

        else {
            if(A >= B && A >= C) {
                if(A > N/2) imp = true;
                for(int i = 0; i < A && 2 * i < N; i++) S[2*i] = M["A"];
                A = 0;
            }
            else if(B >= C && B >= A) {
                for(int i = 0; i < B && 2 * i < N; i++) S[2*i] = M["B"];
                if(B > N/2) imp = true;
                B = 0;
            }
            else {
                for(int i = 0; i < C && 2 * i < N; i++) S[2*i] = M["C"];
                if(C > N/2) imp = true;
                C = 0;
            }
            if(S[N-1] != '.') imp = true;
            if(B > 0) {S[N-1] = M["B"]; B--;}
            else {
                S[N-1] = M["C"]; C--;
            }
            x[M["A"]] = A;
            x[M["B"]] = B;
            x[M["C"]] = C;
            i = N-3;
            while(x[S[N-1]] > 0 && i >= 0) {
                if(S[i] != '.') i--;
                if(i >= 0) {S[i] = S[N-1]; x[S[N-1]]--;}
                i -= 2;
            }
            if(x[S[N-1]] > 0) imp = true;
             for(int i = 0; i < N; i++) if(S[i] == '.') {
                if(x[M["A"]] > 0) S[i] = M["A"];
                if(x[M["B"]] > 0) S[i] = M["B"];
                if(x[M["C"]] > 0) S[i] = M["C"];
            }
            for(int i = 0; i + 1 < N; i++) if(S[i] == S[i+1]) imp = true;
            if(S[0] == S[N-1]) imp = true;

        }



        if(imp) printf("Case #%d: IMPOSSIBLE\n", t);
        else {
            printf("Case #%d: ", t);
            for (int i = 0; i < N; i++) cout << S[i];
            cout << endl;
        }
    }
    return 0;
}
