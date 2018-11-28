#include <bits/stdc++.h>
using namespace std;

char arr[100][100];

int main(){
	ios_base::sync_with_stdio(0);
	cin.tie(0);
	
	long long T, cas, R, C, i, j, f, k;
	cin >> T;
	for(cas=1;cas<=T;cas++){
	    cout << "Case #" << cas << ":\n";
        cin >> R >> C;
        for(i=0;i<R;i++){
            f = 1;
            for(j=0;j<C;j++){
                cin >> arr[i][j];
                if(arr[i][j]!='?') f=0;
            }
            if(!f){
                for(j=0;j<C;j++){
                    if(arr[i][j]!='?'){
                        for(k=j-1;k>=0 and arr[i][k]=='?';k--){
                            arr[i][k] = arr[i][j];
                        }
                    }
                }
                for(j=C-1;j>=0;j--){
                    if(arr[i][j]!='?'){
                        for(k=j+1;k<C and arr[i][k]=='?';k++){
                            arr[i][k] = arr[i][j];
                        }
                    }
                }
            }
        }
        for(i=0;i<R;i++){
            for(j=0;j<C;j++){
                f=1;
                if(arr[i][j]!='?') f=0;
            }
            if(f){
                f=0;
                for(k=i-1;k>=0;k--){
                    if(arr[k][0]!='?'){
                        f=1;
                        break;
                    }
                }
                if(!f){
                    for(k=i+1;k<R;k++){
                        if(arr[k][0]!='?'){
                            f=1;
                            break;
                        }
                    }
                }
                for(j=0;j<C;j++){
                    arr[i][j] = arr[k][j];
                }
            }
        }
        for(i=0;i<R;i++){
            for(j=0;j<C;j++){
                cout << arr[i][j];
            }
            cout << '\n';
        }
	}
	return 0;
}
