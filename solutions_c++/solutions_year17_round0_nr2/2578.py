#include<iostream>
#include<algorithm>
#include<fstream>
#include <iomanip>
#include <math.h>
using namespace std;
int main(){
    ifstream cin("B-large.in");
    //ofstream cout("result.txt");
    int n;
    cin >> n;
    for(int p = 0 ; p < n; p++){
        long long s;
        cin >> s;
        int a[19];
        long long result = s;
        while(true){
            int index = -1;
            for(int i = 1 ; i <= 18 ; i++){
                long long temp1 = pow(10,i);
                long long temp2 = pow(10,i-1);
                if(temp1%10 == 9){
                    temp1++;
                }
                if(temp2%10 == 9){
                    temp2++;
                }
                long long out = (s%temp1 - s%temp2)/temp2;
                a[i-1] = out;

                if(i == 18){
                    a[i-1] = s/temp2;
                }
            }

            for(int i = 0 ; i < 17 ; i++){
                if(a[i] < a[i+1]){
                    index = i+1;
                }
            }

            if(index == -1){
                break;
            }
            result = 0;

            for(int i = 0 ; i <= 18 ; i++){
                long long temp1 = pow(10,i);
                if(temp1%10 == 9){
                    temp1++;
                }
                if(i < index){
                    result = result + (9*temp1);
                }
                else if(i > index){
                    result = result + (a[i]*temp1);
                }
                else{
                    result = result + ((a[i]-1)*temp1);
                }

            }
            s = result;

        }
        cout <<"Case #"<<p+1<<": " << result << endl;
    }
}
