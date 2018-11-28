#include <bits/stdc++.h>

using namespace std;

int main(){

    int n, N, R, O, Y, G, B, V;
    string s;
    bool flag, tap, tip;

    cin >> n;

    for (int i = 1; i <= n; i++){
        flag = false;
        tap = false;
        tip = false;
        cin >> N >> R >> O >> Y >> G >> B >> V;

        s = "";
        if (G){
            s += "R";
            R--;
            for (int j = 0; j < G; j++){
                s += "GR";
                R--;
            }
            tap = true;
        }

        if (R < 0){
            if (Y > 0 || B > 0 || O > 0 || V > 0){
                flag = true;
            }else{
                s.erase(s.length()-1, 1);
            }
        }else{
            if (O){
                s += "B";
                B--;
                for (int j = 0; j < O; j++){
                    s += "OB";
                    B--;
                }
                tip = true;
            }
            if (B < 0){
                if (R > 0 || Y > 0 || V > 0 || tap){
                    flag = true;
                }else{
                    s.erase(s.length()-1, 1);
                }
            }else{
                if (V){
                    s += "Y";
                    Y--;
                    for (int j = 0; j < V; j++){
                        s += "VY";
                        Y--;
                    }
                }
                if (Y < 0){
                    if (R > 0 || B > 0 || tap || tip)
                        flag = true;
                    else
                        s.erase(s.length()-1, 1);
                }else{

                    if (s.empty()){
                        if (R >= B && R >= Y) {
                            s += 'R';
                            R--;
                        }else if (B >= R && B >= Y){
                            s += 'B';
                            B--;
                        }else{
                            s += 'Y';
                            Y--;
                        }
                    }
                    int t = R + B + Y;
                    for (int j = 0; j < t; j++){
                        if (s[s.length()-1] == 'R'){
                            if (Y > B){
                                s += 'Y';
                                Y--;
                            }else if (Y == B){
                                if (s[0] == 'Y'){
                                    s += 'Y';
                                    Y--;
                                }else{
                                    s += 'B';
                                    B--;
                                }
                            }else{
                                s += 'B';
                                B--;
                            }
                        }else if (s[s.length()-1] == 'B'){
                            if (R > Y){
                                s += 'R';
                                R--;
                            }else if (Y == R){
                                if (s[0] == 'Y'){
                                    s += 'Y';
                                    Y--;
                                }else{
                                    s += 'R';
                                    R--;
                                }
                            }else{
                                s += 'Y';
                                Y--;
                            }
                        }else{
                            if (B > R){
                                s += 'B';
                                B--;
                            }else if (R == B){
                                if (s[0] == 'R'){
                                    s += 'R';
                                    R--;
                                }else{
                                    s += 'B';
                                    B--;
                                }
                            }else{
                                s += 'R';
                                R--;
                            }
                        }

                        //cout << s << endl;
                        if (R < 0 || B < 0 || Y < 0){
                            flag = true;
                            break;
                        }
                    }
                }
            }
        }

        if (s.size() > 1 && s[0] == s[s.length()-1]) flag = true;

        cout << "Case #" << i << ": ";
        if (flag){
            cout << "IMPOSSIBLE\n";
        }else{
            cout << s << endl;
        }
    }
}
