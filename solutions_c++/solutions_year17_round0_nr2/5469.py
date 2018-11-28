#include <iostream>

using namespace std;

int main(){
        int t;
        cin >> t;
        int ca = 1;
        while (t--){
                long long int n;
                cin >> n;
                int arr[19];
                for (int i=18;i>=0;i--){
                        arr[i] = n%10;
                        n/=10;
                }
                int changed = 1;
                while (changed){
                        changed = 0;
                        for (int i=0;i<18;i++){
                                if (arr[i]>arr[i+1]){
                                        changed = 1;
                                        arr[i]--;     
                                        while (i<18){
                                                i++;
                                                arr[i] = 9;
                                        }
                                }
                        } 
                }
                
                cout << "Case #"<<ca++ << ": ";
                int ctr = 0;
                while (arr[ctr]==0 && ctr<19){
                        ctr++;
                }
                while (ctr<19){
                        cout << arr[ctr++];
                }
                cout << '\n';
        }
        return 0;
}
