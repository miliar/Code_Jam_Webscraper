#include<iostream>
#include<algorithm>
#include<fstream>
#include <iomanip>
#include <queue>
using namespace std;
int main(){
    ifstream cin("C-large.in");
    //ofstream cout("result.txt");
    int n;
    cin >> n;
    for(int p = 0 ; p < n; p++){
        long long s,k;
        cin >> s >> k;
        //cout << "input : " << s << " " << k << endl;
        long long temp = k;
        long long counter=1;
        long long minn = 0;
        long long maxx = 1;
        long long min_val = s;
        long long max_val = s;

        int i = 0;
        while(true){
            temp = temp - counter;
            if(temp <= 0){
                temp = temp + counter;
                break;
            }
            counter = counter*2;
            if(max_val == min_val && max_val %2 != 0){
                maxx = maxx*2;
                minn = minn*2;
            }else if(max_val == min_val && max_val %2 == 0){
                maxx = minn+maxx;
                minn = maxx+minn;

            }else if(max_val%2 == 0){
                maxx = maxx;
                minn = minn*2+maxx;
            }else{
                maxx = maxx*2+minn;
                minn = minn;
            }
            max_val = max_val-((max_val-1)/2)-1;
            min_val = (min_val-1)/2;
            //cout << min_val  << " : "<< minn << " ______ " << max_val << " : " << maxx <<endl;

        }
        //cout << temp << endl;
        if(temp <= maxx)
            cout <<"Case #"<<p+1<<": " << max_val-(((max_val-1)/2)+1) << " " << (max_val-1)/2 << endl;
        else
            cout <<"Case #"<<p+1<<": " << min_val-(((min_val-1)/2)+1) << " " << (min_val-1)/2 << endl;
    }
}
