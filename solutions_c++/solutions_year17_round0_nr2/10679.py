#include <bits/stdc++.h>
#include <fstream>
using namespace std;

long long tidy(long long t){
    int aux = t;
    int sum = 0;
    vector <int> nums;
    while(aux % 10 != 0){
        nums.push_back(aux % 10);
        aux /= 10;
    }
    sort(nums.begin(), nums.end());
    for(int i = 0; i < nums.size(); i++){
        sum += nums[i] * (pow(10, nums.size() - (i + 1)));
    }
    return sum == t? true : false;
}

int main()
{
    ifstream fin("entrada.in");
    ofstream fout("salida.out");
    int n;
    int t;
    vector <int> output;
    fin >> n;
    for(int i = 0; i < n; ++i){
        fin >> t;
        while(!tidy(t)){
            t--;
        }
        output.push_back(t);
    }
    for(int i = 0; i < output.size(); i++){
        fout << "Case #" << i + 1 << ": " << output[i] << endl;
    }

    return 0;
}
