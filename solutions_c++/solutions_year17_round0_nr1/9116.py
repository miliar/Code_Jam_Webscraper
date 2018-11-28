
    #include <bits/stdc++.h>
    using namespace std;


    int main() {     
        int n, casos= 1;
        int pulo;
        string a;
        cin >> n;
        for(int i = 0 ; i < n ; i++){
            int ans = 0;
            cin >> a >> pulo;
            for(int j = 0 ; j < a.size(); j++){
                if(a[j] == '-'){
                    //cout << "MENOS NO " << j << endl;
                    if(j + pulo > a.size()){
                    //    printf("ENTROU NO %d COM O %c\n",j, a[j]);
                        ans = -1;
                        break;
                    }
                    for(int k = j; k < j + pulo; k++){
                        if(a[k] == '-') a[k] = '+';
                        else a[k] = '-';
                    }
                    ans++;

                }
            }
            printf("Case #%d: ",casos++);
            if(ans == -1)
                cout << "IMPOSSIBLE" << endl;
            else
                cout << ans << endl;
        }

        
    return 0;-
    }
