
    #include <bits/stdc++.h>
    using namespace std;


    int main() {     
        int n, caso = 1, x;
        cin >> n;
        vector<char> v;
        for(int i = 0 ; i < n ; i++){
            cin >> x;
            printf("Case #%d: ",caso++);
            if(x < 10)
            cout << x << endl;
            else{
                char aux[1000];
                for(int j = x ; j >= 0; j--){
                    bool ok = true;
                    sprintf(aux,"%d", j);
                    //printf("AUX TA %s\n",aux);
                    for(int k = 1 ; aux[k] != '\0'; k++){
                        if(aux[k] < aux[k-1]){
                           // printf("RECEBEU FALSE COM O %d\n",j);
                            ok = false;
                            break;
                        }
                    }    
                    if(ok){
                        cout << j << endl;
                        break;
                    }
                }

              }




        }  
        
    return 0;
    }
