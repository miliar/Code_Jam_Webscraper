#include <iostream>
using namespace std;

int flip(string pancake, int k) {
    int len = pancake.size();
    int sum = 0;
    int i = 0;
    for (i = 0; i < len - k; i++) {
        if(pancake[i] == '-') {
            sum++;
            for(int j = 0; j < k; j++)
                pancake[i + j] = pancake[i + j] == '+' ? '-' : '+';
        }
    }
    for(int j = i + 1; j < len; j++) {
        if(pancake[j] != pancake[i])
            return -1;
    }
    if(pancake[i] == '-')
        sum++;
    return sum;
}

int main(int argc, char* argv[])
{
    int t;
    cin>>t;
    for(int i=1;i<=t;i++){
        string s;
        int k;
        cin>>s>>k;
        int res = flip(s, k);
        cout<<"Case #"<<i<<": ";
        cout<<(res < 0 ? "IMPOSSIBLE" : to_string(res))<<endl;
    }

    return 0;
}
