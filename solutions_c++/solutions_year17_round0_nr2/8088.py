#include <iostream>

using namespace std;

int solve(string &numb){
    int n = numb.size();
    for(int i = 0; i<n-1; i++){
        if(numb[i] > numb[i+1]){
            for(int j = i; j>=1; j--){
                if(numb[j-1] > numb[j]-1){
                    continue;
                }else{
                    numb[j]--;
                    return j;
                }
            }
            numb[0]--;
            return 0;
        }
    }
    return numb.size();
}

int main()
{
    ios_base::sync_with_stdio(false);
    int t;
    cin >> t;
    for(int i = 1; i<=t; i++){
        string numb;
        cin >> numb;
        int nineStart = solve(numb);
        int j = 0;
        cout << "Case #" << i <<": ";
        if(numb[0] == '0')
            j++;
        for( ; j<numb.size(); j++){
            if(j<=nineStart){
                cout << numb[j];
            }else{
                cout << '9';
            }
        }
        cout << "\n";
    }
    return 0;
}
