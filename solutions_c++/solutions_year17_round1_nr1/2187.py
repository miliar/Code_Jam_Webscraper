#include<bits/stdc++.h>

using namespace std;

#define ll long long
#define s(x) scanf("%lld" , &x)

int main()
{
    freopen("a2.in" , "r" , stdin);
    freopen("o1.txt" , "w" , stdout);
    ll t , p = 0;
    s(t);
    while(t--){
        p ++;
        ll r , c , i , j , pos1 , pos2 , k;
        string arr[100];
        vector<char> v;
        s(r);
        s(c);
        for(i = 0; i < r; i ++){
            cin >> arr[i];
        }
        ll flag = 0;
        for(i = 0; i < r; i ++){
            for(j = 0; j < c; j ++){
                if(arr[i][j] != '?'){
                    pos1 = i;
                    pos2 = j;
                    flag = 1;
                    break;
                }
            }
            if(flag == 1){
                break;
            }
        }
        for(i = 0; i < pos1; i ++){
            for(j = 0; j <= pos2; j ++){
                arr[i][j] = arr[pos1][pos2];
            }
        }
        cout << "Case #" << p << ":" << endl;
        for(i = pos1; i < r; i ++){
            v.clear();
            for(j = 0; j < c; j ++){
                if(arr[i][j] != '?'){
                    v.push_back(arr[i][j]);
                }
            }
            if(v.size() == 0){
                for(j = 0; j < c; j ++){
                    arr[i][j] = arr[i-1][j];
                }
            }
            else{
                k = 0;
                for(j = 0; j < c; j ++){
                    if(arr[i][j] == '?'){
                        if(k == v.size())
                            arr[i][j] = v[k-1];
                        else{
                            arr[i][j] = v[k];
                        }
                    }
                    else{
                        k ++;
                    }
                }
            }
        }
        for(i = r-1; i >= 0; i --){
            for(j = 0; j < c; j ++){
                if(arr[i][j] == '?'){
                    arr[i][j] = arr[i+1][j];
                }
            }
        }
        for(i = 0; i < r; i ++){
            for(j = 0; j < c; j ++){
                cout << arr[i][j];
            }
            cout << endl;
        }
    }
    return 0;
}
