#include <bits/stdc++.h>

using namespace std;

int t;
int r,c;
char inp[55][55];
int arr[55][55];
vector< pair<int,int> > shooters;
int main()
{
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    cin >> t;
    for (int test = 1; test <= t; test++){
        cin >> r >> c;
        shooters.clear();
        for (int i = 0; i < r; i++){
            getchar();
            for (int j = 0; j < c; j++){
                arr[i][j]=0;
                inp[i][j] = getchar();
                if (inp[i][j] == '|')
                    inp[i][j] = '-';
                if (inp[i][j] == '-')
                    shooters.push_back(make_pair(i,j));
            }
        }
        bool impossible = false;
        for (int i = 0; i < shooters.size(); i++){
            int p = shooters[i].first;
            int q = shooters[i].second;
            int left = q-1;
            int right = q+1;
            while(left >= 0 && inp[p][left] == '.'){
                arr[p][left]++;
                left--;
            }
            while (right <c && inp[p][right] == '.'){
                arr[p][right]++;
                right++;
            }
            if (left >= 0 && inp[p][left] == '|' || right < c && inp[p][right] == '-'){
                inp[p][q] = '|';
                while(left < q){
                    left++;
                    arr[p][left]--;
                }
                while(right > q){
                    right--;
                    arr[p][right]--;
                }
                int top = p-1;
                int bot = p+1;
                while(top >= 0 && inp[top][q] == '.'){
                    arr[top][q]++;
                    top--;
                }
                while(bot < r && inp[bot][q] == '.'){
                    arr[bot][q]++;
                    bot++;
                }
                if (top >= 0 && (inp[top][q] == '|' || inp[top][q] == '-') || bot < r && inp[bot][q] == '-'){
                    impossible = true;
                    break;
                }
            }
        }
        if (impossible){
            cout << "Case #" << test << ": IMPOSSIBLE\n";
        }
        else{
            for (int i = 0; i < r; i++){
                for (int j = 0; j < c; j++){
                    if (inp[i][j] == '.' && arr[i][j] == 0){
                        int k = i-1;
                        int p = i+1;
                        while (k >= 0 && inp[k][j] == '.') k--;
                        while(p < r && inp[p][j] == '.') p++;
                        if (k >= 0 && p < r && inp[k][j] == '-' && inp[p][j] == '-'){
                            impossible = true;
                            break;
                        }
                        else if (k >= 0 && inp[k][j] == '-')
                            p=k;
                        if (p < r && inp[p][j] == '-'){
                            inp[p][j]='|';
                            int left = j-1;
                            int right = j+1;
                            while(inp[p][left] == '.'){
                                arr[p][left]--;
                                left--;
                            }
                            while(inp[p][right] == '.'){
                                arr[p][right]--;
                                right++;
                            }
                            int top = p-1;
                            int bot = p+1;
                            while(inp[top][j] == '.'){
                                arr[top][j]++;
                                top--;
                            }
                            while(inp[bot][j] == '.'){
                                arr[bot][j]++;
                                bot++;
                            }
                            if (top >= 0 && inp[top][j] == '-' || bot < r && inp[bot][j] == '-'){
                                impossible = true;
                                break;
                            }
                        }
                        else{
                            impossible = true;
                            break;
                        }
                    }
                }
                if (impossible) break;
            }
            if (impossible){
                cout << "Case #" << test << ": IMPOSSIBLE\n";
            }
            else{
                for (int i = 0; i < r; i++){
                    for (int j = 0; j < c; j++){
                        if (inp[i][j]=='.'&&arr[i][j]==0) impossible=true;
                    }
                }
                if (impossible){
                    cout << "Case #" << test << ": IMPOSSIBLE\n";
                }
                else{
                    cout << "Case #" << test << ": POSSIBLE\n";
                    for (int i = 0; i < r; i++){
                        for (int j = 0; j < c; j++){
                            cout << inp[i][j];
                        }
                        cout << '\n';
                    }
                }
            }
        }
    }
    return 0;
}
