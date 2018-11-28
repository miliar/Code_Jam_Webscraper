#include <bits/stdc++.h>

using namespace std;

vector<int> d;
long long N;


int main()
{
    freopen("C:\\Users\\Bibin\\Downloads\\B-small-attempt2.in", "r", stdin);
    freopen("C:\\Users\\Bibin\\Downloads\\output.txt", "w", stdout);


    int T;
    cin >> T;
    for(int t=1 ; t<=T; t++){

        cin >> N;
        d = vector<int>(0);
        while( N > 0){
            d.push_back(N%10);
            N = N/10;
        }

        reverse(d.begin(), d.end()); // 123 -> [1, 2, 3]


        int save = -1;
        bool first = true;
        for(int i=0; i<d.size()-1; i++){
            if(d[i] > d[i+1]){
                d[i] = d[i]-1;
                if(first){
                    d[i+1] = 9;
                    first = false;
                }
                save = i;
                i = i-2;
            }
        }

        if(save >= 0){
            for(int i=save+1; i< d.size(); i++){
                d[i] = 9;
            }
        }

        cout << "Case #" << t << ": ";
        for(int i=0; i<d.size(); i++){
            if(d[i] == 0){
                continue;
            }
            cout << d[i];
        }
        cout << "\n";
    }
}
