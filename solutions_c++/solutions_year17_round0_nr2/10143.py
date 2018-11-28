#include<iostream>

using namespace std;

int numLength(int number){
    int digits = 0;
    if (number < 0) digits = 1; // remove this line if '-' counts as a digit
    while (number) {
        number /= 10;
        digits++;
    }
    return digits;
}

bool isTidy(int n){
    //int numDigits = numLength(n);
    int temp = n%10;;
    while(n > 0){
        n = n/10;
        if(temp < n%10){
            return false;
        }else{
            temp = n%10;
        }
    }
    return true;
}

void lastTidyNumber(int n){
    
    do{
        if(isTidy(n)){
            cout<<n<<endl;
            break;
        }
    }while(n--);
}

int main(){
    int t;
    cin>>t;
    int i = 1;
    while(t--){
        int n;
        cin>>n;
        cout<<"Case #"<<i<<": ";
        lastTidyNumber(n);
        i++;
    }
    return 0;
}
