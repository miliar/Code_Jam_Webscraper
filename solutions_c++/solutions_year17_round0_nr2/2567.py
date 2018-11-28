#include <iostream>
#include <list>
#include <iomanip>
#include <set>
#include <vector>
#include <cstring>
#include <algorithm>
#include <complex>
#include <map>
#include <queue>
#include <stack>
#include <functional>
#include <unordered_set>
#include <unordered_map>

using namespace std;
const int MAX = 5 * 10000;
const long long MOD = 1e9 + 7;
const double PI = 3.141592653589793238462643383279502884;
const double EPS = 1e-9;

double dist_stand(double x1, double y1, double x2, double y2){
    return sqrt((x1 - x2)*(x1 - x2) + (y1 - y2)*(y1 - y2));
}
int dist_man(int x1, int y1, int x2, int y2){
    return (abs(x1 - x2) + abs(y1 - y2));
}





int main()
{
    int t;
    int mas[20];
    cin >> t;
    for(int l = 0;l<t;l++){
        string s;
        cin >> s;
        for(int i = 0;i<20;i++){
            mas[i] = 11;
        }
        int lenmas = s.size();
        for(int i = 0;i<s.size();i++) {
            mas[i] = int(s[i]-'0');
        }

        for(int i = lenmas-1;i>=1;i--){
            if(mas[i] < mas[i-1]){
                mas[i] = 9;
                int j = i-1;
                while(mas[j]==0){
                    mas[j] = 9;
                    j--;
                }
                mas[j]--;
                for (int k = i+1;k<lenmas;k++){
                    mas[k] = 9;
                }
            }
        }

        long long ans = 0;
        for(int i = 0;i<lenmas;i++){
            ans = ans*10+mas[i];
        }
        cout << "Case #" << (l+1) << ": ";
        cout << ans;
        cout << endl;
    }

    cout << endl;
    return 0;
}