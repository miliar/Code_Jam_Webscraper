#include <iostream>
#include <string>
#include <stdio.h>

using namespace std;

int tryFlip(string s, int k){
    int a = 0;
    int count = 0;
    while(a+k <= s.size()){
        if(s.at(a) == '-'){
            for(int i=0 ; i<k ; i++){
                if(s.at(a+i) == '-') s.at(a+i) = '+';
                else if(s.at(a+i) == '+') s.at(a+i) = '-';
            }
            count++;
        }
        a++;
    }
    for(int i=a; i<s.size(); i++){
        if(s.at(i) == '-'){
            return -1;
        }
    }
    return count;
}

int main(){
    int n;
    double s[100][1000];
    double k[100][1000];
    double d[100];
    int m[100];
    cin >> n;
    for(int j=0; j<n; j++){
        cin >> d[j] >> m[j];
        for(int i=0; i<m[j]; i++){
            cin >> k[j][i] >> s[j][i];
        }
    }
    double maxTime[100];
    memset(maxTime, 0, sizeof(maxTime));
    for(int j=0; j<n; j++){
        for(int i=0; i<m[j]; i++){
            // cout << "fak\n";
            // cout << k[j][i] << " " << s[j][i] << "\n";
            double result = (double)(d[j] - k[j][i])/s[j][i];
            if(result > maxTime[j]){
                maxTime[j] = result;
                // cout << result << "\n";
            }
        }
    }
    cout.precision(15);

    for(int i=0 ; i<n ; i++)
    cout << "Case #" << i+1 << ": " << (double)d[i]/maxTime[i] << "\n";

    return 0;
}