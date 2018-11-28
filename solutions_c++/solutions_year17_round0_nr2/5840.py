#include <iostream>
using namespace std;

void printClean(int arr[20]){
    //print clean number no leading 0
    for(int i = 0; i<20;i++){
        if(arr[i] == 0){
            continue;
        } else {
            cout<<arr[i];
        }
    }
}

void generateTidyNumber(unsigned long long nbr){
    int arr[20] = {0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0};
    int len = 0;
    //unsigned long long nbr = orgNbr;
    int flag = 1;
    //initialize array
    arr[19] = nbr % 10;
    while(nbr != 0){
        arr[19-len] = nbr%10;
        nbr = nbr/10;
        len++;
    }

    //printClean(arr);

    int strtDigit = 0;
    for(strtDigit = 0; strtDigit < 20; strtDigit++){
        if(arr[strtDigit] != 0 ){
            break;
        }
    }

    for(int j = strtDigit; j<20 && len > 1;j++){
        flag = 1;
        for(int l= strtDigit, k=0; l<20; k++,l++){
            if(arr[19-k] < arr[19-(k+1)]){
                //Reduce the value of 19-k+1 by 1
                //cout<<"here"<<arr[19-k]<<" "<<arr[19-(k+1)]<<endl;
                if(arr[19-k] < arr[19 - (k+1)]){
                    //If non zero
                    if(arr[19 - (k+1)] != 0){
                        arr[19 - (k+1)] = arr[19 - (k+1)] - 1;

                        for(int m = (19-k); m<20; m++){
                            arr[m] = 9;
                        }
                    }
                }
            }
            //cout<<"Iteration";
            //printClean(arr);
            //cout<<endl;
        }
    }

    printClean(arr);
}



int main(){
    int t;
    unsigned long long n;

    cin >> t;
    for(int i=1; i <= t ;i++){
        cin >> n;
        cout<<"Case #"<<i<<": ";
        generateTidyNumber(n);
        cout<<endl;
    }
    return 0;
}
