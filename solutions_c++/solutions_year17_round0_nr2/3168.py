// Acroph created at 2017-04-08 14:41:55
// ptx9363@gmail.com for more cantact

#include <iostream>
#include <string>

using namespace std;

int main(){
    int T;
    char number[20];
    cin.getline(number, 20);
    
    T = atoi(number);

    for(int t=0; t<T; t++){
        cin.getline(number, 20);
        
        int n = strlen(number);
        int f=-1;
        for(int k=0;k<n-1;k++)
            if (number[k] > number[k+1]){
                f = k;    
                break;
            }
        
        if (f == -1){
            // the number is tidy
            cout << "Case #" << t+1 << ": " << number << endl;
            continue;
        }
        
        while(f > 0 && number[f-1] == number[f])
            f--;

        number[f] = number[f]-1;
        
        // prefix 0
        if (f == 0 && number[f] == (0 + '0')){
            for(int k=0;k<n-1;k++)
                number[k] = 9 + '0';
            number[n-1] = 0;
        }
        else{
            for(int k=f+1;k<n;k++)
                number[k] = 9 + '0';
        }

        cout << "Case #" << t+1 << ": " << number << endl;
    }
    return 0;
}
