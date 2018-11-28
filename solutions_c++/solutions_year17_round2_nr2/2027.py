#include <bits/stdc++.h>
#define ll long long
#define ss second
#define ff first
using namespace std;

int max_3(int r,int y, int b){

    if(r >= y && r >= b){
        return 1;
    }

    if(y >= r && y >= b){
        return 2;
    }

    if(b >= r && b >= y){
        return 3;
    }

}

int main(){
    freopen("A.in", "r", stdin);
    freopen("A.out", "w", stdout);
    int t;
    cin >> t;
    for(int z = 1; z <= t; ++z)
    {
        int g, v, o, r, y, b;
        int n;

        cin  >> n >> r >> o >> y >> g >> b >> v;
        if( (g && g > r-1) || (v && v > y-1) || (o && o > b -1) ){
            printf("Case #%d: IMPOSSIBLE\n", z);
            continue;
        }
        else {

            r -= g;
            y -= v;
            b -= o;

            string gg = "";
            if(g)gg += "R";
            while(g--)gg += "GR";
            string vv = "";
            if(v)vv += "Y";
            while(v--)vv += "VY";
            string oo = "";
            if(o)oo += "B";
            while(o--)oo += "BO";



            int maxI = max_3(r, y, b);
            string ans = "";
            if(maxI == 1)ans+="R", --r;
            else if(maxI == 3)ans+="B", --b;
            else if(maxI == 2)ans+="Y", --y;

            int f = true;
            int i = 0;
            while(r + b + y != 0){
                if(ans[i] == 'R'){
                    if(y + b == 0){
                        f = false;
                        break;
                    }

                    if(y == b && ans[0] == 'Y'){
                            ans += "Y";
                            --y;
                    }

                    else if(y == b && ans[0] == 'B'){
                            ans += "B";
                            --b;
                    }

                    else if(y > b){
                        ans += "Y";
                        --y;
                    }else {
                        ans += "B";
                        --b;
                    }

                }
                else if(ans[i] == 'B'){

                    if(y + r == 0){
                        f = false;
                        break;
                    }

                    if(y == r && ans[0] == 'Y'){
                            ans += "Y";
                            --y;
                    }

                    else if(y == r && ans[0] == 'R'){
                            ans += "R";
                            --r;
                    }

                    else if(y > r){
                        ans += "Y";
                        --y;
                    }else {
                        ans += "R";
                        --r;
                    }

                }
                else if(ans[i] == 'Y'){

                    if(r + b == 0){
                        f = false;
                        break;
                    }

                    if(b == r && ans[0] == 'B'){
                            ans += "B";
                            --b;
                    }

                    else if(y == r && ans[0] == 'R'){
                            ans += "R";
                            --r;
                    }

                    else if(r > b){
                        ans += "R";
                        --r;
                    }else {
                        ans += "B";
                        --b;
                    }

                }

                ++i;
            }


            if(!f || (n != 1 && ans[i] == ans[0])){
                printf("Case #%d: IMPOSSIBLE\n", z);
            }else {printf("Case #%d: ", z); cout << ans << "\n";
            }








        }
    }
}
