#include <iostream>
#include <string>
#define INF 1000000007
using namespace std;
string s;
bool arr[1010],aux[1010],corr;
int t,k,caso,n,temp,ans;
int main()
{
    cin >> t;
    while (t--){
        caso++;
        cin >> s >> k;
        n = s.length();
        for(int i=0;i<n;i++){
            arr[i] = (s[i]=='+');
        }
        for (int i =0;i<n;i++){
            aux[i] = arr[i];
        }
        //izquierda a derecha
        ans = INF;
        temp =0;
        for (int i=0;i<n-k+1;i++){
            if (!aux[i]){
                temp++;
                for (int j=0;j<k;j++){
                    aux [i+j] = ! aux[i+j];
                }
            }
        }
        corr = true;
        for (int i=0;i<n;i++){
            corr = corr & aux[i];
        }
        if (corr){
            ans = min(ans,temp);
        }

        //derecha a izquierda
        for (int i =0;i<n;i++){
            aux[i] = arr[i];
        }
        temp =0;
        for (int i=n-1;i>=k-1;i--){
            if (!aux[i]){
                temp++;
                for (int j=0;j<k;j++){
                    aux [i-j] = ! aux[i-j];
                }
            }
        }
        corr = true;
        for (int i=0;i<n;i++){
            corr = corr & aux[i];
        }
        if (corr){
            ans = min(ans,temp);
        }
        cout << "Case #" << caso << ": ";
        if (ans != INF){
            cout << ans << "\n";
        } else {
            cout << "IMPOSSIBLE\n";
        }
    }
    return 0;
}
