#include <iostream>
#include <cstring>

using namespace std;

int main(){
    int n;
    string c;
    cin>>n;
    for (int i = 0; i < n; i++){
        int k, result = 0;
        cin>>c>>k;
        int s = c.length();
        for (int j = 0; j < s - k + 1; j++){
            if (c[j] == '-'){
                result++;
                for (int l = j; l < j + k; l++)
                    c[l] = (c[l] == '+')? '-' : '+';
            }
        }
        for (int j = s - k; j < s; j++)
            if (c[j] == '-')
                result = -1;
        if (result >= 0)
            cout<<"Case #"<<i+1<<": "<<result<<endl;
        else
            cout<<"Case #"<<i+1<<": IMPOSSIBLE"<<endl;
    }
}
