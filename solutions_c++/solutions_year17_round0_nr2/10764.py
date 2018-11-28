#include <iostream>
#include <vector>
#include <algorithm>
 
using namespace std; 
bool tiny(int input)
{
    int lastdigit = 20; 
    int digit;

    while (input > 0) {
        digit = input % 10;
        if (lastdigit < digit)
            return false;
        lastdigit = digit;
        input /= 10;
    }
    return true;
}
 
int main(){
    int t;
    cin >> t;
    int i = 1;
    while(i<=t){
        int n;
        cin >> n;
        while(n>0){
            if(tiny(n)){
                cout << "Case #" << i <<": "<< n << endl;
                break;
            }
            else
                n--;
        }
        i++;
    }
        
    return 0;
}