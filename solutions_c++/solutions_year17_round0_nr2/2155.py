#include <bits/stdc++.h>

using namespace std;
int t;
long long n;
int arr[20];
int main()
{
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    cin >> t;
    for (int test = 1; test <= t; test++){
        cin >> n;
        int i =0;
        while(n>0){
            arr[i]=n%10;
            i++;
            n/=10;
        }
        int k = i;
        for (i = 0; i < k-1; i++){
            if (arr[i]<arr[i+1]){
                for (int j = 0; j <= i; j++)
                    arr[j]=9;
                arr[i+1]--;
            }
        }
        cout << "Case #" << test << ": ";
        if (arr[k-1])
            cout << arr[k-1];
        for (int i = k-2; i >= 0; i--){
            cout << arr[i];
        }
        cout << "\n";
    }
    return 0;
}
