#include<iostream>
#include<string>
#include<cmath>
#include<vector>
#include<algorithm>

#define large unsigned long long

using namespace std;


bool cmp(int i, int j){
    return i > j;
}

int main(){
    int To;
    cin >> To;

    for(int T = 0; T < To; T++){
        large N, K;
        vector<int> numbers;
        cin >> N >> K;
        numbers.push_back(N);
        int height = log2(2 * K);
        for(int i = 0, l = 1; i < height; i++, l*=2){

            for(int j = numbers.size() - l, len = numbers.size(); j < len; j++){
                int element = numbers[j];
                if(element % 2 == 1){
                    numbers.push_back((element - 1)/2);
                    numbers.push_back((element - 1)/2);
                }
                else{
                    numbers.push_back(element/2);
                    numbers.push_back((element-1)/2);
                }
            }
        }


        sort(numbers.begin(), numbers.end(), cmp);

        int answer = numbers[K - 1], maxnum, minnum;

//        cout << endl;
//        for(number: numbers){
//          cout << number << " ";
//        }
//        cout << endl << answer <<endl;

        if(answer % 2 == 0){
            maxnum = answer/2;
            minnum = (answer - 1) / 2;
        }
        else{
            maxnum = minnum = (answer - 1) / 2;
        }

        cout << "Case #" << T+1/*N << " " << K*/ <<": "<< maxnum << " " << minnum << endl;
    }
}
