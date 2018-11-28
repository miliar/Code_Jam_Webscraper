#include <bits/stdc++.h>

using namespace std;

int t;
int arr[50];

void action(int index)
{
    long long N;
    cin >> N;
    int ind = 0;
    while(N > 0){
        arr[ind++] = N%10;
        N /= 10;
    }
    for(int i = 0; i < ind-1; i++){
        if(arr[i] < arr[i+1]){
            for(int j = i; j >= 0; j--)
                arr[j] = 9;
            arr[i+1] -= 1;
        }
    }
    for(int i = ind-1; i >= 0; i--){
        N = N*10 + arr[i];
    }
    cout << "Case #" << index << ": " << N << endl;
}

int main()
{
    freopen("input.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    cin >> t;
    for(int i = 0; i < t; i++)
        action(i+1);
    return 0;
}
