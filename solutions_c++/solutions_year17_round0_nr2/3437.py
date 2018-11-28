#include <iostream>
#include <vector>

using namespace std;

long long int n;

vector<int> digits;
void getLastTidy(){

    for(int i = 0; i<digits.size()-1;i++){
        if(digits[i]<digits[i+1]){
            digits[i]=9;
            if(digits[i]==0){
                for(int j = i+1; digits[j]==0; j++){
                    digits[j]==9;
                    if(digits[j+1]!=0){
                        i=j-1;
                        digits[j+1]-=1;
                    }
                }
            }else{
                digits[i]=9;
                for(int j = i; j>=0; j--){
                    digits[j]=9;
                }
                digits[i+1]-=1;
            }
        }
    }

    int i = digits.size()-1;

    while(digits[i]==0)i--;

    for(; i>=0; i--){
        cout<<digits[i];
    }
    cout<<endl;

}

int main(){

    int tt; cin>>tt;

    for(int i = 0; i< tt; i++){
        cin>>n;
        digits.clear();

        while(n>0){
            digits.push_back(n%10);
            n/=10;
        }

        cout<<"Case #"<<i+1<<": ";

        getLastTidy();
    }
    return 0;
}
