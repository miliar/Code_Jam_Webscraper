#include<iostream>
using namespace std;
int main()
{
    int test;
    cin >> test;
    while(test)
    {
        int n,p,k=2,i,j,arr[100],arr2[100][100],c=0,cn=0;
        cin >> n >> p;
        for(i=0;i<n;i++){
            cin >> arr[i];
        }
        for(i=0;i<n;i++){
            for(j=0;j<p;j++){
                cin >> arr2[i][j];
            }
        }
        if(n==1){
        for(i=0;i<n;i++){
            for(j=0;j<n;j++){

                if(arr[i]<arr2[i][j]){
                    while(arr[i]<arr2[i][j]){
                        arr[i]*=k;
                        k++;
                }
            }

                if(arr[i] >= 0.9*arr2[i][j] && arr[i] <= 1.1*arr2[i][j]){
                    cn++;
                }
            }
            if(n==2){

                for(j=1;j<n;j++){

                if(arr[i]<arr2[i][j]){
                    while(arr[i]<arr2[i][j])
                        arr[i]*=k;
                        k++;
                }
            }

                if(arr[i] >= 0.9*arr2[i][j] && arr[i] <= 1.1*arr2[i][j]){
                    c++;
                }
            }
            }
        }
        cout << cn*c << endl;
        test--;
    }
    return 0;
}
