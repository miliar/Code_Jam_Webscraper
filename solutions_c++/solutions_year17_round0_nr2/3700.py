//
// Created by Dai Tao on 2017/4/8.
//
#include <iostream>
#include <vector>
using namespace std;

// from the right to left, split the digits into array
void splitD(long long int N, vector<long long int> &container);
long long int doJob(long long int N, vector<long long int> &container);
long long int constructD(vector<long long int> &container);
int main(){
    int T;
    cin >> T;
    vector<long long int> container;
    for(int i = 0; i < T; i++){
        long long int N;
        cin >> N;
        cout << "Case #" << i + 1 << ": " << doJob(N, container) << endl;
        container.clear();
    }
}

void splitD(long long int N, vector<long long int> &container){
    while(N > 0){
        container.push_back(N % 10);
        N /= 10;
    }
}

long long int constructD(vector<long long int> &container){
    long long int result = 0;
    for(int i = container.size() - 1; i >= 0; i--){
        result *= 10;
        result += container[i];
    }
    return result;
}

long long int doJob(long long int N, vector<long long int> &container){
    splitD(N, container);
    if(container.size() == 1) return container[0];
    for(int i = 0; i < container.size() - 1; i++){
        if(container[i] >= container[i+1]) continue;
        else {
            for(int j = 0; j <= i; j++){
                container[j] = 9;
            }
            container[i+1]--;
        }
    }
    long long int result = constructD(container);
    return result;
}



