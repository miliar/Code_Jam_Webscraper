#include <bits/stdc++.h>


using namespace std;

vector<int> ToVector(long long number){
    vector<int> answer;
    while(number > 0){
        answer.push_back(number % 10);
        number /=10;
    }
    reverse(answer.begin()  , answer.end());
    return answer;
}

bool IsValid(long long number,long long limit){
    if(number > limit){
        return false;
    }
    vector<int> digits = ToVector(number);
    for(int i = 0; i  + 1 < digits.size(); ++i){
        if(digits[i] > digits[i + 1]){
            return false;
        }
    }
    return true;
}


void Solve(int numbercase){

    long long limit;
    cin >> limit;

    vector<int> number = ToVector(limit);
    long long maximum = 0;
    long long current = 0;
    for(int i = 0; i < number.size(); ++i){
        if(number[i] > 0){
            long long tmp = current * 10 + number[i] - 1;
            for(int rep = i + 1 ; rep < number.size(); ++rep){
                tmp = tmp * 10 + 9;
            }
            if(IsValid(tmp , limit)){
                maximum = max(maximum , tmp);
            }
        }
        current = current * 10 + number[i];
    }
    if(IsValid(current , limit)){
        maximum = max(maximum , current);
    }

    printf("Case #%d: %lld\n",numbercase , maximum);

}


int main(){

    freopen("B-large.in","r",stdin);
    freopen("output.c","w",stdout);

    int tc;
    cin >> tc;
    for(int numbercase = 1; numbercase <= tc; numbercase++){
        Solve(numbercase);
    }



    return 0;
}
